import tweepy
from dotenv import load_dotenv
import os

load_dotenv()
Consumer_key=os.getenv('Consumer_key')
Consumer_secret=os.getenv('Consumer_secret')
Access_key=os.getenv('Access_key')
Access_secret=os.getenv('Access_secret')

auth=tweepy.OAuthHandler(Consumer_key,Consumer_secret)
auth.set_access_token(Access_key,Access_secret)
api=tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

@client.command()
async def tweet_post(ctx,*,text):
    api.update_status(text)
    await ctx.sent("Done")
    
