import disnake
from disnake import TextInputStyle
from disnake.ext import commands
import random
from disnake.utils import *
from eco.func.func import *

bot = commands.InteractionBot()

class Bal(disnake.ui.View):
    def __init__(self, money: str, bit1: str, exp: str, lvl: str, prem: int, coin: int, ver: int):
        super().__init__()
        money = int(money)
        bit1 = int(bit1)
        coin = int(coin)
        self.add_item(disnake.ui.Button(label=f"{money:,} {ex}", style=disnake.ButtonStyle.green, disabled=True))
        self.add_item(disnake.ui.Button(label=f"{bit1:,} BTC", style=disnake.ButtonStyle.primary, disabled=True))
        self.add_item(disnake.ui.Button(label=f"{coin:,} COIN", style=disnake.ButtonStyle.success, disabled=True))
        #self.add_item(disnake.ui.Button(label=f"|-----------------------------|", style=disnake.ButtonStyle.red, disabled=True, row=1))
        self.add_item(disnake.ui.Button(label=f"{exp} EXP", style=disnake.ButtonStyle.grey, disabled=True, row=2))
        self.add_item(disnake.ui.Button(label=f"{lvl} LVL", style=disnake.ButtonStyle.grey, disabled=True, row=2))
        if prem == 1:
            self.add_item(disnake.ui.Button(label=f"Premium User", style=disnake.ButtonStyle.red, disabled=True, row=1))
            if ver == 1:
                self.add_item(disnake.ui.Button(label=f" ", emoji='✅', custom_id="MAINPURSE", style=disnake.ButtonStyle.green, disabled=False, row=2))
        elif ver == 1:
            self.add_item(disnake.ui.Button(label=f" ", emoji='✅', custom_id="MAINPURSE", style=disnake.ButtonStyle.green, disabled=False, row=2))

class UserCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    @bot.slash_command(description="Узнать свой или чужой баланс")
    @commands.guild_only()
    async def user(self, ctx, user: disnake.User=None):
            if user == None:
                user=ctx.author
                id = user.id
                create(ctx.guild.id, ctx.author.id, 10)
            else:
                user=user
                id = user.id
                user=user
                if user.bot == True:
                    embed=disnake.Embed(description=f"**Причина:**\n> Это бот!",
                    color=check_server_bd(ctx.guild.id)[1], timestamp=datetime.datetime.now())
                    embed.set_author(name='Извините', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
                    embed.set_footer(text=f"{ctx.author}", icon_url=f"{ctx.author.avatar}")
                    return await ctx.response.send_message(embed=embed, ephemeral=True)
            money = check(ctx.guild.id, id, "cash")
            bit1 = check(ctx.guild.id, id, 'bit')
            exp = check(ctx.guild.id, id, 'exp')
            lvl = int(exp) / 100
            prem = check(ctx.guild.id, id, 'prem')
            coin = check(ctx.guild.id, id, 'coin')
            ver = check(ctx.guild.id, id, 'ver')
            pay = check(ctx.guild.id, id, 'pay')
            cris = check(ctx.guild.id, ctx.author.id, "cris")
            if money == None:
                    embed=disnake.Embed(description=f"**Причина:**\n> Этого юзера нету в бд!",
                    color=check_server_bd(ctx.guild.id)[1], timestamp=datetime.datetime.now())
                    embed.set_author(name='Извините', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
                    embed.set_footer(text=f"{ctx.author}", icon_url=f"{ctx.author.avatar}")
                    await ctx.response.send_message(embed=embed, ephemeral=True)
            elif check(ctx.guild.id, id, "show") == 1:
                embed=disnake.Embed(description=f"**Причина:**\n> Этот пользователь закрыл свой профиль",
                color=check_server_bd(ctx.guild.id)[1], timestamp=datetime.datetime.now())
                embed.set_author(name='Извините', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
                embed.set_footer(text=f"{ctx.author}", icon_url=f"{ctx.author.avatar}")
                return await ctx.response.send_message(embed=embed, ephemeral=True)
            else:
                if pay == 1:
                    text="**Этот пользователь выключил переводы на свой аккаунт**"
                elif pay == 0:
                    text=""
                else:
                    text="Не удалось получить данные об юзере"
                dateman = datetime.datetime.strptime(check(ctx.guild.id, id, 'datecre'), "%Y-%m-%d %H:%M:%S.%f")
                await ctx.response.send_message(user, embed=disnake.Embed(description=f"Профиль: {user.mention}\nДата создание аккаунта в базе: {format_dt(dateman)} | [{format_dt(dateman, 'R')}]\n{text}\n\n```cs\nВаше звание: {check(ctx.guild.id, id, 'man')}\n```\nКристалликов: `{cris}`",
                color=check_server_bd(ctx.guild.id)[2]), view=Bal(money, bit1, exp, lvl, prem, coin, ver))

    @commands.has_permissions(administrator=True)
    @bot.slash_command(description="Изменить участника в базе", options=[
        disnake.Option(name="участник", type=disnake.OptionType.user, description="Укажите участника которое хотите изменить", required=True)
        ,disnake.Option(name="значение", description="Укажите значение которые хотите изменить", choices=list(ValueinBd().list.keys()), required=True)
        ,disnake.Option(name="изменить", description="Укажите что хотите сделать",
        choices=["установить", "добавить", "убрать", "умножить", "разделить", "удалить"], required=True)
        ,disnake.Option(name="новое", description="Укажите на что изменить", required=True)])
    @commands.guild_only()
    async def user_change(self, inter, участник, значение, изменить, новое):
        try:
            ex = {"user": f"{участник.id}", "value": f"{значение}", "changed": f"{изменить}", "new": f"{новое}"}
            if значение == 'man':
                if изменить == "удалить": nam = '" "'
                else: nam = f'\'{новое}\''
                sql.execute(f"UPDATE user{inter.guild.id} SET man = {nam} WHERE id = '{участник.id}'")
                db.commit()
                embed= disnake.Embed(title="Участник изменён", color=check_server_bd(inter.guild.id)[2])
                embed.add_field(name=f"{int(участник.id/20090114)}({значение})", value=f"```cs\n{новое}\n```", inline=True)
                await inter.response.send_message(embed=embed)
                return
            else:
                da = изменить
                fa = check(inter.guild.id, inter.author.id, значение)
                fa = int(fa)
                новое = int(новое)
                if da == "установить": new = int(новое)
                elif da == "добавить": new = int(fa + новое)
                elif da == "убрать": new = int(fa - новое)
                elif da == "умножить": new = int(fa * новое)
                elif da == "разделить": new = int(fa / новое)
                elif da == "удалить": new = 0
                if значение:
                    if значение in ["bam", "prem", "pay", "ver", "use", "show"]:
                        if int(new) == 0: pass
                        elif int(new) == 1: pass
                        else:
                            return await inter.response.send_message(embed=disnake.Embed(description="Ошибка!\nВы можете указать только 0 или-же 1", color=check_server_bd(inter.guild.id)[1]), ephemeral=1)
                new = int(new)
                sql.execute(f"UPDATE user{inter.guild.id} SET {значение} = {int(new)} WHERE id = '{участник.id}'")
                db.commit()
                embed= disnake.Embed(title="Участник изменён", color=check_server_bd(inter.guild.id)[2])
                embed.add_field(name=f"{int(участник.id/20090114)}({значение})", value=f"{new:,}", inline=True)
                await inter.response.send_message(embed=embed)
        except Exception as e:
            await inter.response.send_message(f"```py\n{e}\n```")

def setup(bot: commands.Bot):
    bot.add_cog(UserCommand(bot))