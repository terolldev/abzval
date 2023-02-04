import disnake
from disnake.ext import tasks, commands
import datetime
import os
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
            except:
                return
            
@bot.event
async def on_ready():
    await bot.change_presence(
            activity=disnake.Streaming(
                name=f'',
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

@bot.slash_command(guild_ids=[1044340714932293724], options=[disnake.Option('команда', choices=os.listdir('commands.'),
 type=disnake.OptionType.string, required=True)])
async def reload(ctx, команда):
      if ctx.author.id == 665271319545511939:
        bot.unload_extension(f'commands.{команда[:-3]}')
        bot.load_extension(f"commands.{команда[:-3]}")
        await ctx.response.send_message(f"Модуль {команда} Перезагружен", ephemeral=True)
      else:
        embed=disnake.Embed(description=f"**Причина:**\n>Вы не разработчик ",
        color=0xed4947, timestamp=datetime.datetime.now())
        embed.set_author(name='Извините', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
        embed.set_footer(text=f"{ctx.author}", icon_url=f"{ctx.author.avatar}")
        await ctx.response.send_message(embed=embed, ephemeral=True)

create_server_bd()
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