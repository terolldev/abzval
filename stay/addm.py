import disnake
from disnake import TextInputStyle
from disnake.ext import commands
import random
from disnake.utils import *
from eco.func.func import *

bot = commands.InteractionBot()

class AddmCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.cooldown(rate=1, per=1200, type=commands.BucketType.user)
    @bot.slash_command(description="Работать")
    @commands.guild_only()
    async def work(self, ctx):
        userr = ctx.author
        id = userr.id
        ss = check(ctx.guild.id, id, "bam")
        if ss == 1:
            await ctx.response.send_message("Вы в чс бота!", ephemeral=True)
        else:
            cash = random.randint(10, 30)
            mon = check(ctx.guild.id, id, "cash")
            mone = int(mon) + cash
            sql.execute(f"UPDATE user{ctx.guild.id} SET cash = {mone} WHERE id = '{id}'")
            db.commit()
            await ctx.response.send_message(embed=disnake.Embed(description=f"Вы проработали и заработали: {int(cash):,}{ex}. Ваш новый баланс: {int(mone):,}{ex}",
            color=check_server_bd(ctx.guild.id)[2]))

    @commands.cooldown(rate=1, per=1200, type=commands.BucketType.user)
    @bot.slash_command(description="Криминал!")
    @commands.guild_only()
    async def crime(self, ctx):
        userr = ctx.author
        id = userr.id
        ss = check(ctx.guild.id, id, "bam")
        if ss == 1:
            await ctx.response.send_message("Вы в чс бота!", ephemeral=True)
        else:
            cash = random.randint(-20, 30)
            mon = check(ctx.guild.id, id, "cash")
            mone = int(mon) + cash
            sql.execute(f"UPDATE user{ctx.guild.id} SET cash = {mone} WHERE id = '{id}'")
            db.commit()
            await ctx.response.send_message(embed=disnake.Embed(description=f"Вы ограбили ларёк и заработали: {int(cash):,}{ex}. Ваш новый баланс: {int(mone):,}{ex}",
            color=check_server_bd(ctx.guild.id)[2]))

def setup(bot: commands.Bot):
    bot.add_cog(AddmCommand(bot))