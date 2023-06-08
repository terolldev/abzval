from disnake.ext import tasks, commands
from eco.func.func import *

@tasks.loop(minutes=5.0) 
async def guild_check(bot: commands.InteractionBot):
    for guilds in bot.guilds:
        for channel in guilds.text_channels:
            create_bd_cuscom(channel.guild.id)
            createbd(channel.guild.id)
            create_bd(channel.guild.id)
            create_bd_anw(channel.guild.id)
            if check_server_bd(channel.guild.id) is None:int_server_bd(channel.guild.id)
            try:
                if check_server_bd(channel.guild.id)[7] == 1:
                    await guilds.leave()
                elif check_server_bd(channel.guild.id)[12] < int(datetime.datetime.now().timestamp()):
                    change_server_bd(channel.guild.id, "prem", 0)
            except:
                return