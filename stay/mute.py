import disnake
from disnake.ext import commands
from eco.func.func import *
import datetime

bot = commands.InteractionBot()

class Mutecommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.has_permissions(manage_messages=True)
    @bot.slash_command(description="Замьютить пользователя", options=[
        disnake.Option(
            "пользователь", description="Укажите пользователя для мьюта!", type=disnake.OptionType.user, required=True),
        disnake.Option(
            "минуты", description="Укажите на сколько минут замьютить!", type=disnake.OptionType.number, required=True, min_value=1, max_value=40320),
        disnake.Option(
            "причина", description="Укажите причину!", type=disnake.OptionType.string, required=False
        ),],)
    @commands.guild_only()
    async def mute(self, inter, пользователь: disnake.Member, минуты: int, причина=None):
      out_1 = пользователь.current_timeout
      if out_1 == None:
        if пользователь.bot == True:
            embed=disnake.Embed(description="**Причина:**\n> Нельзя указать бота!", color=check_server_bd(inter.guild.id)[1], timestamp=datetime.datetime.now())
            embed.set_author(name='Ошибка', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
            embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.response.send_message(embed=embed, ephemeral=True)
        else:
          minuts = минуты * 60
          if минуты < 60:
            if пользователь == inter.author:
                embed=disnake.Embed(description="**Причина:**\n> Нельзя указать самого себя!", color=check_server_bd(inter.guild.id)[1], timestamp=datetime.datetime.now())
                embed.set_author(name='Ошибка', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
                embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
                await inter.response.send_message(embed=embed, ephemeral=True)
            elif причина == None:
                await пользователь.timeout(duration=minuts, reason=f'Mod: {inter.author}')
                embed=disnake.Embed(title="> 🎉 | Мьют",
                description=f'**Модератор:** {inter.author.mention}\n**Пользователь:** {пользователь.mention}\n**Время:** {int(минуты%60)} минут\n**Причина:** Без причины',
                color=check_server_bd(inter.guild.id)[2], timestamp=datetime.datetime.now())
                embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
                await inter.response.send_message(embed=embed)
                embed=disnake.Embed(title=f'> 🛠️ | Вы были замьючены на сервере: {inter.guild.name}', description=f'**Модератор:** {inter.author.mention}\n**Время:** {int(минуты%60)} минут\n**Причина:** Без причины', color=0x2e2f33)
                await пользователь.send(embed=embed)
            else:
                await пользователь.timeout(duration=minuts, reason=f'{причина} (ID: {inter.author.id})')
                embed=disnake.Embed(title="> 🎉 | Мьют",
                description=f'**Модератор:** {inter.author.mention}\n**Пользователь** {пользователь.mention}\n**Время:**  {int(минуты%60)} минут\n**Причина:** {причина}',
                color=check_server_bd(inter.guild.id)[2], timestamp=datetime.datetime.now())
                embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
                await inter.response.send_message(embed=embed)
                embed=disnake.Embed(title=f'> 🛠️ | Вы были замьючены на сервере: {inter.guild.name}', description=f'**Модератор:** {inter.author.mention}\n**Время:** {int(минуты%60)} минут\n**Причина:** {причина}', color=0x2e2f33)
                await пользователь.send(embed=embed)
          elif минуты > 60:
            if пользователь == inter.author:
                embed=disnake.Embed(description="**Причина:**\n> Нельзя указать самого себя!", color=check_server_bd(inter.guild.id)[2], timestamp=datetime.datetime.now())
                embed.set_author(name='Ошибка', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
                embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
                await inter.response.send_message(embed=embed, ephemeral=True)
            elif причина == None:
                await пользователь.timeout(duration=minuts, reason=f'Mod: {inter.author}')
                embed=disnake.Embed(title="> 🎉 | Мьют",
                description=f'**Модератор:** {inter.author.mention}\n**Пользователь:** {пользователь.mention}\n**Время:** {int(минуты//60)} час {int(минуты%60)} минут\n**Причина:** Без причины',
                color=check_server_bd(inter.guild.id)[2], timestamp=datetime.datetime.now())
                embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
                await inter.response.send_message(embed=embed)
                embed=disnake.Embed(title=f'> 🛠️ | Вы были замьючены на сервере: {inter.guild.name}', description=f'**Модератор:** {inter.author.mention}\n**Время:** {int(минуты//60)} час {int(минуты%60)} минут\n**Причина:** Без причины', color=0x2e2f33)
                await пользователь.send(embed=embed)
            else:
                await пользователь.timeout(duration=minuts, reason=f'{причина} (ID: {inter.author.id})')
                embed=disnake.Embed(title="> 🎉 | Мьют",
                description=f'**Модератор:** {inter.author.mention}\n**Пользователь** {пользователь.mention}\n**Время:** {int(минуты//60)} час {int(минуты%60)} минут\n**Причина:** {причина}',
                color=check_server_bd(inter.guild.id)[2], timestamp=datetime.datetime.now())
                embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
                await inter.response.send_message(embed=embed)
                embed=disnake.Embed(title=f'> 🛠️ | Вы были замьючены на сервере: {inter.guild.name}', description=f'**Модератор:** {inter.author.mention}\n**Время:** {int(минуты//60)} час {int(минуты%60)} минут\n**Причина:** {причина}', color=0x2e2f33)
                await пользователь.send(embed=embed)
      else:
            embed=disnake.Embed(description="**Причина:**\n> Пользователь уже замьючен!", color=check_server_bd(inter.guild.id)[2], timestamp=datetime.datetime.now())
            embed.set_author(name='Ошибка', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
            embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.response.send_message(embed=embed, ephemeral=True)
        
    #un mute
    @commands.has_permissions(manage_messages=True)
    @bot.slash_command(description="Размьютить пользователя", options=[
        disnake.Option(
            "пользователь", description="Укажите пользователя для мьюта!", type=disnake.OptionType.user, required=True),
        disnake.Option(
            "причина", description="Укажите причину!", type=disnake.OptionType.string, required=False
        ),],)
    @commands.guild_only()
    async def unmute(self, inter, пользователь: disnake.Member, причина=None):
        out_1 = пользователь.current_timeout
      
        if out_1 == None:
            embed=disnake.Embed(description="**Причина:**\n> Пользователь не замьючен!", color=0xed4947, timestamp=datetime.datetime.now())
            embed.set_author(name='Ошибка', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
            embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.response.send_message(embed=embed, ephemeral=True)
        elif причина == None:
            await пользователь.timeout(duration=None, reason=f'Mod: {inter.author}')
            embed=disnake.Embed(title="> 🎉 | Размьют",
            description=f'**Модератор:** {inter.author.mention}\n**Пользователь:** {пользователь.mention}\n**Причина:** Без причины',
            color=0x2e2f33, timestamp=datetime.datetime.now())
            embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.response.send_message(embed=embed)
            embed=disnake.Embed(title=f'> 🛠️ | Вы были размьючены на сервере: {inter.guild.name}', description=f'**Модератор:** {inter.author.mention}\n**Причина:** Без причины', color=0x2e2f33)
            await пользователь.send(embed=embed)
        else:
            await пользователь.timeout(duration=None, reason=f'{причина} (ID: {inter.author.id})')
            embed=disnake.Embed(title="> 🎉 | Размьют",
            description=f'**Модератор:** {inter.author.mention}\n**Пользователь** {пользователь.mention}\n**Причина:** {причина}',
            color=0x2e2f33, timestamp=datetime.datetime.now())
            embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.response.send_message(embed=embed)
            embed=disnake.Embed(title=f'> 🛠️ | Вы были размьючены на сервере: {inter.guild.name}', description=f'**Модератор:** {inter.author.mention}\n**Причина:** {причина}', color=0x2e2f33)
            await пользователь.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(Mutecommand(bot))