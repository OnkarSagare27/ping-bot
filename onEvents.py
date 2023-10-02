from discord.ext import commands
import discord
import traceback

class Bot_Events(commands.Cog):

    def __init__(self, bot_: discord.Bot):
        self.bot = bot_


    @commands.Cog.listener()
    async def on_ready(self):
        print(f'[+] Logged in as {self.bot.user.name}')
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="/help"))

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'{member.name} just joined the server!')

    # @commands.Cog.listener()
    # async def on_application_command(self,ctx):
    #     channel = self.bot.get_channel(936069341693231155)
    #     if ctx.guild is None:
    #         server = "None"
    #     else:
    #         server = ctx.guild.name
    #     user = ctx.author
    #     command = ctx.data.name
    #     embed = discord.Embed(description=f"**{command} {ctx.filled_options}** \nused by {user.mention} [{user.name}] in {server} server",
    #                           color=discord.Color.blue())
    #     embed.set_thumbnail(url=user.display_avatar.url)
    #     await channel.send(embed=embed)

    # @commands.Cog.listener()
    # async def on_guild_join(self,guild):
     

    # @commands.Cog.listener()
    # async def on_guild_remove(self,guild):


    # @commands.Cog.listener()
    # async def on_slash_command_error(self, ctx: discord.ApplicationCommandInteraction, error: discord.ext.commands.CommandError):
    #     if isinstance(error, commands.MissingPermissions):
    #         embed = discord.Embed(
    #             description=f"You are missing permissions to use `/{ctx.application_command.qualified_name}`.\n"
    #                         f"**Permissions Required**: `{' '.join(error.missing_permissions)}`",
    #             color=discord.Color.red())
    #         return await ctx.send(embed=embed)
    #     elif isinstance(error, MissingGuildPlan):
    #         embed = discord.Embed(
    #             description=f"**This command requires a [guild subscription](https://www.patreon.com/magicbots).**",
    #             color=discord.Color.red())
    #         return await ctx.send(embed=embed)
    #     elif isinstance(error, commands.MessageNotFound) or isinstance(error, discord.NotFound):
    #         pass
    #     else:
    #         if ctx.guild is None:
    #             embed = discord.Embed(
    #                 description=f"This bot no longer allows commands in DM, please use commands in a server.",
    #                 color=discord.Color.red())
    #             await ctx.send(embed=embed, ephemeral=True)
    #         else:
    #             e = str(error)[0:3000]
    #             if "404 Not Found" in e:
    #                 return
    #             embed2 = discord.Embed(
    #                 description=f"Unhandled Error: {str(error)[0:3000]}",
    #                 color=discord.Color.red())
    #             channel = await self.bot.fetch_channel(989919520405725264)
    #             await channel.send(content=f"`/{ctx.application_command.qualified_name} {ctx.filled_options}`", embeds=[embed2])

    # @commands.Cog.listener()
    # async def on_application_command_error(self, ctx: discord.ApplicationContext, error: discord.DiscordException):
    #     if isinstance(error, commands.NotOwner):
    #         embed = discord.Embed(title="Missing permission", description=f"You can't use this command!", color=self.bot.embedColor)
    #         await ctx.respond(embed=embed)
    #     else:
    #         raise error



def setup(bot: commands.Bot):
    bot.add_cog(Bot_Events(bot))