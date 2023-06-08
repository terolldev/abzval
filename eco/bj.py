import disnake
from disnake.ext import commands
import random
import json
from disnake.utils import *
from eco.func.func import *

bot = commands.InteractionBot()
bjcashe = {}

class BjSystem(disnake.ui.View):
    def __init__(self, cash):
        super().__init__(timeout=120)

    @disnake.ui.button(custom_id="bjb", label="Взять", style=disnake.ButtonStyle.green)
    async def take_button(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        card = random.randint(4, 10)
        bjcashe.update({interaction.author.id: [bjcashe[interaction.author.id][0]+card, bjcashe[interaction.author.id][1], bjcashe[interaction.author.id][2]]})
        card1 = random.randint(4, 10)
        bjcashe.update({interaction.author.id: [bjcashe[interaction.author.id][0], bjcashe[interaction.author.id][1]+card1, bjcashe[interaction.author.id][2]]})
        if bjcashe[interaction.author.id][0] == bjcashe[interaction.author.id][1]:
                date = bjcashe[interaction.author.id]
                embed=disnake.Embed(title=f"Выпала карта: {card}", description=f"Ничья\nВаш счёт: {date[0]}\nСчёт противника: {date[1]}")
                newcash = check(interaction.guild.id, interaction.author.id, "cash") - bjcashe[interaction.author.id][2]
                sql.execute(f"UPDATE user{interaction.guild.id} SET cash = {newcash} WHERE id = '{interaction.author.id}'")
                db.commit()
                embed.set_footer(text=f"Ваш новый баланс: {int(newcash):,} $")
                bjcashe.pop(interaction.author.id)
                await interaction.response.edit_message(embed=embed, view=None)
        elif bjcashe[interaction.author.id][1] == 21:
                date = bjcashe[interaction.author.id]
                embed=disnake.Embed(title=f"Выпала карта: {card}", description=f"Увы вы проиграли\n\nВаш счёт: {date[0]}\nСчёт противника: {date[1]}")
                newcash = check(interaction.guild.id, interaction.author.id, "cash") - bjcashe[interaction.author.id][2]
                sql.execute(f"UPDATE user{interaction.guild.id} SET cash = {newcash} WHERE id = '{interaction.author.id}'")
                db.commit()
                embed.set_footer(text=f"Ваш новый баланс: {int(newcash):,} $")
                bjcashe.pop(interaction.author.id)
                await interaction.response.edit_message(embed=embed, view=None)

        elif bjcashe[interaction.author.id][1] > 21:
                date = bjcashe[interaction.author.id]
                embed=disnake.Embed(title=f"Выпала карта: {card}", description=f"Вы выйграли\n\nВаш счёт: {date[0]}\nСчёт противника: {date[1]}")
                newcash = check(interaction.guild.id, interaction.author.id, "cash") + bjcashe[interaction.author.id][2]
                sql.execute(f"UPDATE user{interaction.guild.id} SET cash = {newcash} WHERE id = '{interaction.author.id}'")
                db.commit()
                embed.set_footer(text=f"Ваш новый баланс: {int(newcash):,} $")
                bjcashe.pop(interaction.author.id)
                await interaction.response.edit_message(embed=embed, view=None)
        elif bjcashe[interaction.author.id][0] == 21:
                date = bjcashe[interaction.author.id]
                embed=disnake.Embed(title=f"Выпала карта: {card}", description=f"Вы выйграли\n\nВаш счёт: {date[0]}\nСчёт противника: {date[1]}")
                newcash = check(interaction.guild.id, interaction.author.id, "cash") + bjcashe[interaction.author.id][2]
                sql.execute(f"UPDATE user{interaction.guild.id} SET cash = {newcash} WHERE id = '{interaction.author.id}'")
                db.commit()
                embed.set_footer(text=f"Ваш новый баланс: {int(newcash):,} $")
                bjcashe.pop(interaction.author.id)
                await interaction.response.edit_message(embed=embed, view=None)
        elif bjcashe[interaction.author.id][0] > 21:
                date = bjcashe[interaction.author.id]
                embed=disnake.Embed(title=f"Выпала карта: {card}", description=f"Увы у вас перебор\n\nВаш счёт: {date[0]}\nСчёт противника: {date[1]}")
                newcash = check(interaction.guild.id, interaction.author.id, "cash") - bjcashe[interaction.author.id][2]
                sql.execute(f"UPDATE user{interaction.guild.id} SET cash = {newcash} WHERE id = '{interaction.author.id}'")
                db.commit()
                embed.set_footer(text=f"Ваш новый баланс: {int(newcash):,} $")
                bjcashe.pop(interaction.author.id)
                await interaction.response.edit_message(embed=embed, view=None)
        elif bjcashe[interaction.author.id][0] < 21:
                date = bjcashe[interaction.author.id]
                embed=disnake.Embed(title=f"Выпала карта: {card}", description=f"У вас не перебор\n\nВаш счёт: {date[0]}\nСчёт противника: {date[1]}")
                await interaction.response.edit_message(embed=embed)
    
    
    @disnake.ui.button(custom_id="bjstay", label="Остановится", style=disnake.ButtonStyle.gray)
    async def stay_button(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        card1 = random.randint(4, 10)
        bjcashe.update({interaction.author.id: [bjcashe[interaction.author.id][0], bjcashe[interaction.author.id][1]+card1, bjcashe[interaction.author.id][2]]})
        date = bjcashe[interaction.author.id]
        if date[0] == date[1]:
            embed=disnake.Embed(title=f"Вы остановились", description=f"Ничья\n\nВаш счёт: {date[0]}\nСчёт противника: {date[1]}")
            newcash = check(interaction.guild.id, interaction.author.id, "cash") - date[2]
            sql.execute(f"UPDATE user{interaction.guild.id} SET cash = {newcash} WHERE id = '{interaction.author.id}'")
            db.commit()
            embed.set_footer(text=f"Ваш новый баланс: {int(newcash):,} $")
            await interaction.response.edit_message(embed=embed, view=None)
        elif date[1] == 21:
            embed=disnake.Embed(title=f"Вы остановились", description=f"Поражение\n\nВаш счёт: {date[0]}\nСчёт противника: {date[1]}")
            newcash = check(interaction.guild.id, interaction.author.id, "cash") - date[2]
            sql.execute(f"UPDATE user{interaction.guild.id} SET cash = {newcash} WHERE id = '{interaction.author.id}'")
            db.commit()
            embed.set_footer(text=f"Ваш новый баланс: {int(newcash):,} $")
            await interaction.response.edit_message(embed=embed, view=None)

        elif date[1] < date[0]:
            embed=disnake.Embed(title=f"Вы остановились", description=f"Победа\n\nВаш счёт: {date[0]}\nСчёт противника: {date[1]}")
            newcash = check(interaction.guild.id, interaction.author.id, "cash") + date[2]
            sql.execute(f"UPDATE user{interaction.guild.id} SET cash = {newcash} WHERE id = '{interaction.author.id}'")
            db.commit()
            embed.set_footer(text=f"Ваш новый баланс: {int(newcash):,} $")
            await interaction.response.edit_message(embed=embed, view=None)

        elif date[1] > date[0]:
            embed=disnake.Embed(title=f"Вы остановились", description=f"Поражение\n\nВаш счёт: {date[0]}\nСчёт противника: {date[1]}")
            newcash = check(interaction.guild.id, interaction.author.id, "cash") - date[2]
            sql.execute(f"UPDATE user{interaction.guild.id} SET cash = {newcash} WHERE id = '{interaction.author.id}'")
            db.commit()
            embed.set_footer(text=f"Ваш новый баланс: {int(newcash):,} $")
            await interaction.response.edit_message(embed=embed, view=None)
        bjcashe.pop(interaction.author.id)

class Bjcommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @bot.slash_command()
    async def showbjcashe(self, inter):
        await inter.response.send_message(bjcashe)

    @bot.slash_command(description="BlackJack")
    async def bj(self, inter, cash: commands.Range[10, 1000000]):
        if inter.author.id in bjcashe:
            await inter.response.send_message(embed=disnake.Embed(description="Закончите прошлую игру", color=check_server_bd(inter.guild.id)[2]), ephemeral=True)
        bjcashe.update({inter.author.id: [random.randint(5, 20), random.randint(5, 20), cash]})
        date = bjcashe[inter.author.id]
        embed = disnake.Embed(description=f"Ваш счёт: {date[0]}\nСчёт противника: {date[1]}")
        await inter.response.send_message(embed=embed, view=BjSystem(check(inter.guild.id, inter.author.id, "cash")), ephemeral=True)

def setup(bot: commands.Bot):
    bot.add_cog(Bjcommand(bot))
