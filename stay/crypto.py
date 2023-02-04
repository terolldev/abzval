import disnake
from disnake import TextInputStyle
from disnake.ext import commands
import random
from disnake.utils import *
from eco.func.func import *
import requests
import json
from asyncio import sleep
import time

bot = commands.InteractionBot()

class Up(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=120)

    @disnake.ui.button(label="0/5", style=disnake.ButtonStyle.primary, emoji="🔄")
    async def count(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if interaction.user.id == interaction.author.id:
            button.label = button.label.replace('/5', '')
            number = int(button.label) if button.label else 0
            nice = self
            if number + 1 >= 5:
                nice = None
            button.label = str(number + 1) + '/5'
            embed=disnake.Embed(description=f"Курс: {int(price):,}{ex}\nПоследнее обновление: {format_dt(bit_time, 'R')}", color=check_server_bd(interaction.guild.id)[2])
            await interaction.response.edit_message(embed=embed,view=nice)

class CryptoCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(cog):
        print("['commands/eco/crypto.py']: Event update curs bit load")
        while True:
            url = "https://www.blockchain.com/ru/ticker"
            j = requests.get(url)
            js = json.loads(j.content)
            global price
            price = js['USD']['buy']
            global bit_time
            bit_time = time.time()
            await sleep(60)

    @commands.cooldown(rate=1, per=30, type=commands.BucketType.user)
    @bot.slash_command(description="Узнать курс бит-коина")
    @commands.guild_only()
    async def crypto(self, inter, value: int = None):
        if value == None:
            embed=disnake.Embed(description=f"Курс: {int(price):,}{ex}\nПоследнее обновление: {format_dt(bit_time, 'R')}", color=check_server_bd(inter.guild.id)[2])
            await inter.response.send_message(embed=embed, view=Up(), ephemeral=True)
        else:
            embed=disnake.Embed(description=f"{int(value):,} BTC это: {int(value * int(price)):,}{ex}\nПоследнее обновление: {format_dt(bit_time, 'R')}", color=check_server_bd(inter.guild.id)[2])
            await inter.response.send_message(embed=embed, ephemeral=True)

    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    @bot.slash_command(description="Передать бит-коин")
    @commands.guild_only()
    async def crypto_pay(self, ctx, user: disnake.User, value: int):
        userr=ctx.author
        id = userr.id
        ss = check(ctx.guild.id, id, "bam")
        if ss == 1:
            embed=disnake.Embed(description=f"**Причина:**\n> Вы в чс бота!",
            color=check_server_bd(inter.guild.id)[1], timestamp=datetime.datetime.now())
            embed.set_author(name='Извините', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
            embed.set_footer(text=f"{ctx.author}", icon_url=f"{ctx.author.avatar}")
            await ctx.response.send_message(embed=embed, ephemeral=True)
        else:
            id = ctx.author.id
            id1 = user.id
            create(ctx.guild.id, id, 10)
            if value < 1:
                    embed=disnake.Embed(description=f"**Причина:**\n> Укажите число больше 0!",
                    color=check_server_bd(ctx.guild.id)[1], timestamp=datetime.datetime.now())
                    embed.set_author(name='Извините', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
                    embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
                    await ctx.response.send_message(embed=embed, ephemeral=True)
            elif value > 100000:
                embed=disnake.Embed(description=f"**Причина:**\n> Укажите число меньше 100,000!",
                color=check_server_bd(ctx.guild.id)[1], timestamp=datetime.datetime.now())
                embed.set_author(name='Извините', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
                embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
                await ctx.response.send_message(embed=embed, ephemeral=True)

            elif check(ctx.guild.id, id1, 'cash') == None:
                embed=disnake.Embed(description=f"**Причина:**\n> Такого юзера нет в бд!",
                color=check_server_bd(ctx.guild.id)[1], timestamp=datetime.datetime.now())
                embed.set_author(name='Извините', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
                embed.set_footer(text=f"{ctx.author}", icon_url=f"{ctx.author.avatar}")
                await ctx.response.send_message(embed=embed, ephemeral=True)
            elif check(ctx.guild.id, id1, 'pay') == 1:
                    embed=disnake.Embed(description=f"**Причина:**\n> Данный пользователь заблокировал переводы на свой аккаунт",
                    color=check_server_bd(ctx.guild.id)[1], timestamp=datetime.datetime.now())
                    embed.set_author(name='Извините', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
                    embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
                    await ctx.response.send_message(embed=embed, ephemeral=True)
            elif user.id == ctx.author.id:
                    embed=disnake.Embed(description=f"**Причина:**\n> Нельзя передать деньги себе!",
                    color=check_server_bd(ctx.guild.id)[1], timestamp=datetime.datetime.now())
                    embed.set_author(name='Извините', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
                    embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
                    await ctx.response.send_message(embed=embed, ephemeral=True)
            else:
                mon = check(ctx.guild.id, id, "bit")
                mon1 = check(ctx.guild.id, id1, "bit")
                inter = ctx
                mone = int(mon) - value
                mone1 = int(mon1) + value
                sql.execute(f"UPDATE user{ctx.guild.id} SET bit = {mone} WHERE id = '{id}'")
                sql.execute(f"UPDATE user{ctx.guild.id} SET bit = {mone1} WHERE id = '{id1}'")
                db.commit()
                await ctx.response.send_message(embed=disnake.Embed(description=f"Вы передали {int(value):,} BTC, юзеру {user.mention}",
                color=check_server_bd(ctx.guild.id)[2]))
    
    @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
    @bot.slash_command(description="Продать бит-коин")
    @commands.guild_only()
    async def crypto_sell(self, inter, value: int):
        userr=inter.author
        id = userr.id
        ss = check(inter.guild.id, id, "bam")
        id = inter.author.id
        create(inter.guild.id, id, 10)
        money = check(inter.guild.id, id, 'cash')
        mon = value * int(price)
        newcash = int(money) + int(mon)
        value1 = int(check(inter.guild.id, id, 'bit'))
        val1 = value1 - value
        if ss == 1:
            embed=disnake.Embed(description=f"**Причина:**\n> Вы в чс бота!",
            color=check_server_bd(inter.guild.id)[1], timestamp=datetime.datetime.now())
            embed.set_author(name='Извините', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
            embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
        else:
            if value == None:
                embed=disnake.Embed(description=f"**Причина:**\n> Укажите сколько хотите продать BTC!",
                color=check_server_bd(inter.guild.id)[1], timestamp=datetime.datetime.now())
                embed.set_author(name='Извините', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
                embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            if value < 1:
                embed=disnake.Embed(description=f"**Причина:**\n> Укажите число больше 0",
                color=check_server_bd(inter.guild.id)[1], timestamp=datetime.datetime.now())
                embed.set_author(name='Извините', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
                embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            elif value > value1:
                embed=disnake.Embed(description=f"**Причина:**\n> У вас недостаточно BTC. Ваш баланс: {value1}",
                color=check_server_bd(inter.guild.id)[1], timestamp=datetime.datetime.now())
                embed.set_author(name='Извините', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
                embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            else:
                    sql.execute(f"UPDATE user{inter.guild.id} SET bit = {int(val1)} WHERE id = '{id}'")
                    sql.execute(f"UPDATE user{inter.guild.id} SET cash = {int(newcash)} WHERE id = '{id}'")
                    db.commit()
                    embed=disnake.Embed(description=f"Вы продали {int(value):,} BTC за {int(mon):,}{ex}", color=check_server_bd(inter.guild.id)[2])
            await inter.response.send_message(embed=embed)

    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    @bot.slash_command(description="Купить бит-коин")
    @commands.guild_only()
    async def crypto_buy(self, inter, value: int):
        userr=inter.author
        id = userr.id
        ss = check(inter.guild.id, id, "bam")
        if ss == 1:
            await inter.response.send_message("Вы в чс бота!", ephemeral=True)
        else:
            if value is None:
                    embed=disnake.Embed(description=f"**Причина:**\n> Где аргумент?",
                    color=check_server_bd(inter.guild.id)[1], timestamp=datetime.datetime.now())
                    embed.set_author(name='Извините', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
                    embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
                    await inter.response.send_message(embed=embed, ephemeral=True)
            elif value < 0:
                embed=disnake.Embed(description=f"**Причина:**\n> Укажите число больше 0",
                color=check_server_bd(inter.guild.id)[1], timestamp=datetime.datetime.now())
                embed.set_author(name='Извините', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
                embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
                await inter.response.send_message(embed=embed, ephemeral=True)
            elif value == -1:
                embed=disnake.Embed(description=f"**Причина:**\n> Укажите число меньше 250",
                color=check_server_bd(inter.guild.id)[1], timestamp=datetime.datetime.now())
                embed.set_author(name='Извините', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
                embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
                await inter.response.send_message(embed=embed, ephemeral=True)
            else:
                id = inter.author.id
                create(inter.guild.id, id, 10)
                money = check(inter.guild.id, id, 'cash')
                mon = value * int(price)
                newcash = int(money) - int(mon)
                value1 = int(check(inter.guild.id, id, 'bit')) + value
                mon33 = mon - int(money)
                if int(money) < int(mon):
                    embed=disnake.Embed(description=f"**Причина:**\n> Вам нужно ещё: {int(mon33):,}{ex}!",
                    color=check_server_bd(inter.guild.id)[1], timestamp=datetime.datetime.now())
                    embed.set_author(name='Извините', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
                    embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
                    await inter.response.send_message(embed=embed, ephemeral=True)
                else:
                    sql.execute(f"UPDATE user{inter.guild.id} SET bit = {int(value1)} WHERE id = '{id}'")
                    sql.execute(f"UPDATE user{inter.guild.id} SET cash = {int(newcash)} WHERE id = '{id}'")
                    db.commit()
                    embed=disnake.Embed(description=f"Вы купили {int(value):,} BTC за {int(mon):,}{ex}", color=check_server_bd(inter.guild.id)[2])
                    await inter.response.send_message(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(CryptoCommand(bot))