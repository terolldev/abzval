import disnake
from disnake import TextInputStyle
from disnake.ext import commands
import random
import sqlite3
from disnake.utils import *
from eco.func.func import *

bot = commands.InteractionBot()

bd = 'bd.db'

db = sqlite3.connect(bd)
sql = db.cursor()

class ModCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.has_permissions(administrator=True)
    @bot.slash_command(description="Обнулить,Удалить,Создать юзера", options=[
        disnake.Option(name="user", required=True, type=disnake.OptionType.user),
        disnake.Option(name="action", required=True, type=disnake.OptionType.string, choices=["Создать", "Удалить", "Обнулить"])
    ])
    async def user_mod(self, inter, user: disnake.User, action):
        if user.id == 1:
            embed=disnake.Embed(description=f"**Причина:**\n> Нельзя указать самого себя",
            color=check_server_bd(inter.guild.id)[1], timestamp=datetime.datetime.now())
            embed.set_author(name='Извините', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
            embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.response.send_message(embed=embed, ephemeral=True)
        else:
            if action == "Создать":
                create(inter.guild.id, user.id, 10)
                embed=disnake.Embed(description=f"Я создал юзера {user.mention}", color=check_server_bd(inter.guild.id)[2])
            elif action == "Удалить":
                if check(inter.guild.id, user.id, "cash") is None:
                    embed=disnake.Embed(description=f"Юзера {user.mention} нету в базе", color=check_server_bd(inter.guild.id)[2])
                else:
                    sql.execute(f"DELETE FROM user{inter.guild.id} WHERE id = ?", (user.id,))
                    db.commit()
                    embed=disnake.Embed(description=f"Я удалил юзера {user.mention}", color=check_server_bd(inter.guild.id)[2])
            elif action == "Обнулить":
                if check(inter.guild.id, user.id, "cash") is None:
                    embed=disnake.Embed(description=f"Юзера {user.mention} нету в базе", color=check_server_bd(inter.guild.id)[2])
                else:
                    sql.execute(f"UPDATE user{inter.guild.id} SET cash = {0} WHERE id = '{user.id}'")
                    sql.execute(f"UPDATE user{inter.guild.id} SET bit = {0} WHERE id = '{user.id}'")
                    sql.execute(f"UPDATE user{inter.guild.id} SET coin = {0} WHERE id = '{user.id}'")
                    sql.execute(f"UPDATE user{inter.guild.id} SET prem = {0} WHERE id = '{user.id}'")
                    sql.execute(f"UPDATE user{inter.guild.id} SET bitmine = {0} WHERE id = '{user.id}'")
                    sql.execute(f"UPDATE user{inter.guild.id} SET exp = {0} WHERE id = '{user.id}'")
                    db.commit()
                    embed=disnake.Embed(description=f"Обнулил юзера {user.mention}", color=check_server_bd(inter.guild.id)[2])
        await inter.response.send_message(embed=embed)
                    


def setup(bot: commands.Bot):
    bot.add_cog(ModCommand(bot))