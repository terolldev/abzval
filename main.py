import disnake
from disnake.ext import tasks, commands
from eco.func.func import *
from script.guild_check import guild_check
from script.voice_check import voice_check
from script.load_ext import load_ext
from script.user_check import user_check192


intents = disnake.Intents.all()
intents.members = True
intents.reactions = True
intents.emojis = True
bot = commands.Bot("d!", intents=intents)
bot.remove_command('help')
from eco.func.func import *
command=len(bot.slash_commands)

            
@bot.event
async def on_ready():
    await bot.change_presence(
            activity=disnake.Streaming(
                name=f'XD | :)',
                 url='https://www.twitch.tv/tim_eiger', twitch_name="discord", game="Minecraft"))
    print(f"[SAPI]: Статус загружен")
    name=bot.user.name
    print(f"[{name}]: Бот запустился")
    voice_check.start(bot)
    guild_check.start(bot)
    user_check192.start(bot)

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

create_server_bd()
create_bd_user()
load_ext(bot)

bot.run("MTA3MTA3NDUwNDkxMjE1NDc0Ng.Gan5Zc.KY6TWK7C-lWi6ObpeGvXd2DGbA6J4aHATEzS2o")
