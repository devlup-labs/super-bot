import discord
import os
import tweepy
from dotenv import load_dotenv
from discord.ext import commands

client = commands.Bot(command_prefix = ",")

@client.event
async def on_ready():
    print('super-bot is online!')

@client.command(aliases=['hi'])
async def hello(ctx):
    await ctx.send(f'Hello {ctx.author.mention}, SUPER-BOT here at your service')

@client.command()
async def dob(ctx):
    await ctx.send('I was born on the **LAST DAY OF 2020**, ready to embark a new beginning !')

@client.command(aliases=['latency'])
async def ping(ctx):
    await ctx.send(f'`My latency is {round(client.latency*1000)} ms`')



# twitter commands

#personal information
consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCES_TOKEN_SECRET')

# authentication of consumer key and secret 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
# authentication of access token and secret 
auth.set_access_token(access_token, access_token_secret) 
api = tweepy.API(auth)

# twitter client_id
twitter_client_id = api.me().id



# tweet command
@client.command()
async def tweet(ctx, *, msg):
    api.update_status(status = msg)

    tweet = api.user_timeline(id = twitter_client_id, count = 1)[0]
    tweet_text = tweet.text   
        #print(tweet.text)
    
    tweet_url = "https://twitter.com/<your_twitter_tagname>/status/" + str(tweet.id)

    for DGuild in client.guilds:
                for DChannel in DGuild.text_channels:
                    if DChannel.name == 'tweet-channel':

                        embed = discord.Embed(title = tweet.user.screen_name, description = tweet_text, colour  = discord.Colour.blue())
                        embed.add_field(name = "TWEET ID", value = tweet.id, inline = True)
                        embed.add_field(name = "TWEET URL", value = tweet_url, inline = True)
                        
#todo                   embed.set_thumbnail(url = tweet_url)

                        embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Posted by {ctx.author.name}")
                        embed.set_author(name='@your_twitter_tagname', icon_url=client.user.default_avatar_url)
                        await DChannel.send(embed = embed)



load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client.run(TOKEN)
