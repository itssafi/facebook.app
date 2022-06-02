from datetime import datetime


class FacebookUser:
    """
    Facebook application
    """
    def __init__(self, name: str, gender: str):
        self.name = name
        self.gender = gender
        self.friend_requests = []
        self.sent_friend_requests = []
        self.list_of_friends = []
        self.comment_box = {}
        self.message_box = {}
        self.dummy_message = {}
        self.now = datetime.now()

    def send_friend_request(self, user, msg: str = None):
        """
        Send friend request to other member
        """
        if user in self.sent_friend_requests:
            return 'Already send friend request to %s !!!' % user.name

        elif user is self:
            return "Can't send friend request to yourself"

        elif user in self.list_of_friends:
            return '%s already your friend !!!' % user.name

        elif user in self.friend_requests:
            return "%s already sent friend request to you !!!" % user.name

        self.sent_friend_requests.append(user)
        user.friend_requests.append(self)
        if msg:
            self.dummy_message[self] = (msg, datetime.now())

        return 'Friend request sent successfully to %s' % user.name

    def accept_friend_request(self, user):
        """
        Accepting friend request
        """
        if user not in self.friend_requests:
            return '%s did not send any friend request !!!' % user.name

        else:
            self.list_of_friends.append(user)
            user.list_of_friends.append(self)
            self.friend_requests.remove(user)
            user.sent_friend_requests.remove(self)

            user.comment_box[self] = []
            self.comment_box[user] = []

            self.message_box[user] = []
            user.message_box[self] = []

            if user in user.dummy_message.keys():
                self.message_box[user].append(user.dummy_message[user])
                del user.dummy_message[user]

            return 'You and %s now friends.' % user.name

    def send_message(self, user, msg):
        """
        Sending message to other friend
        """
        if user in self.sent_friend_requests:
            return "%s yet not accept your friend request !!!" % user.name

        if user in self.friend_requests:
            return "First accept %s's friend request !!!" % user.name

        if user not in self.list_of_friends:
            return "Message sending fail !!!\n%s is not your friend" % user.name

        user.message_box[self].append((msg, datetime.now()))
        return 'Message sent successfully to %s' % user.name

    def show_friend_request(self):
        """
        Showing all requested friends
        """
        if not self.friend_requests:
            return 'No friend request !!!'

        friend_req = []
        for user in self.friend_requests:
            if user in user.dummy_message:
                friend_req.append((user.name, user.dummy_message[user]))

            else:
                friend_req.append(user.name)

        return friend_req

    def show_friend_list(self):
        """
        Show friend list
        """
        if not self.list_of_friends:
            return 'Friend list is empty !!!'

        else:
            friend_list = []
            for user in self.list_of_friends:
                friend_list.append(user.name)
            return friend_list

    def comments(self, comment, user=None):
        """
        Comment on your object or your friend
        """
        if not user:
            self.comment_box[self].append((comment, datetime.now()))
            return "You commented '%s'." % comment

        if user in self.sent_friend_requests:
            return "%s yet not accept your friend request !!!" % user.name

        if user in self.friend_requests:
            return "First accept %s's friend request !!!" % user.name

        if user not in self.list_of_friends:
            return "%s is not your friend !!!" % user.name

        user.comment_box[self].append((comment, datetime.now()))
        return "You commented '%s' on %s" % (comment, user.name)

    def show_message(self, user):
        """
        Showing message of your as well as your friend
        """
        if user in self.message_box:
            return self.message_box[user]

        return []

    def show_comments(self, user=None):
        """
        Showing comments of your as well as your friend
        """
        if not user:
            if not self.comment_box:
                return "You don't have any comment !!!"

            return "You commented '%s' on you." % self.comment_box[self]

        elif self.is_exists(user.comment_box[self]) and self.is_exists(self.comment_box[user]):
            return ("You commented '%s' on %s.\n%s commented '%s' on you." % (user.comment_box[self],
                                                                              user.name, user.name,
                                                                              self.comment_box[user]))

        elif self.is_exists(user.comment_box[self]):
            return "You commented '%s' on %s." % (user.comment_box[self], user.name)

        elif self.is_exists(self.comment_box[user]):
            return "%s commented '%s' on you." % (user.name, self.comment_box[user])

        return "Don't have any comment either on you from %s or your on %s !!!" % (user.name, user.name)

    @staticmethod
    def is_exists(test_message):
        """
        Checking whether present or not
        """
        if test_message:
            return True

        return False
