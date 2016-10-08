# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-07 17:30:51
# @Last Modified time: 2016-10-07 17:48:36
# @FileName: 355.py

import heapq

class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time = 0
        self.tweets = {}
        self.followee = {}


    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.time += 1
        self.tweets[userId] = self.tweets.get(userId, []) + [(-self.time,  tweetId)]

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        ans = []
        people = self.followee.get(userId, set()) | set([userId])
        for person in people:
            if person in self.tweets and self.tweets[person]:
                time, tweet = self.tweets[person][-1]
                ans.append((time, tweet, person, len(self.tweets[person]) - 1))
        heapq.heapify(ans)
        news = []
        for _ in range(10):
            if ans:
                time, tweet, person, idx = heapq.heappop(ans)
                news.append(tweet)
                if idx:
                    new_time, new_tweet = self.tweets[person][idx-1]
                    heapq.heappush(ans, (new_time, new_tweet, person, idx - 1))
        return news
        
        

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        self.followee[followerId] = self.followee.get(followeeId, set()) | set([followeeId])

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId in self.followee:
            self.followee[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)