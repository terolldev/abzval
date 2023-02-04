import disnake
from disnake.ext import commands
import requests
import datetime
import sqlite3
import time
import random
import json
from eco.func.func import *
from asyncio.tasks import sleep
from disnake.utils import *

db = sqlite3.connect(bd)
sql = db.cursor()

bot = commands.InteractionBot()

class Bal(disnake.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(disnake.ui.Button(label=f" ", style=disnake.ButtonStyle.green, disabled=True))
        self.add_item(disnake.ui.Button(label=f" ", style=disnake.ButtonStyle.primary, disabled=True))
        self.add_item(disnake.ui.Button(label=f" ", style=disnake.ButtonStyle.success, disabled=True))
        #self.add_item(disnake.ui.Button(label=f"|-----------------------------|", style=disnake.ButtonStyle.red, disabled=True, row=1))
        self.add_item(disnake.ui.Button(label=f" ", style=disnake.ButtonStyle.grey, disabled=True, row=2))
        self.add_item(disnake.ui.Button(label=f" ", style=disnake.ButtonStyle.grey, disabled=True, row=2))
        self.add_item(disnake.ui.Button(label=f" ", style=disnake.ButtonStyle.red, disabled=True, row=1))
        self.add_item(disnake.ui.Button(label=f" ", custom_id="MAINPURSE", style=disnake.ButtonStyle.green, disabled=False, row=2))

class Test(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    @bot.slash_command(description="Шаблон", guild_ids=[1044340714932293724, 966808361251270737])
    @commands.guild_only()
    async def шаблон(self, ctx):
            await ctx.response.send_message(embed=disnake.Embed(description=f"Профиль: \nДата создание аккаунта в базе: | [ ]\n\n\n```cs\nВаше звание: \n```",
            color=check_server_bd(ctx.guild.id)[2]), view=Bal(), ephemeral=True)

    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    @bot.slash_command(description="Рулетка(НЕ ДЕНЬГИ)")
    @commands.guild_only()
    async def roll(self, inter, макс: int):
        if макс < 2:
            embed=disnake.Embed(description=f"**Причина:**\n> Укажите число больше 1",
            color=check_server_bd(inter.guild.id)[1], timestamp=datetime.datetime.now())
            embed.set_author(name='Извините', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
            embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.response.send_message(embed=embed, ephemeral=True)
        else:
            rand = random.randint(1, макс)
            embed=disnake.Embed(description=f"Вам выпало {int(rand):,} из {int(макс):,}", color=check_server_bd(inter.guild.id)[1])
            await inter.response.send_message(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(Test(bot))