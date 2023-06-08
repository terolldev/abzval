from disnake.ext import tasks, commands
from eco.func.func import *
import datetime

@tasks.loop(minutes=5.0) 
async def user_check192(bot: commands.InteractionBot):
    for guild in bot.guilds:
        guild = bot.get_guild(guild.id)
        for user in guild.members:
            data = check_user_bd(user.id)
            if data is not None:
                if data[6] > int(datetime.datetime.now().timestamp()):
                    guild = bot.get_guild(1044340714932293724)
                    member = guild.get_member(user.id)
                    role = guild.get_role(1090242967912075324)
                    if role in member.roles:
                        return
                    await member.add_roles(role, reason="user busting server")
                elif data[6] < int(datetime.datetime.now().timestamp()):
                    guild = bot.get_guild(1044340714932293724)
                    member = guild.get_member(user.id)
                    role = guild.get_role(1090242967912075324)
                    change_user_bd(user.id, "busting", 0)
                    await member.remove_roles(role, reason="user not busting server")
        