import disnake
from disnake.ext import commands
from disnake.utils import *
from eco.func.func import *

bot = commands.InteractionBot()

class BonusCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @bot.slash_command()
    async def bonus(self, inter):
        pass

    @bonus.sub_command(description="Проверить наличие бонусов")
    async def check(self, inter):
        embed=disnake.Embed(title=f"Бонусы на сервере {inter.guild.name}", color=check_server_bd(inter.guild.id)[2])
        if check_server_bd(inter.guild.id)[5] == 0:
            embed.description="`Бонусов на сервере не найдено!`\nЕсли вы их активировали то подождите около 5 минут"
        elif check_server_bd(inter.guild.id)[5] == 1:
            embed.description=f"Бонусы на сервере пропадут <t:{check_server_bd(inter.guild.id)[12]}:R>"
        await inter.response.send_message(embed=embed)

    @bonus.sub_command(description="Выдать бонус на сервере")
    async def give(self, inter):
        if check_user_bd(inter.author.id)[1] < 1:
            embed=disnake.Embed(description=f"**Причина:**\n> У вас нету бонусов!",
            color=check_server_bd(inter.guild.id)[1], timestamp=datetime.datetime.now())
            embed.set_author(name='Извините', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
            embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.response.send_message(embed=embed, ephemeral=True)
        else:
            if check_server_bd(inter.guild.id)[12] == 0:
                dateman = int(datetime.datetime.now().timestamp()+2592000)
            else:
                dateman = int(check_server_bd(inter.guild.id)[12]+2592000)
            change_server_bd(inter.guild.id, "enddate", dateman)
            change_user_bd(inter.author.id, "prems", int(check_user_bd(inter.author.id)[1]-1))
            change_server_bd(inter.guild.id, "prem", 1)
            embed=disnake.Embed(title=f"Вы выдали бонус на сервер [{inter.guild.name}]", 
            description=f"Он пропадёт <t:{dateman}:R>", color=check_server_bd(inter.guild.id)[2])
            await inter.response.send_message(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(BonusCommand(bot))
