import disnake
from disnake import TextInputStyle
from disnake.ext import commands
import random
from disnake.utils import *
from eco.func.func import *
import requests
import json
import time

bot = commands.InteractionBot()

class TopCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    @bot.slash_command(description="Список лидеров", options=[disnake.Option(name="где", type=disnake.OptionType.string, choices=["деньги", "битки", "всё"], required=True)])
    async def top(self, inter, где: str):
        embedload=disnake.Embed(title="Загрузка...", color=check_server_bd(inter.guild.id)[2])
        start = time.time()
        await inter.response.send_message(embed=embedload, ephemeral=True)
        message = await inter.original_message()
        if где == "деньги":
            ex = "$"
            types = "cash"
        elif где == "битки":
            ex = "BTC"
            types = "bit"
        elif где == "всё":
            ex = "$"
            types = "cash,bit,prem"
        sql.execute(f"SELECT {types},id FROM user{inter.guild.id}")
        spis = list(sql.fetchall())
        embedload.description = "Загрузка участников..."
        await message.edit(embed=embedload)
        embed=disnake.Embed(title=f"Список лидеров по {где}", color=check_server_bd(inter.guild.id)[2])
        spis.sort(reverse=True)
        ren = range(0, 25)
        leader=[]
        defa = False
        if len(spis) < 25:
            ren = range(0, len(spis))
        embedload.description = "Делаю вычесление балансов..."
        await message.edit(embed=embedload)
        if types == "cash,bit,prem":
            url = "https://www.blockchain.com/ru/ticker"
            j = requests.get(url)
            js = json.loads(j.content)
            curs = js['USD']['buy']
            embedload.description = "Получение курса биткоина..."
            await message.edit(embed=embedload)
        for us in ren:
            if types == "cash,bit,prem":
                if spis[us][2] == 1:
                    prem = 2_000_000
                else:
                    prem = 0
                total=spis[us][0]+int(spis[us][1]*curs+prem)
                if total < 1:
                    pass
                else:
                    user=spis[us]
                    leader.append((total, user[3]))
            else:
                if spis[us][0] > 1:
                    user = spis[us]
                    leader.append((user[0], user[1]))
                else:
                    pass
        embedload.description = "Создаю массив..."
        await message.edit(embed=embedload)
        if len(leader) < 25:
            ren = range(0, len(leader))
        leader.sort(reverse=True)
        defa = True
        for us in ren:
            if us+1 > 10:
                defa=False
            user = leader[us]
            embed.add_field(name=f"{us+1} место", value=f"<@{user[1]}>: ```cs\n{int(user[0]):,} {ex}\n```", inline=defa)
        embedload.description = "Готово!"
        await message.edit(embed=embedload)
        end = time.time() - start
        if len(embed.fields)<1:
            embed.description=f"На сервере не у кого нету больше 1 {ex}"
        embed.set_footer(text=f"Время выполнение: {int(end)} сек")
        await message.edit(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(TopCommand(bot))