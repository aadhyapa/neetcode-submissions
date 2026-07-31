class Twitter:

    def __init__(self):
        self.users = {}
        self.count = 0

    def __addUser(self, userId):
            self.users[userId] = {}
            self.users[userId]['following'] = set()
            self.users[userId]['posts'] = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            self.users[userId] = {}
            self.users[userId]['following'] = set()
            self.users[userId]['posts'] = []
        
        self.count += 1
        self.users[userId]['posts'].append((self.count, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = [post for post in self.users[userId]['posts']]
        for followee in self.users[userId]['following']:
            heap.extend([post for post in self.users[followee]['posts']])
        heap.sort(reverse = True)
        feed = [tweetId for count, tweetId in heap[:10]]
        return feed
        

    def follow(self, followerId: int, followeeId: int) -> None:
        # if followeeId not in self.follows:
        #     self.follows[followeeId] = []
        # self.follows[followeeId].append(followerId)

        if followerId == followeeId:
            return

        if followeeId not in self.users:
           self.__addUser(followeeId)

        if followerId not in self.users:
            self.__addUser(followerId)

        self.users[followerId]['following'].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return

        if followeeId not in self.users:
           self.__addUser(followeeId)

        if followerId not in self.users:
            self.__addUser(followerId)

        self.users[followerId]['following'].discard(followeeId)

