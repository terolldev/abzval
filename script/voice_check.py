from disnake.ext import tasks, commands
from eco.func.func import *

@tasks.loop(minutes=1.0) 
async def voice_check(bot: commands.InteractionBot):
    for guilds in bot.guilds:
        for channel in guilds.voice_channels:
            if channel.guild.afk_channel == None: afk_channel = 0
            else: afk_channel = channel.guild.afk_channel.id
            if channel.members and channel.id != afk_channel:
                for member in channel.members:
                    create_use(member.guild.id, member.id)
                    if member.bot == True:return
                    elif member.id == bot.user.id:return
                    elif member.voice.self_mute or member.voice.self_deaf or len(member.voice.channel.members) < 2 == True:return
                    add_user(member.guild.id, member.id, "act", int(check_user(member.guild.id, member.id, "act")+60))