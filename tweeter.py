import tweepy
import os
from dotenv import load_dotenv

# Twitter API keys
load_dotenv()
Consumer_key = os.getenv('CONSUMER_KEY')                    
Consumer_secret = os.getenv('CONSUMER_SECRET')                  
Access_key = os.getenv('ACCESS_KEY')                              
Access_secret = os.getenv('ACCESS_SECRET')                        

auth = tweepy.OAuthHandler(Consumer_key,Consumer_secret)
auth.set_access_token(Access_key,Access_secret)
api = tweepy.API(auth)
twitter_client_id = api.me().id
twitter_username = os.getenv('TWITTER_USERNAME')

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

def status_update(text):
    api.update_status(status = text)
    
def tweet_s():
    tweets = api.user_timeline(id = twitter_client_id, count = 1)[0]
    return tweets

def tweetText():
    tweets = tweet_s()
    tweet_text = tweets.text
    return tweet_text

def tweetURL():
    tweets = tweet_s()
    tweet_url = f"https://twitter.com/{twitter_username}/status/" + str(tweets.id)
    return tweet_url
