from disnake.ext import commands
import os
def load_ext(bot: commands.InteractionBot):
    for filename in os.listdir("./commands"):
        if filename.endswith(".py"):
            print(f"[DEBUG]: {filename[:-3]} load")
            bot.load_extension(f"commands.{filename[:-3]}")
    for filename in os.listdir("./eco"):
        if filename.endswith(".py"):
            print(f"[DEBUG]: {filename[:-3]} load")
            bot.load_extension(f"eco.{filename[:-3]}")
    for filename in os.listdir("./fun"):
        if filename.endswith(".py"):
            print(f"[DEBUG]: {filename[:-3]} load")
            bot.load_extension(f"fun.{filename[:-3]}")