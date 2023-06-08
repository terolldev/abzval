import disnake
from disnake.ext import commands
from disnake.utils import *
from eco.func.func import *
from bot.error import *

bot = commands.InteractionBot()

class UserUI(disnake.ui.View):
    def __init__(self, user: list):
        super().__init__()
        if user[3] == 1:
            self.add_item(disnake.ui.Button(label=None, custom_id="dev", emoji="<:dev:1076038119893237801>", style=disnake.ButtonStyle.gray, disabled=False))
            # if user[4]:
            #     self.add_item(disnake.ui.Button(label=None, custom_id="mod", emoji="<:mod:1076038124041408557>", style=disnake.ButtonStyle.gray, disabled=False))
        if user[4] == 1:
            self.add_item(disnake.ui.Button(label=None, custom_id="mod", emoji="<:mod:1076038124041408557>", style=disnake.ButtonStyle.gray, disabled=False))

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
            await Message.sendError(inter, "Вы не добавлены в базу данных\nПеревыполните команду!")
        else:
            embed=disnake.Embed(title=f"Информация", description=f"`[`{inter.author.mention}`]`", color=check_server_bd(inter.guild.id)[2])
            embed.add_field(name="Кол-во бонусов", value=f"{user[1]}", inline=False)
            await inter.response.send_message(f"{inter.author}", embed=embed, view=UserUI(user))


def setup(bot: commands.Bot):
    bot.add_cog(USer1Command(bot))
