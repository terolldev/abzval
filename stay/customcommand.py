import disnake
from disnake.ext import commands
from disnake.utils import *
import sqlite3
from disnake import TextInputStyle
from eco.func.func import *

bd = 'bd.db'
db = sqlite3.connect(bd)
sql = db.cursor()

bot = commands.InteractionBot()

def check1(id: int):
    for val in sql.execute(f"SELECT exp FROM users WHERE id = ?", (id,)):
        return val[0]

class Change(disnake.ui.Modal):
    def __init__(self, name: str, inter):
        components = [
          disnake.ui.TextInput(
              label="Новый ответ",
              placeholder="Укажите новый ответ для команды",
              custom_id="newreply",
              style=TextInputStyle.paragraph,
              min_length=1,
              value=check_command(inter.guild.id, name)[0],
              max_length=250,
              required=True
            ),
        disnake.ui.TextInput(
              label="Новое описание",
              placeholder="Укажите новое описание для команды",
              custom_id="newdesc",
              style=TextInputStyle.short,
              min_length=1,
              value=check_command(inter.guild.id, name)[1],
              max_length=250,
              required=True
            ),
        ]
        super().__init__(
            title="Изменить пользовательскую команду",
            custom_id=name,
            components=components,
        )
    async def callback(self, inter: disnake.ModalInteraction):
        name = self.custom_id
        newreply = inter.text_values['newreply']
        newdesc = inter.text_values['newdesc']
        change_command(inter.guild.id, name, newreply, newdesc)
        embed=disnake.Embed(title=f"Пользовательская команда была изменена!", color=check_server_bd(inter.guild.id)[2])
        embed.add_field(name="Название", value=name, inline=False)
        embed.add_field(name="Новый ответ", value=f"```\n{newreply}\n```", inline=False)
        embed.add_field(name="Новое описание", value=newdesc, inline=False)
        await inter.response.send_message(embed=embed)

class Create(disnake.ui.Modal):
    def __init__(self):
        components = [
            disnake.ui.TextInput(
              label="Название команды",
              placeholder="Укажите название команды",
              custom_id="name",
              style=TextInputStyle.short,
              min_length=1,
              max_length=15,
              required=True
            ),
            disnake.ui.TextInput(
              label="Ответ",
              placeholder="Укажите что должна ответить команда",
              custom_id="reply",
              style=TextInputStyle.paragraph,
              min_length=1,
              max_length=250,
              required=True
            ),
            disnake.ui.TextInput(
              label="Описание",
              placeholder="Укажите описание команды",
              custom_id="description",
              style=TextInputStyle.short,
              min_length=1,
              max_length=50,
              required=True
            )
        ]
        super().__init__(
            title="Создание пользовательской команды",
            custom_id="create_command",
            components=components,
        )
    async def callback(self, inter: disnake.ModalInteraction):
        name = inter.text_values['name']
        reply = inter.text_values['reply']
        description=inter.text_values['description']
        if check_command(inter.guild.id, name) is not None:
            embed=disnake.Embed(description=f"**Причина:**\n> Команда с таким именем уже создана!",
            color=check_server_bd(inter.guild.id)[1], timestamp=datetime.datetime.now())
            embed.set_author(name='Ошибка', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
            embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.response.send_message(embed=embed, ephemeral=True)
        elif name == "help":
            embed=disnake.Embed(description=f"**Причина:**\n> Команду с таким именем нельзя создать!",
            color=check_server_bd(inter.guild.id)[1], timestamp=datetime.datetime.now())
            embed.set_author(name='Ошибка', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
            embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.response.send_message(embed=embed, ephemeral=True)
        else:
            create_command(inter.guild.id, name, reply, description)
            embed=disnake.Embed(title=f"Пользовательская команда создана!", color=check_server_bd(inter.guild.id)[2])
            embed.add_field(name="Название", value=name, inline=False)
            embed.add_field(name="Ответ", value=f"```\n{reply}\n```", inline=False)
            embed.add_field(name="Описание", value=description, inline=False)
            await inter.response.send_message(embed=embed)

class CustomCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.has_permissions(administrator = True)
    @bot.slash_command(description="Система Пользовательских команд")
    async def command(self, inter):
        pass

    @command.sub_command(description="Создать пользовательскую команду")
    async def create(self, inter):
        if check_server_bd(inter.guild.id)[3] == 0:
            embed=disnake.Embed(description=f"**Причина:**\n> Пользовательские команды отключены на этом сервере",
            color=check_server_bd(inter.guild.id)[1], timestamp=datetime.datetime.now())
            embed.set_author(name='Ошибка', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
            embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.response.send_message(embed=embed, ephemeral=True)
        else:
            sql.execute(f"SELECT * FROM cuscom{inter.guild.id}")
            if len(sql.fetchall()) > 25:
                embed=disnake.Embed(description=f"**Причина:**\n> Вы создали больше 25 команд!",
                color=check_server_bd(inter.guild.id)[1], timestamp=datetime.datetime.now())
                embed.set_author(name='Упс... Лимит :)', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
                embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
                await inter.response.send_message(embed=embed, ephemeral=True)
            else:
                await inter.response.send_modal(Create())

    @command.sub_command(description="Изменить пользовательскую команду")
    async def change(self, inter, name: str):
        if check_server_bd(inter.guild.id)[3] == 0:
            embed=disnake.Embed(description=f"**Причина:**\n> Пользовательские команды отключены на этом сервере",
            color=check_server_bd(inter.guild.id)[1], timestamp=datetime.datetime.now())
            embed.set_author(name='Ошибка', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
            embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.response.send_message(embed=embed, ephemeral=True)
        else:
            if check_command(inter.guild.id, name) is None:
                embed=disnake.Embed(description=f"**Причина:**\n> Команды с таким именем не найдено!",
                color=check_server_bd(inter.guild.id)[1], timestamp=datetime.datetime.now())
                embed.set_author(name='Ошибка', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
                embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
                await inter.response.send_message(embed=embed, ephemeral=True)
            else:
                await inter.response.send_modal(Change(name, inter))

    @command.sub_command(description="Удалить пользовательскую команду")
    async def delete(self, inter, name: str):
        if check_server_bd(inter.guild.id)[3] == 0:
            embed=disnake.Embed(description=f"**Причина:**\n> Пользовательские команды отключены на этом сервере",
            color=check_server_bd(inter.guild.id)[1], timestamp=datetime.datetime.now())
            embed.set_author(name='Ошибка', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
            embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.response.send_message(embed=embed, ephemeral=True)
        else:
            if check_command(inter.guild.id, name) is not None:
                delete_command(inter.guild.id, name)
                embed=disnake.Embed(title=f"Пользовательская команда была удалена!", color=check_server_bd(inter.guild.id)[2])
                embed.add_field(name="Название", value=name, inline=False)
                await inter.response.send_message(embed=embed)
            else:
                embed=disnake.Embed(description=f"**Причина:**\n> Команды с таким именем не найдено!",
                color=check_server_bd(inter.guild.id)[1], timestamp=datetime.datetime.now())
                embed.set_author(name='Ошибка', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
                embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
                await inter.response.send_message(embed=embed, ephemeral=True)

def setup(bot: commands.Bot):
    bot.add_cog(CustomCommand(bot))