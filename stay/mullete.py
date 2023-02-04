import disnake
from disnake import TextInputStyle
from disnake.ext import commands
import random
from disnake.utils import *
from eco.func.func import *

bot = commands.InteractionBot()

class MulleteCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
    @bot.slash_command(description="игра в рулетку, ахха", options=[
        disnake.Option(name="cost", type=disnake.OptionType.number, description="Укажите ставку", required=True, min_value=50, max_value=1_000_000),
        disnake.Option(name="number", type=disnake.OptionType.string, description="Укажите число", required=True , 
            choices=["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","чёт","нечет","красное","черное"])])
    async def mullete(self, inter, cost, number):
        create(inter.guild.id, inter.author.id, 10)
        ss = check(inter.guild.id, inter.author.id, "bam")
        if ss == 1:
            error = disnake.Embed(description=f"**Причина:**\n> Вы в чс бота!",
            color=check_server_bd(inter.guild.id)[1], timestamp=datetime.datetime.now())
            error.set_author(name='Извините', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
            error.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.response.send_message(embed=error, ephemeral=True)
        else:
            balance=check(inter.guild.id, inter.author.id, "cash")
            if balance < cost:
                error = disnake.Embed(description=f"**Причина:**\n> У вас нет столько денег.\nВаш баланс: {int(balance):,}$",
                color=check_server_bd(inter.guild.id)[1], timestamp=datetime.datetime.now())
                error.set_author(name='Извините', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
                error.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
                await inter.response.send_message(embed=error, ephemeral=True)
            else:
                mas = random.randint(0, 20)
                color = random.choice(["красное", "черное"])
                if number == "красное":
                    if number == color:
                        num=cost
                        newbalance=balance+num
                        text=f"Поздравляем выпало `{mas}` (`{color}`) вы выйграли {int(num):,}$ ."
                    else:
                        num=0-cost
                        newbalance=balance+num
                        text=f"Увы выпало `{mas}` (`{color}`) вы проиграли {int(num):,} $."
                elif number == "черное":
                    if number == color:
                        num=cost
                        newbalance=balance+num
                        text=f"Поздравляем выпало `{mas}` (`{color}`) вы выйграли {int(num):,} $."
                    else:
                        num=0-cost
                        newbalance=balance+num
                        text=f"Увы выпало `{mas}` (`{color}`) вы проиграли {int(num):,} $."

                elif number == "чёт":
                    if mas % 2 == 0:
                        num=cost
                        newbalance=balance+num
                        text=f"Поздравляем выпало `{mas}` (`{color}`) вы выйграли {int(num):,} $."
                    else:
                        num=0-cost
                        newbalance=balance+num
                        text=f"Увы выпало `{mas}` (`{color}`) вы проиграли {int(num):,} $."

                elif number == "нечет":
                    if mas % 2 == 0:
                        num=0-cost
                        newbalance=balance+num
                        text=f"Увы выпало `{mas}` (`{color}`) вы проиграли {int(num):,} $."
                    else:
                        num=cost
                        newbalance=balance+num
                        text=f"Поздравляем выпало `{mas}` (`{color}`) вы выйграли {int(num):,} $."

                else:
                    if int(number) == mas:
                        if mas == "0":
                            num=cost*10
                            newbalance=balance+num
                            text=f"Поздравляем выпало `{mas}` вы выйграли {int(num):,} $."
                        else:
                            num=cost*5
                            newbalance=balance+num
                            text=f"Поздравляем выпало `{mas}` (`{color}`) вы выйграли {int(num):,}$ ."
                    else:
                        num=0-cost
                        newbalance=balance+num
                        text=f"Увы выпало `{mas}` (`{color}`) вы проиграли {int(num):,} $."
                embed=disnake.Embed(description=text, color=check_server_bd(inter.guild.id)[2])
                embed.set_footer(text=f"Ваш новый баланс: {int(newbalance):,} $", icon_url=f"{inter.author.avatar}")
                sql.execute(f"UPDATE user{inter.guild.id} SET cash = {int(newbalance)} WHERE id = '{inter.author.id}'")
                db.commit()
                await inter.response.send_message(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(MulleteCommand(bot))