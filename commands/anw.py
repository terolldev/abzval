import disnake
from disnake.ext import commands
from eco.func.func import *

bot = commands.InteractionBot()

bd = 'bd.db'

db = sqlite3.connect(bd)
sql = db.cursor()

class Val1(disnake.ui.Modal):
    def __init__(self, fors: str, count: int, forg: str, countg: int):
        components = [
            disnake.ui.TextInput(
              label="Текст",
              placeholder="Ведите Название",
              custom_id="name",
              style=disnake.TextInputStyle.short,
              min_length=3,
              max_length=15,
              required=True
            ),
            disnake.ui.TextInput(
              label="Текст",
              placeholder="Ведите описание",
              custom_id="des",
              style=disnake.TextInputStyle.short,
              min_length=1,
              max_length=35,
              required=True
            )
        ]
        super().__init__(
            title="Название & Описание",
            custom_id="nameanddes",
            components=components,
        )
        self.fors = fors
        self.count = count
        self.forg = forg
        self.countg = countg
    async def callback(self, inter: disnake.ModalInteraction):
        if check_anw(inter.guild.id, f"{inter.text_values['name']}") is None:
            create_anw(inter.guild.id, inter.text_values['name'], inter.text_values['des'], self.fors, self.count, self.forg, self.countg)
            embed = disnake.Embed(title=f"Достижение {inter.text_values['name']} создано!", color=check_server_bd(inter.guild.id)[2])
            await inter.response.send_message(embed=embed)
        else:
            embed=disnake.Embed(description=f"**Причина:**\n> Достижение с таким именем уже есть",
            color=check_server_bd(inter.guild.id)[1], timestamp=datetime.datetime.now())
            embed.set_author(name='Извините', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
            embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.response.send_message(embed=embed, ephemeral=True)

class ChangeAnw(disnake.ui.Modal):
    def __init__(self, ids: int, name: str):
        components = [
            disnake.ui.TextInput(
              label="Описание",
              placeholder="Ведите описание",
              custom_id="des",
              style=disnake.TextInputStyle.short,
              min_length=1,
              max_length=35,
              required=True,
              value=check_anw(ids, name)[1]
            ),
            disnake.ui.TextInput(
              label="Сколко",
              placeholder="Ведите сколько хотите выдавать",
              custom_id="skolca",
              style=disnake.TextInputStyle.short,
              min_length=1,
              max_length=9,
              required=True,
              value=check_anw(ids, name)[5]
            ),
            disnake.ui.TextInput(
              label="За сколько",
              placeholder="Ведите за сколько хотите выдавать",
              custom_id="skolka",
              style=disnake.TextInputStyle.short,
              min_length=1,
              max_length=9,
              required=True,
              value=check_anw(ids, name)[5]
            )
        ]
        super().__init__(
            title="Изменить достижение(выбор будет потом)",
            custom_id="changeanw",
            components=components,
        )
        self.name = name
    async def callback(self, inter: disnake.ModalInteraction):
        embed=disnake.Embed(title="Изменение достижение", color=check_server_bd(inter.guild.id)[2],
        description=f"Название: **{self.name}**\nОписание: **{inter.text_values['des']}**\nПодробнее: Выдать **`Не указано`** в размере **`{inter.text_values['skolca']}`**, за **`Не указано`**, в размере **`{inter.text_values['skolka']}`**")
        await inter.response.send_message(embed=embed, view=cHANGE(inter))
class cHANGE(disnake.ui.View):
    def __init__(self, inter: disnake.ModalInteraction):
        super().__init__(timeout=60)

    @disnake.ui.string_select(placeholder="Укажите за что хотите выдавать",
    max_values=1, options=[disnake.SelectOption(label="messages", description="Общее кол-во сообщений"), 
                           disnake.SelectOption(label="total_commands", description="Общее кол-во использование команд"),
                           disnake.SelectOption(label="voice_activity", description="Общее кол-во времени в войсе")])
    async def zachto(self, value: disnake.ui.StringSelect, inter: disnake.MessageInteraction): await inter.response.send_message(ephemeral=True, content=value.values)

    @disnake.ui.string_select(placeholder="Укажите что хотите выдавать",
    max_values=1, options=[disnake.SelectOption(label="cash", description=ValueinBd().list['cash']), 
                           disnake.SelectOption(label="bit", description=ValueinBd().list['bit']),
                           disnake.SelectOption(label="coin", description=ValueinBd().list['coin']),
                           disnake.SelectOption(label="cris", description=ValueinBd().list['cris']),
                           disnake.SelectOption(label="exp", description=ValueinBd().list['exp']),
                           disnake.SelectOption(label="prem", description=ValueinBd().list['prem'])])
    async def chto(self, value: disnake.ui.StringSelect, inter: disnake.MessageInteraction): await inter.response.send_message(ephemeral=True, content=value.values)
    
class AnwCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @bot.slash_command(description="Система получение наград")
    async def anw(self, inter):pass

    @anw.sub_command()
    async def check(self, inter):
        embed=disnake.Embed(title="Все награды для участников", color=check_server_bd(inter.guild.id)[2])
        sql.execute(f"SELECT * FROM anw{inter.guild.id}")
        for anw in sql.fetchall():
            name = anw[0]
            description = anw[1]
            zachto = anw[2].replace("messages","Сообщения").replace("voice_activity", "Времени в войсе").replace("total_commands", "Команд")
            skolco = anw[3]
            chto = anw[4]
            slolko = anw[5]
            embed.add_field(name=f"{name}", value=f"`{slolko} {chto}` за `{skolco} {zachto}`\n{description}", inline=False)
        await inter.response.send_message(embed=embed)

    @anw.sub_command(description="Создать достижение для участников",
    options=[
        disnake.Option("за_что", description="За что выдавать", choices=[
        "voice_activity", "messages", "total_commands"], required=True),
        disnake.Option("кол_во", description="Количество", type=disnake.OptionType.integer, required=True),
        disnake.Option("что", description="Укажите что выдать", choices=[
        "cash", "bit", "prem", "cris", "coin", "exp"], required=True),
        disnake.Option("количетво", description="Количство выдачи", type=disnake.OptionType.integer, required=True)])
    async def create(self, inter, за_что: str, кол_во: int, что: str, количетво: int):
        if что == "prem":
            if кол_во > 1:
                embed=disnake.Embed(description=f"**Причина:**\n> Укажите число 1 или 0",
                color=check_server_bd(inter.guild.id)[1], timestamp=datetime.datetime.now())
                embed.set_author(name='Извините', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
                embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
                await inter.response.send_message(embed=embed, ephemeral=True)
        await inter.response.send_modal(Val1(за_что, кол_во, что, количетво))

    @anw.sub_command(description="Удалить достижение для участников")
    async def delete(self, inter, name: str):
        print(check_anw(inter.guild.id, name))
        if check_anw(inter.guild.id, name) is None:
            embed=disnake.Embed(description=f"**Причина:**\n> Достижение с таким именем не существует",
            color=check_server_bd(inter.guild.id)[1], timestamp=datetime.datetime.now())
            embed.set_author(name='Извините', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
            embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.response.send_message(embed=embed, ephemeral=True)
        else:
            delete_anw(inter.guild.id, name)
            embed=disnake.Embed(title=f"Достижение {name} удалено", description="Вы удалили достижение", color=check_server_bd(inter.guild.id)[1])
            await inter.response.send_message(embed=embed)

    @anw.sub_command(description="Имзенить достижение")
    async def change(self, inter, name):
        if check_anw(inter.guild.id, name) is None:
            embed=disnake.Embed(description=f"**Причина:**\n> Достижение с таким именем не существует",
            color=check_server_bd(inter.guild.id)[1], timestamp=datetime.datetime.now())
            embed.set_author(name='Извините', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
            embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.response.send_message(embed=embed, ephemeral=True)
        else:
            await inter.response.send_modal(ChangeAnw(inter.guild.id, name))

def setup(bot: commands.Bot):
    bot.add_cog(AnwCommand(bot))