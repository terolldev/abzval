import disnake
from disnake.ext import tasks, commands
import datetime
import os
from eco.func.func import *
intents = disnake.Intents.all()
intents.members = True
bot = commands.Bot("d!", intents=intents)
bot.remove_command('help')
from eco.func.func import *
command=len(bot.slash_commands)

@tasks.loop(minutes=1.0) 
async def voice_check():
    for guilds in bot.guilds:
        for channel in guilds.voice_channels:
            if channel.guild.afk_channel == None: afk_channel = 0
            else: afk_channel = channel.guild.afk_channel.id
            if channel.members and channel.id != afk_channel:
                for member in channel.members:
                    create_use(member.guild.id, member.id)
                    if member.bot == True:return
                    elif member.id == bot.user.id:return
                    elif member.voice.self_mute or member.voice.self_deaf == True:return
                    add_user(member.guild.id, member.id, "act", int(check_user(member.guild.id, member.id, "act")+60))
                    check1=check_user(member.guild.id, member.id, "act")

@tasks.loop(minutes=5.0) 
async def guild_check():
    for guilds in bot.guilds:
        for channel in guilds.text_channels:
            create_bd_cuscom(channel.guild.id)
            createbd(channel.guild.id)
            create_bd(channel.guild.id)
            int_server_bd(channel.guild.id)
            try:
                if check_server_bd(channel.guild.id)[7] == 1:
                    await guilds.leave()
                elif check_server_bd(channel.guild.id)[12] < int(datetime.datetime.now().timestamp()):
                    change_server_bd(channel.guild.id, "prem", 0)
            except:
                return
            
@bot.event
async def on_ready():
    await bot.change_presence(
            activity=disnake.Streaming(
                name=f'XD | :)',
                 url='https://www.twitch.tv/timeigep', twitch_name="discord", game="Minecraft"))
    print(f"[SAPI]: Статус загружен")
    name=bot.user.name
    print(f"[{name}]: Бот запустился")
    voice_check.start()
    guild_check.start()

@bot.command()
async def cd(ctx, command: str):
  if ctx.author.id == 665271319545511939:
      bot.remove_slash_command(command)
      await ctx.reply(f"Команда {command} Выключена")
  else: return

@bot.command()
async def ban_server(ctx, id: int):
    if ctx.author.id == 665271319545511939:
        if check_server_bd(id)[7] == 0:
            change_server_bd(id, "ban", 1)
            text = f"Я забанил сервер под айди: `{id}`"
        elif check_server_bd(id)[7] == 1:
            change_server_bd(id, "ban", 0)
            text = f"Я разбанил сервер под айди: `{id}`"
        await ctx.reply(text)

@bot.command()
async def change(ctx, *, sqll):
    if ctx.author.id == 665271319545511939:
        sql.execute(sqll)
        await ctx.reply("Сделал!")

create_server_bd()
create_bd_user()
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

bot.run("MTA3MTA3NDUwNDkxMjE1NDc0Ng.GOJTcA.6oRuI7bNhk6INEKDrmCixqBWY1AMY82bl5P19E")