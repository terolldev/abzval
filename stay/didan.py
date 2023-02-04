import disnake
from disnake import TextInputStyle
from disnake.ext import commands
import random
from disnake.utils import *
from eco.func.func import *

bot = commands.InteractionBot()

class DidanCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.cooldown(rate=1, per=120, type=commands.BucketType.user)
    @bot.slash_command(description="Игра в дидан")
    @commands.guild_only()
    async def didan(self, ctx, money: commands.Range[1, 10000]):
        userr = ctx.author
        id = userr.id
        create(ctx.guild.id, id, 10)
        ss = check(ctx.guild.id,id, "bam")
        if ss == 1:
            await ctx.response.send_message("Вы в чс бота!", ephemeral=True)
        else:
            if money < 1:
                await ctx.response.send_message(embed=disnake.Embed(description=f"Укажите число больше 1",
                color=check_server_bd(ctx.guild.id)[1]), ephemeral=True)
            else:
                if check(ctx.guild.id,id,'prem') == 1: 
                    rand = random.randint(0,4)
                else: rand = random.randint(0,3)
                id = ctx.author.id
                cash = check(ctx.guild.id,id,'cash')
                if int(cash) < money:
                    await ctx.response.send_message(embed=disnake.Embed(description=f"У вас нет столько денег. Ваш баланс: {int(cash):,}{ex}",
                    color=check_server_bd(ctx.guild.id)[1]), ephemeral=True)
                else:
                    if rand == 0:
                        rand=rand
                        cash1 = int(money)
                        cash = int(cash) - cash1
                        cash1 = 0 - money
                    elif rand == 1:
                        cash = int(cash)
                        cash1 = 0
                    else:
                        rand=rand
                        cash1 = int(money) * rand
                        cash = int(cash) + cash1
                    sql.execute(f"UPDATE user{ctx.guild.id} SET cash = {cash} WHERE id = '{id}'")
                    db.commit()
                    await ctx.response.send_message(embed=disnake.Embed(description=f"Вы выйграли {int(cash1):,}{ex}. ваша ставка умножется на {rand}x. Ваш новый баланс: {int(cash):,}{ex}",
                    color=check_server_bd(ctx.guild.id)[2]))

def setup(bot: commands.Bot):
    bot.add_cog(DidanCommand(bot))