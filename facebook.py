class FacebookUser(object):
    """
    Facebook application
    """
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.friend_requests = []
        self.sent_friend_requests = []
        self.list_of_friends = []
        self.dict_of_comments = {}
        self.message = {}
        self.dummy_message = {}
        self.dict_of_comments.update({self:[]})

    def send_friend_request(self, user, msg=None):
        """
        Send friend request to other member
        """
        if user in self.sent_friend_requests:
            print 'Already send friend request to %s !!!' %user.name
        elif user in self.list_of_friends:
            print '%s already your friend !!!' %user.name
        else:
            self.sent_friend_requests.append(user)
            user.friend_requests.append(self)
            if msg:
                user.dummy_message.update({self:msg})

    def accept_friend_request(self, user):
        """
        Accepting friend request
        """
        if user not in self.friend_requests:
            print user.name,' did not send any friend request !!!'
        else:
            self.list_of_friends.append(user)
            user.list_of_friends.append(self)
            self.friend_requests.remove(user)
            user.sent_friend_requests.remove(self)

            if user in self.dummy_message.keys():
                self.message.update({user: self.dummy_message[user]})
                user.message.update({user: self.dummy_message[user]})

    def display_friend_list(self):
        """
        Show friend list
        """
        if self.list_of_friends == []:
            print 'Friend list is empty !!!'
        else:
            print 'Name       |       Gender'
            print '========================='
            for user in self.list_of_friends:
                print user.name,'  |  ',user.gender

    def comments(self, cmnt, user=None):
        """
        Comment on your object or your friend
        """
        if not user:
            self.dict_of_comments[self].append(cmnt)
        elif user in self.list_of_friends:
            user.dict_of_comments[user].append(cmnt)
        else:
            print 'You are not friend of ',user.name

    def display_comments(self, user=None):
        """
        Showing comments of your as well as your friends
        """
        if user == '':
            if self.dict_of_comments[self] == []:
                print 'No comments.'
            else:
                user = self
                for comment in self.dict_of_comments[user]:
                    print self.name,' ==> ',comment
        elif user in self.list_of_friends:
            if user.dict_of_comments[user] == []:
                print 'No comments.'
            else:
                for comment in user.dict_of_comments[user]:
                    print user.name,' ==> ',comment
        else:
            print 'You are not friend of ',user.name
