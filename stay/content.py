import disnake
from disnake.ext import commands
from eco.func.func import *

bot = commands.InteractionBot()

class Brawl11Command(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.cooldown(rate=1, per=20, type=commands.BucketType.user)
    @bot.slash_command(description="Политика бота")
    @commands.dm_only()
    async def content(self, inter):
        await inter.response.defer()
        embed=disnake.Embed(title="Правила!",
        description=Text.content, color=0x0540ca)
        await inter.followup.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(Brawl11Command(bot))