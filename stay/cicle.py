import disnake
from disnake.ext import commands
from disnake.utils import *
import sqlite3
import random
import json
import time
import datetime
from eco.func.func import *

bot = commands.InteractionBot()

bd = 'bd.db'

db = sqlite3.connect(bd)
sql = db.cursor()

class Cicle(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: disnake.Message):
        if message.author.discriminator == 0000: return
        elif message.author.bot == True: return
        create_use(message.guild.id, message.author.id)
        if check_server_bd(message.guild.id)[3] == 1:
            if message.content.startswith("b!") == True:
                if check_command(message.guild.id,message.content.replace("b!", "").split(" ")[0].lower()) is not None:
                    check1 = check_user(message.guild.id, message.author.id, "total_commands")
                    add_user(message.guild.id, message.author.id, "total_commands", int(check1)+1)
            else:
                if len(message.content) < 5: return
                elif message.author.bot == True: return
                else: 
                    check1 = check_user(message.guild.id, message.author.id, "messages")
                    add_user(message.guild.id, message.author.id, "messages", int(check1)+1)
        else:
            if len(message.content) < 5: return
            elif message.author.bot == True: return
            else: 
                check1 = check_user(message.guild.id, message.author.id, "messages")
                add_user(message.guild.id, message.author.id, "messages", int(check1)+1)

    @commands.Cog.listener()
    async def on_slash_command_completion(self, inter):
        create_use(inter.guild.id, inter.author.id)
        if inter.author is not None:
            check1 = check_user(inter.guild.id, inter.author.id, "total_commands")
            add_user(inter.guild.id, inter.author.id, "total_commands", int(check1)+1)


    # @bot.slash_command()
    # async def update_bd(self, inter):
    #     for guild in self.bot.guilds:
    #         for channel in guild.channels:
    #             if channel.guild.id == 988347553894514749 or 966808361251270737: pass
    #             else:
    #                 sql.execute(f"ALTER TABLE user{channel.guild.id} ADD COLUMN cris BIGINT")
    #                 sql.execute(f"UPDATE user{channel.guild.id} SET cris = 0")
    #     await inter.response.send_message("Я успешно обновил базу данных экономики")
        

    @bot.slash_command(description="Узнать статистику пользователя")
    async def statis(self, inter, user: disnake.User=None):
        if user == None: user = inter.author
        if user.bot == True:
            embed=disnake.Embed(description=f"**Причина:**\n> Это бот!",
            color=check_server_bd(inter.guild.id)[1], timestamp=datetime.datetime.now())
            embed.set_author(name='Ошибка', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
            embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            return await inter.response.send_message(embed=embed, ephemeral=True)
        create_use(inter.guild.id, inter.author.id)
        one = check_user(inter.guild.id, user.id, "act")
        sec = one % (24 * 3600) 
        hour = sec // 3600 
        sec %= 3600 
        min = sec // 60 
        sec %= 60
        tot = check_user(inter.guild.id, user.id, "messages")
        command = check_user(inter.guild.id, user.id, "total_commands")
        embed=disnake.Embed(title=f"Статистика {user.name} [{user.display_name}]", color=check_server_bd(inter.guild.id)[2])
        embed.add_field(name=f"Активность в голосовых каналах", value=f"{hour} Часов, {min} Минут", inline=True)
        embed.add_field(name=f"Всего сообщений", value=f"{tot}", inline=True)
        embed.add_field(name=f"Всего использовал комманд", value=f"{command}", inline=True)
        await inter.response.send_message(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(Cicle(bot))
