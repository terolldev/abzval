import disnake
from disnake import TextInputStyle
from disnake.ext import commands
import random
from disnake.utils import *
from eco.func.func import *

bot = commands.InteractionBot()

class SlotsCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @bot.slash_command(description="Слоты казино фм")
    async def slots(self, inter, cost: commands.Range[1, 1_000_000]):
        create(inter.guild.id, inter.author.id, 10)
        ss = check(inter.guild.id, inter.author.id, "bam")
        if ss == 1:
            error = disnake.Embed(description=f"**Причина:**\n> Вы в чс бота!",
            color=check_server_bd(inter.guild.id)[1], timestamp=datetime.datetime.now())
            error.set_author(name='Извините', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
            error.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            return await inter.response.send_message(embed=error, ephemeral=True)
        defcost = cost
        _check = check(inter.guild.id, inter.author.id, "cash")
        if cost > check(inter.guild.id, inter.author.id, "cash"):
            error = disnake.Embed(description=f"**Причина:**\n> У вас недостаточно денег. Ваш баланс: {str(int(_check)):,}{ex}",
            color=check_server_bd(inter.guild.id)[1], timestamp=datetime.datetime.now())
            error.set_author(name='Извините', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
            error.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.response.send_message(embed=error, ephemeral=True)
        else:
            if check_user(inter.guild.id, inter.author.id, "str") == "win": slot = ["J"]
            else: slot = ["2", "3", "2", "2", "2", "3", "3", "2", "5", "J"]
            ran1 = random.choice(slot)
            ran2 = random.choice(slot)
            ran3 = random.choice(slot)
            if ran1 == "2":
                if ran2 == "2":
                    if ran3 == "2":
                        cost = cost * 2
                    else:
                        cost = 0
                else:
                    cost = 0

            elif ran1 == "3":
                if ran2 == "3":
                    if ran3 == "3":
                        cost = cost * 3
                    else:
                        cost = 0
                else:
                    cost = 0
            elif ran1 == "5":
                if ran2 == "5":
                    if ran3 == "5":
                        cost = cost * 5
                    else:
                        cost = 0
                else:
                    cost = 0
            elif ran1 == "J":
                if ran2 == "J":
                    if ran3 == "J":
                        cost = cost * 100
                    else:
                        cost = 0
                else:
                    cost = 0
            else:
                cost = 0
            if cost == 0:
                cost = cost - defcost
            bal = check(inter.guild.id, inter.author.id, "cash")
            sql.execute(f"UPDATE user{inter.guild.id} SET cash = {int(bal+cost)} WHERE id = '{inter.author.id}'")
            db.commit()
            await inter.response.send_message(embed=disnake.Embed(title=f"Слоты: || {ran1}, {ran2}, {ran3} || ", 
            description=f"Вы выйграли: **{int(cost):,}{ex}**.\n\nВаш новый баланс: **{int(bal+cost):,}{ex}**", 
            color=check_server_bd(inter.guild.id)[2]))

def setup(bot: commands.Bot):
    bot.add_cog(SlotsCommand(bot))