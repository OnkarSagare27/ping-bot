import discord
from discord.commands import SlashCommandGroup, option, slash_command
from discord.ext import commands
import json
import traceback
import requests

class Ping(commands.Cog):

    """
    Ping endpoints command
    ----------
    /ping <user>
    """

    def __init__(self, bot_: discord.Bot):
        self.bot = bot_


    @commands.slash_command(description='Ping OTTO', guild_only=True)
    async def ping(self, ctx: discord.ApplicationContext):
        await ctx.defer()
        file = open('jsons/endpoints.json', 'r')
        endpoints = json.load(file)
        embed = discord.Embed(title='Pinged!', description=f'```OTTO is up```', color=0x9678bf)
        while True:
            try:
                response = requests.get(endpoints['otto'])
                if response.status_code == 200:
                
                    await ctx.respod(embed=embed)
                    break
            except:
                response = requests.get(endpoints['otto'])
                if response.status_code == 200:
     
                    await ctx.respond(embed=embed)
                    break


        
        


    @commands.Cog.listener()
    async def on_application_command_error(self, ctx: discord.ApplicationContext, error: discord.DiscordException):
        if isinstance(error, commands.MemberNotFound):
            await ctx.respond("Not found error triggered.")
        else:
            raise error

def setup(bot):
    bot.add_cog(Ping(bot))
