import disnake
from disnake.ext import commands
from disnake.utils import *
from eco.func.func import *
import requests
import json

bot = commands.InteractionBot()

class NeirosenyaCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @bot.slash_command(name="нейросеня", description="Сделать запрос в нейросеню")
    async def neirosenya(self, inter, text: str):
        await inter.response.defer(ephemeral=True)
        embed=disnake.Embed(title="Нейро-Сеня (build >> 1.0.5)", color=check_server_bd(inter.guild.id)[2])
        url = requests.get(f"http://localhost:8080")
        ps = json.loads(url.content)
        embed.add_field(name="Нейросеть ответила", value=f"{ps['text']}", inline=False)
        await inter.followup.send(embed=embed)
        

def setup(bot: commands.Bot):
    bot.add_cog(NeirosenyaCommand(bot))
