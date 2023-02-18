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
            che = check(inter.guild.id, user.id, "*")
            cash = che[1] # 1
            bit = che[2] # 2
            bam = che[3] # 3
            prem = che[4] # 4
            exp = che[5] # 5
            bitmine = che[6] # 6
            man = che[7] # 7
            datecreate = che[8] # 8
            coin = che[9] # 9
            ver = che[10] # 11
            show = che[11] # 12
            cris = che[12] # 13
            text=f"```cs\nДеньги: {int(cash):,} $\nБитКоины: {int(bit):,}\nБлокировка: {bool(bam)}\nПремиум статус: {bool(prem)}\nВерификация: {bool(ver)}\nМонеты: {int(coin):,}\nЗвание: {man}\nДата создание: {datecreate}\nОпыта: {exp}\nЗакрытый ли профиль: {bool(show)}\nУровень видео карт: {bitmine}\nКристаллики: {int(cris):,}\n```"
        embed=disnake.Embed(title=f"Информация об {user.name}", description=text, color=check_server_bd(inter.guild.id)[2])
        await inter.response.send_message(embed=embed, ephemeral=True)

def setup(bot: commands.Bot):
    bot.add_cog(CheckCommand(bot))