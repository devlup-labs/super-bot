import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

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
    await ctx.channel.purge(limit=amount)
  
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client.run(TOKEN)
