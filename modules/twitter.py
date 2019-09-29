#!/usr/bin/env python
# encoding: utf-8
# 2019 Charles Thao cthao19@bu.edu


import tweepy #https://github.com/tweepy/tweepy
import json


#Twitter API credentials
api_keys = {}
with open('./api_key.json') as json_file:
    api_keys = json.load(json_file)

consumer_key = api_keys["twitter_consumer"]
consumer_secret = api_keys["twitter_consumer_secret"]
access_key = api_keys["twitter_access_token"]
access_secret = api_keys["twitter_access_secret"]

 
def get_all_tweets(product_name):
    print("Searching tweets for " + product_name)
    #Twitter only allows access to a users most recent 3240 tweets with this method
    
    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    
    #initialize a list to hold all the tweepy Tweets
    alltweets = tweepy.Cursor(api.search, q=str(product_name), geocode="42.361145,-71.057083,25km").items(20) 
    
    #make initial request for most recent tweets (200 is the maximum allowed count)
    # new_tweets = api.user_timeline(screen_name = product_name,count=10)
    tweet_lst = []
    for tweet in alltweets:
        tweet_lst.append(tweet.text)
    return tweet_lst
    

if __name__ == '__main__':
    #pass in the username of the account you want to download
    get_all_tweets("#iPhone11")