import validation
import tweepy
import json
import pprint



def get_tweets(username):
        # Authorization to consumer key and consumer secret
        auth = tweepy.OAuthHandler(validation.consumer_key, validation.consumer_secret)
  
        # Access to user's access key and access secret
        auth.set_access_token(validation.access_key, validation.access_secret)
  
        # Calling api
        api = tweepy.API(auth)
  
        # 200 tweets to be extracted
        number_of_tweets=15000
        tweets = api.user_timeline(screen_name='elonmusk')
        
        
        
        # This code print out the first tweet pulled in JSON format
         data = tweets[0]._json
         pprint.pprint(data["created_date"])
        # Empty Array

        #tmp=[] 
  
        # create array of tweet information: username, 
        # tweet id, date/time, text
        #tweets_for_csv = [tweet.text for tweet in tweets] # CSV file created 
       # for j in tweets_for_csv:
  
            # Appending tweets to the empty array tmp
         #   tmp.append(j) 
  
        # Printing the tweets
       # for i in tmp:
            #print(i+"\n")

get_tweets("twitter-handle") 