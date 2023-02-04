import disnake
from disnake import TextInputStyle
from disnake.ext import commands
import random
from disnake.utils import *
from eco.func.func import *

bot = commands.InteractionBot()

class CasinoCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
    @bot.slash_command(description="POV: всрать деньги. игра в казино")
    @commands.guild_only()
    async def casino(self, ctx, money: int):
        user=ctx.author
        id = user.id
        ss = check(ctx.guild.id, id, "bam")
        if ss == 1:
            await ctx.response.send_message("Вы в чс бота!", ephemeral=True)
        else:
            id = ctx.author.id
            create(ctx.guild.id, id, 10)
            if money < 1:
                embed=disnake.Embed(description=f"**Причина:**\n> Укажите число больше 0!",
                color=check_server_bd(ctx.guild.id)[1], timestamp=datetime.datetime.now())
                embed.set_author(name='Извините', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
                embed.set_footer(text=f"{ctx.author}", icon_url=f"{ctx.author.avatar}")
                await ctx.response.send_message(embed=embed, ephemeral=True)
            else:
                mon = check(ctx.guild.id, id, "cash")
                if money > int(mon):
                    embed=disnake.Embed(description=f"**Причина:**\n> У вас недостаточно денег. Ваш баланс: {mon}{ex}",
                    color=check_server_bd(ctx.guild.id)[1], timestamp=datetime.datetime.now())
                    embed.set_author(name='Извините', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
                    embed.set_footer(text=f"{ctx.author}", icon_url=f"{ctx.author.avatar}")
                    await ctx.response.send_message(embed=embed, ephemeral=True)
                elif money > 1_000_000:
                    await ctx.response.send_message(embed=disnake.Embed(description=f"Укажите число меньше 1 млн.",
                         color=check_server_bd(ctx.guild.id)[2]), ephemeral=True)
                else:
                    if check(ctx.guild.id, id,'prem') == 1: num = random.randint(1, 3)
                    else: num = random.randint(1, 2)
                    if num == 1:
                        mon = check(ctx.guild.id, id, "cash")
                        mone = int(mon) + money 
                        sql.execute(f"UPDATE user{ctx.guild.id} SET cash = {mone} WHERE id = '{id}'")
                        db.commit()
                        await ctx.response.send_message(embed=disnake.Embed(description=f"Поздравляем вы выйграли. Ваш новый баланс: {int(mone):,}{ex}",
                         color=check_server_bd(ctx.guild.id)[2]))
                    elif num == 2:
                        mon = check(ctx.guild.id, id, "cash")
                        mone = int(mon) - money
                        sql.execute(f"UPDATE user{ctx.guild.id} SET cash = {mone} WHERE id = '{id}'")
                        db.commit()
                        await ctx.response.send_message(embed=disnake.Embed(description=f"Увы но вы проиграли. Ваш новый баланс: {int(mone):,}{ex}",
                         color=check_server_bd(ctx.guild.id)[2]))
                    elif num == 3:
                        mon = check(ctx.guild.id, id, "cash")
                        mone = int(mon) + money 
                        sql.execute(f"UPDATE user{ctx.guild.id} SET cash = {mone} WHERE id = '{id}'")
                        db.commit()
                        await ctx.response.send_message(embed=disnake.Embed(description=f"Поздравляем вы выйграли. Ваш новый баланс: {int(mone):,}{ex}",
                         color=check_server_bd(ctx.guild.id)[2]))

def setup(bot: commands.Bot):
    bot.add_cog(CasinoCommand(bot))