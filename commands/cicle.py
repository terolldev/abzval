import disnake
from disnake.ext import commands
from disnake.utils import *
import sqlite3
from bot.error import *
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
            return await Message.sendError(inter, "Это бот!")
        elif check_user(inter.guild.id, user.id, "act") == None:
            return await Message.sendError(inter, "Этот пользователь нечего не делал на сервере")
        create_use(inter.guild.id, inter.author.id)
        one = check_user(inter.guild.id, user.id, "act")
        sec = one % (24 * 3600) 
        hour = sec // 3600
        sec %= 3600 
        min = sec // 60 
        sec %= 60
        texta = f"{min} Минут"
        if one > 86400:
            texta = f"{int(one/3600/24)} Дней, {hour} Часов, {min} Минут"
        elif one > 3600:
            texta = f"{hour} Часов, {min} Минут"
        tot = check_user(inter.guild.id, user.id, "messages")
        command = check_user(inter.guild.id, user.id, "total_commands")
        embed=disnake.Embed(title=f"Статистика {user.name} [{user.display_name}]", color=check_server_bd(inter.guild.id)[2])
        embed.add_field(name=f"Активность в голосовых каналах", value=f"{texta}", inline=True)
        embed.add_field(name=f"Всего сообщений", value=f"{tot}", inline=True)
        embed.add_field(name=f"Всего использовал команд", value=f"{command}", inline=True)
        await inter.response.send_message(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(Cicle(bot))
