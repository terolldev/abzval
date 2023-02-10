import disnake
from disnake.ext import commands
from disnake.utils import *
from eco.func.func import *

bot = commands.InteractionBot()

class USer1Command(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @bot.slash_command(description="Посмотреть информацию об вас")
    async def user(self, inter):
        user = check_user_bd(inter.author.id)
        # 1 = prems
        # 2 = ban
        # 3 = mod
        # 4 = tester
        if user == None:
            embed=disnake.Embed(description=f"**Причина:**\n> Вы не добавлены в базу данных\nПеревыполните команду!",
            color=check_server_bd(inter.guild.id)[1], timestamp=datetime.datetime.now())
            embed.set_author(name='Извините', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
            embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.response.send_message(embed=embed, ephemeral=True)
        else:
            embed=disnake.Embed(title="Информация", description=f"`[`{inter.author.mention}`]`", color=check_server_bd(inter.guild.id)[2])
            embed.add_field(name="Кол-во бонусов", value=f"{user[1]}", inline=False)
            embed.add_field(name="Блокировка?", value=f"{bool(user[2])}", inline=True)
            embed.add_field(name="Модератор?", value=f"{bool(user[3])}", inline=True)
            embed.add_field(name="Тестирует функции?", value=f"{bool(user[4])}", inline=True)
            await inter.response.send_message(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(USer1Command(bot))
