import validation
import tweepy
import json
import pprint
import csv
import datetime
import twint


#This function can be configured specify tweets from a specific user based on certain search keywords, dates, etc
def scrapeTweets():
    # Configure
    c = twint.Config()
    c.Username = "elonmusk"
    c.Search = "bitcoin"
    c.Store_csv = True
    c.Output = "elonTweets.csv"
    c.Limit = 100
    # Run
    twint.run.Search(c)

def get_tweets():
        # Authorization to consumer key and consumer secret
        auth = tweepy.OAuthHandler(validation.consumer_key, validation.consumer_secret)
  
        # Access to user's access key and access secret
        auth.set_access_token(validation.access_key, validation.access_secret)
        # Calling api
        api = tweepy.API(auth)
        user = api.get_user(screen_name='@elonmusk')
        tweets = []
        csvFile = open('elonsTweets2.csv', 'w')
        csvWriter = csv.writer(csvFile)
        pages = tweepy.Cursor(api.user_timeline,user_id=user.id_str, count=200,include_rts=True).pages(16)

        for page in pages:
            for tweet in page:
                csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
                tweets.append(tweet)
                print(tweet.text)
        csvFile.close()

get_tweets() 