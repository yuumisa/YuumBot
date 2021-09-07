from tokenize import triple_quoted
import discord
from discord.ext import commands

class fun_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.shatoCounter = 0
    
    @commands.command(name="shato", help="Sus Shato Counter")
    async def shato(self,ctx):
        self.shatoCounter += 1
        print(self.shatoCounter)
        await ctx.send("Shato has been sus " + str(self.shatoCounter) + " times ")

    @commands.command(name="test", help="test")
    async def test(self,ctx):
        await ctx.send("test")