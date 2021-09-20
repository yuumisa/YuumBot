from inspect import CO_GENERATOR
import discord
from discord import voice_client
from discord.ext import commands
import os
from discord import FFmpegPCMAudio
from discord.ext.commands import bot
from discord.ext.commands.core import command
import youtube_dl
import asyncio
from variables import *
from music_cog import music_cog
from fun_cog import fun_cog

intents = discord.Intents.default()
client = commands.Bot(command_prefix = '&', intents = intents)

client.add_cog(music_cog(client))
client.add_cog(fun_cog(client))
social = {"134117892747821056": {"twitter": "totheskye_"}}

@client.event
async def on_ready():
  print('YuumBot is operational')

@client.command()
async def bio(ctx):
    await ctx.channel.send("I am YuumBot. Current Version: 1.3. As of right now, I am primarily a music bot. Full list of features coming soon via &help. Ask <@!134117892747821056> about anything regarding me.")

@client.command()
async def join(ctx):
  if(ctx.author.voice is None):
    await ctx.channel.send("You're not in a voice channel bro")
  else:
    channel = ctx.author.voice.channel
    await channel.connect()

@client.command()
async def leave(ctx):
  if(ctx.voice_client is None):
    await ctx.channel.send("I'm not in a voice channel bro")
  else:
    await ctx.voice_client.disconnect()

@client.command()
async def addTwitter(ctx, username):
  social["user"] = str(ctx.author.id)
  social["user"][str(ctx.author.id)]["twitter"] = str(username)
  await ctx.send(social)

@client.command()
async def printS(ctx):
  u2 = { "12312622": {"twitter": "idk"}}
  social.update(u2)
  await ctx.send(social)

@client.command()
async def embed(ctx):
  id = str(ctx.author.id)
  embed=discord.Embed(title="Profile", description="<@!" + id + ">", color=0x38ccc9)
  embed.set_author(name=ctx.message.author.name)
  embed.set_thumbnail(url=ctx.message.author.avatar_url)
  embed.add_field(name="Date Joined", value = ctx.message.author.joined_at.strftime("%b %d, %Y"))
  embed.add_field(name="Twitter", value = "https://twitter.com/totheskye_")
  embed.set_footer(text="Profile")
  #embed.set_image(ctx.message.author.user.avatar_url)
  await ctx.send(embed=embed)

client.run(token)

 