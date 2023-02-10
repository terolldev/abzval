import disnake
from disnake import TextInputStyle
from disnake.ext import commands
import random
from disnake.utils import *
from eco.func.func import *

bot = commands.InteractionBot()

class PayCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    @bot.slash_command(description="Передать деньги")
    @commands.guild_only()
    async def pay(self, ctx, user: disnake.User, money: int):
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
            if check(ctx.guild.id, id1, 'cash') == None:
                embed=disnake.Embed(description=f"**Причина:**\n> Такого юзера нет в бд!",
                color=check_server_bd(inter.guild.id)[1], timestamp=datetime.datetime.now())
                embed.set_author(name='Извините', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
                embed.set_footer(text=f"{ctx.author}", icon_url=f"{ctx.author.avatar}")
                await ctx.response.send_message(embed=embed, ephemeral=True)
            else:
                mon = check(ctx.guild.id, id, "cash")
                mon1 = check(ctx.guild.id, id1, "cash")
                inter = ctx
                if user.id == ctx.author.id:
                    embed=disnake.Embed(description=f"**Причина:**\n> Нельзя передать деньги себе!",
                    color=check_server_bd(inter.guild.id)[1], timestamp=datetime.datetime.now())
                    embed.set_author(name='Извините', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
                    embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
                    await inter.response.send_message(embed=embed, ephemeral=True)
                if money > int(mon):
                    embed=disnake.Embed(description=f"**Причина:**\n> У вас нету столько денег",
                    color=check_server_bd(inter.guild.id)[1], timestamp=datetime.datetime.now())
                    embed.set_author(name='Извините', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
                    embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
                    await inter.response.send_message(embed=embed, ephemeral=True)
                elif money < 1:
                    embed=disnake.Embed(description=f"**Причина:**\n> Укажите число больше 0!",
                    color=check_server_bd(inter.guild.id)[1], timestamp=datetime.datetime.now())
                    embed.set_author(name='Извините', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
                    embed.set_footer(text=f"{ctx.author}", icon_url=f"{inter.author.avatar}")
                    await inter.response.send_message(embed=embed, ephemeral=True)
                elif money > check_server_bd(inter.guild.id)[9]:
                    embed=disnake.Embed(description=f"**Причина:**\n> Укажите число меньше {int(check_server_bd(inter.guild.id)[9]):,}!",
                    color=check_server_bd(inter.guild.id)[1], timestamp=datetime.datetime.now())
                    embed.set_author(name='Извините', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
                    embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
                    await inter.response.send_message(embed=embed, ephemeral=True)
                elif check(ctx.guild.id, id1, 'pay') == 1:
                    embed=disnake.Embed(description=f"**Причина:**\n> Данный пользователь заблокировал переводы на свой аккаунт",
                    color=check_server_bd(inter.guild.id)[1], timestamp=datetime.datetime.now())
                    embed.set_author(name='Извините', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
                    embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
                    await inter.response.send_message(embed=embed, ephemeral=True)
                else:
                    mone = int(mon) - money
                    mone1 = int(mon1) + money
                    sql.execute(f"UPDATE user{ctx.guild.id} SET cash = {mone} WHERE id = '{id}'")
                    sql.execute(f"UPDATE user{ctx.guild.id} SET cash = {mone1} WHERE id = '{id1}'")
                    db.commit()
                    await ctx.response.send_message(embed=disnake.Embed(description=f"Вы передали {int(money):,}{ex} юзеру {user.mention}",
                             color=check_server_bd(inter.guild.id)[2]))

def setup(bot: commands.Bot):
    bot.add_cog(PayCommand(bot))