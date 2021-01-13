import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
import sys
import random
 
client = commands.Bot(command_prefix = ",")

import tweet_bot

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
    
@client.command()
async def bye(ctx,*,text):
    r=["Ok, byee byee time to go offline",
        "good bye, i am also going offline",
       "See you later, i'mm also gonna go offline now :) ",
       "Going offline, bye >_< ",
       "ta-ta, gona go offline ",
       "ME go'in offline, Sayonara" 
        ]
    
    await ctx.send(r[random.randint(0,5)])
    sys.exit()                

@client.command()
async def tweet(ctx,*,text):
    text=text.split()
    dict1={'lobby':793547817372352525 , 'testing':793548437748056145 }
    channel = client.get_channel(dict1[text[0]])
    messages =await channel.history(limit=int(text[1])).flatten()
    await tweet_bot.tweet_post(ctx,text = messages[-1].content)
    #await channel.send('Done')

    


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client.run(TOKEN)

