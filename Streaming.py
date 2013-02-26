__author__ = 'amaatouq'

from MyStreamListener import MyStreamListener
import time, tweepy, sys
class Streaming(object):

    def __init__(self, credential = None):
        self.credential = credential
        self.keywords= None
        self.api = None
        self.listener = None
        self.auth1 = None
        self.connect()

    def connect(self):
        self.auth1 = tweepy.auth.OAuthHandler(self.credential['consumer_key'],self.credential['consumer_secret'])
        self.auth1.set_access_token(self.credential['access_token'],self.credential['access_token_secret'])
        self.api = tweepy.API(self.auth1)
        self.listener = MyStreamListener()

    def listen(self,keywords=None,location=None,users=None,follow=None):
        streamer = tweepy.Stream(auth=self.auth1,listener=self.listener,timeout=300000000000)
        streamer.filter(follow=follow,track=keywords,locations=location)








