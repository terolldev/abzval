import disnake
from disnake.ext import commands
from eco.func.func import *

class Message():
    async def sendError(inter, text: str):
        embed=disnake.Embed(description=f"**Причина:**\n> {text}",
        color=check_server_bd(inter.guild.id)[1], timestamp=datetime.datetime.now())
        embed.set_author(name='Ошибка', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
        embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
        await inter.response.send_message(embed=embed, ephemeral=True)

    async def sendWarning(inter, text: str):
        embed=disnake.Embed(description=f"**Причина:**\n> {text}",
        color=check_server_bd(inter.guild.id)[1], timestamp=datetime.datetime.now())
        embed.set_author(name='Warning!', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
        embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
        await inter.response.send_message(embed=embed, ephemeral=True)
    
    async def sendDeveloperMessage(inter, text):
        embed=disnake.Embed(title="DEBUG", description=f"{text}", color=0xFF0000)
        await inter.response.send_message(embed=embed)
