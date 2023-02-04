import disnake
from disnake import TextInputStyle
from disnake.ext import commands
import random
from disnake.utils import *
from eco.func.func import *

bot = commands.InteractionBot()

class HasleCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @bot.slash_command(description="Игра для самых успешных чуваков")
    async def hasle(self, inter, cost: commands.Range[10, 10_000_000], number: commands.Range[1, 5]):
        create(inter.guild.id, inter.author.id, 10)
        ss = check(inter.guild.id, inter.author.id, "bam")
        if ss == 1:
            error = disnake.Embed(description=f"**Причина:**\n> Вы в чс бота!",
            color=check_server_bd(inter.guild.id)[1], timestamp=datetime.datetime.now())
            error.set_author(name='Извините', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
            error.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.response.send_message(embed=error, ephemeral=True)
        else:
            bal = check(inter.guild.id, inter.author.id, "cash")
            if bal < cost:
                error = disnake.Embed(description=f"**Причина:**\n> У вас нету столько денег.\nВаш баланс: {int(bal):,} $",
                color=check_server_bd(inter.guild.id)[1], timestamp=datetime.datetime.now())
                error.set_author(name='Извините', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
                error.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
                await inter.response.send_message(embed=error, ephemeral=True)
            elif bal < 10000:
                error = disnake.Embed(description=f"**Причина:**\n> Вы недостаточно богатый.\nПолучите ещё: {int(10000-bal):,} $, и приходите снова",
                color=check_server_bd(inter.guild.id)[1], timestamp=datetime.datetime.now())
                error.set_author(name='Извините', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
                error.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
                await inter.response.send_message(embed=error, ephemeral=True)
            else:
                num = random.randint(1
                , 5)
                collectbonus = random.choice(["1.1","1.2","1.3","1.4","1.5"])
                variant = random.choice(["False","False","False","False","False","False","False","False","False",
                "False","False","False","False","False","False","False","False","False","False","True"])
                if number==num:
                    if variant == "True":
                        collectbonus=float(collectbonus)
                        bonus=cost*collectbonus-cost
                        text=f"Бонус за игру: `{int(bonus):,} $`"
                    elif variant == "False":
                        collectbonus = 1
                        text="`Бонуса за игру нету`"
                    newbal=bal+cost*collectbonus
                    textwin=f"Поздравляем вы выйграли {int(cost*collectbonus):,} $"
                else:
                    text=" "
                    newbal=bal-cost
                    textwin=f"Увы вы проиграли {int(cost):,} $"
                sql.execute(f"UPDATE user{inter.guild.id} SET cash = {int(newbal)} WHERE id = '{inter.author.id}'")
                db.commit()
                embed=disnake.Embed(title="Hasle Игра", description=f"{textwin}\n\n{text}", color=check_server_bd(inter.guild.id)[2])
                embed.set_footer(text=f"Ваш новый баланс: {int(newbal):,} $", icon_url=f"{inter.author.avatar}")
                await inter.response.send_message(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(HasleCommand(bot))