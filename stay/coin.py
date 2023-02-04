import disnake
from disnake import TextInputStyle
from disnake.ext import commands
import random
from disnake.utils import *
from eco.func.func import *

bot = commands.InteractionBot()

class CoinCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @bot.slash_command(description="Монетка!", options=[disnake.Option("сторона", "Укажите сторону", disnake.OptionType.string, 
    choices=["Орёл", "Решка"], required=True)])
    async def coinflip(self, inter, сторона):
        st = random.choice(["Орёл", "Решка"])
        if сторона == st:
            embed=disnake.Embed(title="Монетка!", description=f"Вы выйграли выпал(а) `{st}`", color=check_server_bd(inter.guild.id)[2])
        elif сторона is not st:
            embed=disnake.Embed(title="Монетка!", description=f"Вы проиграли выпал(а) `{st}`", color=check_server_bd(inter.guild.id)[2])
        await inter.response.send_message(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(CoinCommand(bot))