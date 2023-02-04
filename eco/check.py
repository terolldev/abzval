import disnake
from disnake import TextInputStyle
from disnake.ext import commands
import random
from disnake.utils import *
from eco.func.func import *

bot = commands.InteractionBot()

class CheckCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.has_permissions(administrator=True)
    @bot.slash_command(description="Посмотреть инфу")
    async def check(self, inter, user: disnake.User):
        if check(inter.guild.id, user.id, "cash") == None:
            text="Ошибка, такого юзера нету"
        else:
            cash=check(inter.guild.id, user.id, "cash")
            bit=check(inter.guild.id, user.id, "bit")
            bam=check(inter.guild.id, user.id, "bam")
            prem=check(inter.guild.id, user.id, "prem")
            ver=check(inter.guild.id, user.id, "ver")
            coin=check(inter.guild.id, user.id, "coin")
            man=check(inter.guild.id, user.id, "man")
            datecreate=check(inter.guild.id, user.id, "datecre")
            exp=check(inter.guild.id, user.id, "exp")
            show=check(inter.guild.id, user.id, "show")
            bitmine=check(inter.guild.id, user.id, "bitmine")
            cris=check(inter.guild.id, user.id, "cris")
            text=f"```cs\nДеньги: {int(cash):,} $\nБитКоины: {int(bit):,}\nБлокировка: {bool(bam)}\nПремиум статус: {bool(prem)}\nВерификация: {bool(ver)}\nМонеты: {int(coin):,}\nЗвание: {man}\nДата создание: {datecreate}\nОпыта: {exp}\nЗакрытый ли профиль: {bool(show)}\nУровень видео карт: {bitmine}\nКристаллики: {int(cris):,}\n```"
        embed=disnake.Embed(title=f"Информация об {user.name}", description=text, color=check_server_bd(inter.guild.id)[2])
        await inter.response.send_message(embed=embed, ephemeral=True)

def setup(bot: commands.Bot):
    bot.add_cog(CheckCommand(bot))