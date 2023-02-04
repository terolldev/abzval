import disnake
from disnake import TextInputStyle
from disnake.ext import commands
import random
from disnake.utils import *
from eco.func.func import *

bot = commands.InteractionBot()

class ShipsCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @bot.slash_command(description="Узнай свою любовь")
    async def ships(self, inter, user: disnake.User):
        random.seed(inter.author.id*user.id)
        embed=disnake.Embed(title=f"Ваша любовь с {user.name}", description=f"```cs\n{random.randint(1, 100)} %\n```", color=check_server_bd(inter.guild.id)[2])
        await inter.response.send_message(embed=embed)        

def setup(bot: commands.Bot):
    bot.add_cog(ShipsCommand(bot))