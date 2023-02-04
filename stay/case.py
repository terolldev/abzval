import disnake
from disnake.ext import commands
import requests
import random
import datetime
from disnake.utils import *
import sqlite3
import time
from eco.func.func import *
from eco.func.cs import generate

bot = commands.InteractionBot()

bd = 'bd.db'

db = sqlite3.connect(bd)
sql = db.cursor()

ex = "$"

class CaseCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @bot.slash_command(description="Кейсы!")
    async def case(self, inter):
        pass

    @commands.cooldown(rate=1, per=120, type=commands.BucketType.user)
    @case.sub_command(name="buy", description=f"Открыть кейс за 100.000{ex}")
    async def case1(self, inter):
        id = inter.author.id
        money = check(inter.guild.id, id, 'cash')
        money1 = check(inter.guild.id, id, 'bit')
        if int(money) < 100_000:
            await inter.response.send_message(f"У вас недостаночно денег. Ваш баланс: {money}{ex}",
            ephemeral=True)
        else:
            money = int(money) - 100_000
            newcash1 = money
            sql.execute(f"UPDATE user{inter.guild.id} SET cash = {newcash1} WHERE id = '{id}'")
            db.commit()
            drop = random.choice(['100.000$', '1.000.000$', '1BTC', '10BTC', '10.000$', '100.000$', '5BTC',
            '1.000.000$', '25BTC', '1BTC', '50BTC', '1$', '10$', '100$', '10.000$'])
            embed = disnake.Embed(description=f"Поздравляем вам выпало: {drop}", color=check_server_bd(inter.guild.id)[2])
            if drop == '100.000$':
                newcash = int(money) + 100_000
                sql.execute(f"UPDATE user{inter.guild.id} SET cash = {newcash} WHERE id = '{id}'")
                db.commit()
                await inter.response.send_message(embed=embed)
            elif drop == '1.000.000$':
                newcash = int(money) + 1_000_000
                sql.execute(f"UPDATE user{inter.guild.id} SET cash = {newcash} WHERE id = '{id}'")
                db.commit()
                await inter.response.send_message(embed=embed)
            elif drop == '1BTC':
                newcash = int(money1) + 1
                sql.execute(f"UPDATE user{inter.guild.id} SET bit = {newcash} WHERE id = '{id}'")
                db.commit()
                await inter.response.send_message(embed=embed)
            elif drop == '10BTC': 
                newcash = int(money1) + 10
                sql.execute(f"UPDATE user{inter.guild.id} SET bit = {newcash} WHERE id = '{id}'")
                db.commit()
                await inter.response.send_message(embed=embed)
            elif drop == '10.000$': 
                newcash = int(money) + 10_000
                sql.execute(f"UPDATE user{inter.guild.id} SET cash = {newcash} WHERE id = '{id}'")
                db.commit()
                await inter.response.send_message(embed=embed)
            elif drop == '1$':
                newcash = int(money) + 1
                sql.execute(f"UPDATE user{inter.guild.id} SET cash = {newcash} WHERE id = '{id}'")
                db.commit()
                await inter.response.send_message(embed=embed)
            elif drop == '10$':
                newcash = int(money) + 10
                sql.execute(f"UPDATE user{inter.guild.id} SET cash = {newcash} WHERE id = '{id}'")
                db.commit()
                await inter.response.send_message(embed=embed)
            elif drop == '100$':
                newcash = int(money) + 100
                sql.execute(f"UPDATE user{inter.guild.id} SET cash = {newcash} WHERE id = '{id}'")
                db.commit()
                await inter.response.send_message(embed=embed)
            elif drop == '5BTC':
                newcash = int(money1) + 5
                sql.execute(f"UPDATE user{inter.guild.id} SET bit = {newcash} WHERE id = '{id}'")
                db.commit()
                await inter.response.send_message(embed=embed)
            elif drop == '25BTC':
                newcash = int(money1) + 25
                sql.execute(f"UPDATE user{inter.guild.id} SET bit = {newcash} WHERE id = '{id}'")
                db.commit()
                await inter.response.send_message(embed=embed)
            elif drop == '50BTC': 
                newcash = int(money1) + 50
                sql.execute(f"UPDATE user{inter.guild.id} SET bit = {newcash} WHERE id = '{id}'")
                db.commit()
                await inter.response.send_message(embed=embed)
            else:
                await inter.response.send_message("Ошибка, дроп не найден", ephemeral=True)

    @case.sub_command(name="cs", description="Легендарные кейсы снова в деле!")
    async def cases(self, inter):
        gen = generate('')
        if gen[1] == "p": color=0xff00f7
        elif gen[1] == "s": color=0x36393f
        elif gen[1] == "g": color=disnake.Colour.gold()
        elif gen[1] == "r": color=disnake.Colour.red()
        elif gen[1] == "pp": color=disnake.Colour.purple()
        elif gen[1] == "b": color=disnake.Colour.blue() 
        embed=disnake.Embed(title="Кейс", description=f"Вам выпало: {gen[0]}{gen[3]}\nКачество: {gen[2]}", color=color)
        await inter.response.send_message(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(CaseCommand(bot))