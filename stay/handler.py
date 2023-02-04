import disnake
from disnake.ext import commands
from disnake.utils import *
from disnake.errors import *
from disnake.ext.commands import *
from disnake.client import *
import datetime
from eco.func.func import *

class Handler(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_slash_command_error(cog, interaction, error):
        create_bd_cuscom(interaction.guild.id)
        createbd(interaction.guild.id)
        create_bd(interaction.guild.id)
        if isinstance (error, MissingPermissions):
            embed=disnake.Embed(description=f"**Причина:**\n> У вас недостаточно прав для этого действия",
            color=check_server_bd(interaction.guild.id)[1], timestamp=datetime.datetime.now())
            embed.set_author(name='Ошибка', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
            embed.set_footer(text=f"{interaction.author}", icon_url=f"{interaction.author.avatar}")
            await interaction.response.send_message(embed=embed, ephemeral=True)
        if isinstance (error, InteractionResponded):
            embed=disnake.Embed(description=f"**Причина:**\n> Подробнее:\n{error}", color=check_server_bd(interaction.guild.id)[1], timestamp=datetime.datetime.now())
            embed.set_author(name='Упс...', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
            await interaction.followup.send(embed=embed)
        if isinstance (error, commands.CommandRegistrationError):
            embed=disnake.Embed(description=f"**Причина:**\n> Мне не удалось создать слеш команду, повторите попытку позже.\nЕсли проблема не исчезнет напишите разработчикам",
            color=check_server_bd(interaction.guild.id)[1], timestamp=datetime.datetime.now())
            embed.set_author(name='Ошибка', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
            embed.set_footer(text=f"{interaction.author}", icon_url=f"{interaction.author.avatar}")
            await interaction.response.send_message(embed=embed, ephemeral=True)
        if isinstance (error, commands.DisabledCommand):
            embed=disnake.Embed(description=f"**Причина:**\n> Разработчик выключил данную команду.",
            color=check_server_bd(interaction.guild.id)[1], timestamp=datetime.datetime.now())
            embed.set_author(name='Извините', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
            embed.set_footer(text=f"{interaction.author}", icon_url=f"{interaction.author.avatar}")
            await interaction.response.send_message(embed=embed, ephemeral=True)
        if isinstance (error, commands.PrivateMessageOnly):
            embed=disnake.Embed(description=f"**Причина:**\n> Данная команда доступна только в [личных сообщениях](https://discord.com/channels/@me)",
            color=check_server_bd(interaction.guild.id)[1], timestamp=datetime.datetime.now())
            embed.set_author(name='Извините', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
            embed.set_footer(text=f"{interaction.author}", icon_url=f"{interaction.author.avatar}")
            await interaction.response.send_message(embed=embed, ephemeral=True)
        if isinstance(error, commands.CommandOnCooldown):
            times = round(error.retry_after, 2)
            if times < 60:
                embed=disnake.Embed(description=f"**Причина:**\n> Подождите: {int(times / 1)} секунд",
                color=check_server_bd(interaction.guild.id)[1], timestamp=datetime.datetime.now())
                embed.set_author(name='Ошибка', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
                embed.set_footer(text=f"{interaction.author}", icon_url=f"{interaction.author.avatar}")
            elif times > 60:
                embed=disnake.Embed(description=f"**Причина:**\n> Подождите: \n# {int(times/60)} минут {int(times%60)} секунд",
                color=check_server_bd(interaction.guild.id)[1], timestamp=datetime.datetime.now())
                embed.set_author(name='Ошибка', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
                embed.set_footer(text=f"{interaction.author}", icon_url=f"{interaction.author.avatar}")
            return await interaction.response.send_message(embed=embed, ephemeral=True)
        if isinstance (error, commands.EmojiNotFound):
            embed=disnake.Embed(description=f"**Причина:**\n> Эмоджи не найдено, укажите правильно", color=check_server_bd(interaction.guild.id)[1], timestamp=datetime.datetime.now())
            embed.set_author(name='Ошибка', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
            embed.set_footer(text=f"{interaction.author}", icon_url=f"{interaction.author.avatar}")
            await interaction.response.send_message(embed=embed, ephemeral=True)
            await interaction.followup.send(embed=embed)
        if isinstance (error, Forbidden):
            embed=disnake.Embed(description="**Причина:**\n> У меня недостаточно прав", color=check_server_bd(interaction.guild.id)[1], timestamp=datetime.datetime.now())
            embed.set_author(name='Ошибка', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
            embed.set_footer(text=f"{interaction.author}", icon_url=f"{interaction.author.avatar}")
            await interaction.response.send_message(embed=embed, ephemeral=True)
        else:
            ser = 'This command cannot be used in private messages.'
            cor = 'Command raised an exception: ExtensionNotLoaded: Extension '
            oq = "Command raised an exception: TypeError: int() argument must be a string, a bytes-like object or a real number, not 'NoneType'"
            ooq = "Command raised an exception: Forbidden: 403 Forbidden (error code: 50013): Missing Permissions"
            em = "Command raised an exception: OperationalError: no such table: atrib"
            wow = "Command raised an exception: OperationalError: no such table: cuscom"
            bit = "Command raised an exception: NameError: name 'price' is not defined"
            com = "Command raised an exception: UnboundLocalError: local variable 'text' referenced before assignment"
            if ser in str(error):
                embed=disnake.Embed(description="**Причина:**\n> Данная команда доступна только на серверах", color=check_server_bd(interaction.guild.id)[1], timestamp=datetime.datetime.now())
                embed.set_author(name='Извините', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
                await interaction.response.send_message(embed=embed, ephemeral=True)
            elif cor in str(error):
                embed=disnake.Embed(description=f"**Причина:**\n> Такого модуля не существует",
                color=check_server_bd(interaction.guild.id)[1], timestamp=datetime.datetime.now())
                embed.set_author(name='Извините', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
                embed.set_footer(text=f"{interaction.author}", icon_url=f"{interaction.author.avatar}")
                await interaction.response.send_message(embed=embed, ephemeral=True)
            elif wow in str(error):
                embed=disnake.Embed(description=f"**Причина:**\n> База пользовательских команд ещё не была создана, используйте команду ещё раз",
                color=check_server_bd(interaction.guild.id)[1], timestamp=datetime.datetime.now())
                embed.set_author(name='Извините', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
                embed.set_footer(text=f"{interaction.author}", icon_url=f"{interaction.author.avatar}")
                await interaction.response.send_message(embed=embed, ephemeral=True)
            elif oq in str(error):
                embed=disnake.Embed(description=f"**Причина:**\n> Ошибка в базе данных! Обьект не найден!",
                color=check_server_bd(interaction.guild.id)[1], timestamp=datetime.datetime.now())
                embed.set_author(name='Извините', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
                embed.set_footer(text=f"{interaction.author}", icon_url=f"{interaction.author.avatar}")
                await interaction.response.send_message(embed=embed, ephemeral=True)
            elif ooq in str(error):
                embed=disnake.Embed(description=f"**Причина:**\n> У меня недостаточно прав",
                color=check_server_bd(interaction.guild.id)[1], timestamp=datetime.datetime.now())
                embed.set_author(name='Извините', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
                embed.set_footer(text=f"{interaction.author}", icon_url=f"{interaction.author.avatar}")
                await interaction.response.send_message(embed=embed, ephemeral=True)
            elif em in str(error):
                embed=disnake.Embed(description=f"**Причина:**\n> База с сервером ещё не была создана, используйте команду ещё раз",
                color=check_server_bd(interaction.guild.id)[1], timestamp=datetime.datetime.now())
                embed.set_author(name='Извините', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
                embed.set_footer(text=f"{interaction.author}", icon_url=f"{interaction.author.avatar}")
                await interaction.response.send_message(embed=embed, ephemeral=True)
            elif bit in str(error):
                embed=disnake.Embed(description=f"**Причина:**\n> Курс бит-коина ещё не загрузился, используйте команду ещё раз",
                color=check_server_bd(interaction.guild.id)[1], timestamp=datetime.datetime.now())
                embed.set_author(name='Извините', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
                embed.set_footer(text=f"{interaction.author}", icon_url=f"{interaction.author.avatar}")
                await interaction.response.send_message(embed=embed, ephemeral=True)
            elif com in str(error):
                embed=disnake.Embed(description=f"**Причина:**\n> Search object has not find.\n pls write normal command name or and object name",
                color=check_server_bd(interaction.guild.id)[1], timestamp=datetime.datetime.now())
                embed.set_author(name='Извините', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
                embed.set_footer(text=f"{interaction.author}", icon_url=f"{interaction.author.avatar}")
                await interaction.response.send_message(embed=embed, ephemeral=True)
            else:
                embed=disnake.Embed(description=f"**Причина:**\n> Подробнее:\n{error}", color=check_server_bd(interaction.guild.id)[1], timestamp=datetime.datetime.now())
                embed.set_author(name='Упс...', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
                #await interaction.followup.send(embed=embed)
                await interaction.response.send_message(embed=embed, ephemeral=True)
        interaction.application_command.reset_cooldown(interaction) 
    @commands.Cog.listener()
    async def on_command_error(cog, ctx, error):
        if ctx.author.id == 665271319545511939: await ctx.reply(error)
        else: return

def setup(bot: commands.Bot):
    bot.add_cog(Handler(bot))