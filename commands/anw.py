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

class AnwCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @bot.slash_command(description="Система получение наград")
    async def anw(self, inter):pass

    @anw.sub_command()
    async def check(self, inter):
        embed=disnake.Embed(title="Все награды для участников", color=check_server_bd(inter.guild.id)[2])
        sql.execute(f"SELECT * FROM anw{inter.guild.id}")
        if sql.fetchall() is None:
            embed.description = "На сервере ещё нету ни одного достижение"
        else:
            embed.description=f"{sql.fetchall()}"
            await inter.response.send_message(embed=embed)
            # for anw in sql.fetchall():
            #     embed.add_field(name=f"{anw}", value=f"", inline=False)

    @anw.sub_command(description="Создать достижение для участников",
    options=[
        disnake.Option("за_что", description="За что выдавать", choices=[
        "voice_activity", "messages", "total_commands"], required=True),
        disnake.Option("кол_во", description="Количество", type=disnake.OptionType.integer, required=True),
        disnake.Option("что", description="Укажите что выдать", choices=[
        "cash", "bit", "prem", "cris", "coin", "exp"], required=True),
        disnake.Option("количетво", description="Количство выдачи", type=disnake.OptionType.integer, required=True)])
    async def create(self, inter, за_что: str, кол_во: int, что: str, количетво: int):
        await inter.response.send_modal(Val1(за_что, кол_во, что, количетво))

def setup(bot: commands.Bot):
    bot.add_cog(AnwCommand(bot))