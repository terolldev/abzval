import disnake
from disnake import TextInputStyle
from disnake.ext import commands
import random
from disnake.utils import *
from eco.func.func import *

bot = commands.InteractionBot()

class JackCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
    @bot.slash_command(description="Джак, игра в чёт, нечет. Игра для очень богатых", options=[
        disnake.Option(name="cost", type=disnake.OptionType.number, description="Укажите ставку", required=True, min_value=50, max_value=1_000_000),
        disnake.Option(name="eand", type=disnake.OptionType.string, description="Укажите чёт или нечет", required=True, choices=["нечет","чёт"])])
    async def jack(self, inter, cost, eand):
        create(inter.guild.id, inter.author.id, 10)
        ss = check(inter.guild.id, inter.author.id, "bam")
        if ss == 1:
            error = disnake.Embed(description=f"**Причина:**\n> Вы в чс бота!",
            color=check_server_bd(inter.guild.id)[1], timestamp=datetime.datetime.now())
            error.set_author(name='Извините', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
            error.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.response.send_message(embed=error, ephemeral=True)
        else:
            bala = check(inter.guild.id, inter.author.id, "cash")
            if bala < cost:
                error = disnake.Embed(description=f"**Причина:**\n> У вас нет столько денег.\nВаш баланс: {int(bala):,}$",
                color=check_server_bd(inter.guild.id)[1], timestamp=datetime.datetime.now())
                error.set_author(name='Извините', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
                error.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
                return await inter.response.send_message(embed=error, ephemeral=True)
            else: pass
            massive = random.randint(1, 9)
            if massive % 2 == 0:
                if eand == "чёт":
                    won = cost
                    text = f"Поздравляем вы выйграли {int(won):,}$"
                else:
                    won = 0 - cost
                    text = f"Увы но вы проиграли {int(won):,}$"
            else:
                if eand == "нечет":
                    won = cost
                    text = f"Поздравляем вы выйграли {int(won):,}$"
                else:
                    won = 0 - cost
                    text = f"Увы но вы проиграли {int(won):,}$"

            embed=disnake.Embed(
                description=text,
                color=check_server_bd(inter.guild.id)[2]
                )
            bal = bala + won
            embed.set_footer(text=f"Ваш новый баланс: {int(bal):,} $", icon_url=f"{inter.author.avatar}")
            sql.execute(f"UPDATE user{inter.guild.id} SET cash = {int(bal)} WHERE id = '{inter.author.id}'")
            db.commit()
            await inter.response.send_message(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(JackCommand(bot))