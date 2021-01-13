import tweepy
import discord
from discord.ext import commands
 
client = commands.Bot(command_prefix = ",")

Consumer_key=''
Consumer_secret=''
Access_key=''
Access_secret=''

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
    api.update_status("#"+text)
    await ctx.send("Done")

'''
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client.run(TOKEN)

'''
