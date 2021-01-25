import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
import tweeter

client = commands.Bot(command_prefix = "\\")

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

@client.command(aliases=['c'])
@commands.has_permissions(manage_messages = True)
async def clear(ctx, amount=2):
       await ctx.channel.purge(limit = amount)

# tweet command
@client.command()
async def tweet(ctx, amount=1):
    await ctx.channel.purge(limit=1)

    msgs = []
    async for msg in ctx.channel.history(limit=amount):
        msgs.append(msg.content)
    msgs.reverse()

    messages = ''
    for msg in msgs:
        messages = messages + msg + '\n'
    
    tweeter.status_update(messages)
    tweets = tweeter.tweet_s()
    tweet_text = tweeter.tweetText()
    tweet_url = tweeter.tweetURL()
    twitter_username = os.getenv('TWITTER_USERNAME')
    response_channel = os.getenv('RESPONSE_CHANNEL_NAME')
    
    for DGuild in client.guilds:
        for DChannel in DGuild.text_channels:
            if DChannel.name == f'{response_channel}':

                embed = discord.Embed(title = tweets.user.screen_name, description = tweet_text, colour  = discord.Colour.blue())
                embed.add_field(name = "TWEET ID", value = tweets.id, inline = True)
                embed.add_field(name = "TWEET URL", value = tweet_url, inline = True)
                embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Posted by {ctx.author.name}")
                embed.set_author(name=f'@{twitter_username}', icon_url=client.user.default_avatar_url)
                await DChannel.send(embed = embed)

# Loading the token from dotenv
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Running the bot
client.run(TOKEN)
