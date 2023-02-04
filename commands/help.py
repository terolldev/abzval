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

class HelpCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        com = []
        commandss = self.bot.global_slash_commands
        for comman in commandss:
            com.append(f"{comman.name}")
        file = open("command.json", "w")
        des = "{"
        des1 = "}"
        com = str(com).replace("'", '"')
        file.write(f"{des}\"commands\": {str(com)}{des1}")
        file.close()

    @bot.slash_command(description="Помощь",)
    async def help(self, inter, команда: str=None):
        if команда == None:     
            command = []
            commands = self.bot.global_slash_commands
            for name in commands:
                command.append(f"</{name.name}:{name.id}>")
            text = ", ".join(command)
            embed=disnake.Embed(color=check_server_bd(inter.guild.id)[2], description=text)
            embed.set_footer(text=f"Всего команд: {len(commands)}")
            await inter.response.send_message(embed=embed,ephemeral=1)
        else:
            command = []
            commands = self.bot.global_slash_commands
            for name in commands:
                if name.name == команда:
                    text = f"Название: </{name.name}:{name.id}>\nОписание: {name.description}"
            embed=disnake.Embed(color=check_server_bd(inter.guild.id)[2], description=text)
            await inter.response.send_message(embed=embed,ephemeral=1)

    @help.autocomplete("команда")
    async def language_autocomp(inter: disnake.CommandInteraction, string: str):
        string = string.lower()
        return [lang for lang in json.loads(open("command.json", "r").readlines()[0])['commands'] if string in lang.lower()]

def setup(bot: commands.Bot):
    bot.add_cog(HelpCommand(bot))
