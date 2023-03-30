from disnake.ext import tasks, commands
from eco.func.func import *

@tasks.loop(minutes=1)
async def voice_check(bot):
    for guild in bot.guilds:
        guild = bot.get_guild(guild.id)
        for channel in guild.voice_channels:
            for member in channel.members:
                if not (member.bot or member.voice.self_mute or member.voice.self_deaf):
                    create_use(member.guild.id, member.id)
                    add_user(member.guild.id, member.id, "act", int(check_user(member.guild.id, member.id, "act")+60))