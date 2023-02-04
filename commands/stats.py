import disnake
from disnake.ext import commands
import psutil
from disnake.utils import *
import sqlite3
from eco.func.func import *
import time

bot = commands.InteractionBot()

bd = 'bd.db'

db = sqlite3.connect(bd)
sql = db.cursor()

global starttime 
starttime = time.time()

ex = "$"
class StatsCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.cooldown(rate=1, per=3, type=commands.BucketType.user)
    @bot.slash_command(description="Статистика бота")
    @commands.guild_only()
    async def stats(self, inter):
        id = inter.author.id
        create(inter.guild.id, id, 10)
        ping = int(self.bot.latency * 1000)
        uptime = format_dt(starttime, 'R')
        sql.execute(f"SELECT * FROM cuscom{inter.guild.id}")
        totalCmd = len(sql.fetchall())
        embed=disnake.Embed(title=f"Инфо об {self.bot.user.name}", color=check_server_bd(inter.guild.id)[2])
        embed.add_field(name=f"Статистика", value=f"Серверов: **{len(self.bot.guilds)}**\nЮзеров: **{len(self.bot.users)}**\n Кол-во команд в боте: **{len(self.bot.all_slash_commands)}**", inline=True)
        embed.add_field(name=f"Клиент", value=f"Задержка: **{ping}**\nПольз.Команд: **{totalCmd}**\n\nВерсия: abz`-`V2.0.0-beta1\nЗапущен: {uptime}", inline=True)
        embed.set_thumbnail(url=self.bot.user.avatar)
        await inter.response.send_message(embed=embed)

    @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
    @bot.slash_command(description="Show server statistic")
    async def dev_stats(self, interaction):
        embed=disnake.Embed(title=f"Statistic for Server: Reserve host", color=check_server_bd(interaction.guild.id)[2])
        try:
            ma = round(psutil.virtual_memory().percent,1)
            ma1 = round(psutil.boot_time(),1)
            a = round(psutil.swap_memory().used,1)
            y = round(psutil.swap_memory().total,1)
            me_tot = int(int(y-a) / 10_000_000)
            sPing = round(self.bot.latency * 100,1)
            rPing = round(self.bot.latency * 222,1)
            embed.add_field(name='Base load', value=f'```cs\n{int(ma/4)}%\n```', inline=True)
            embed.add_field(name="Server load", value=f"```cs\n{int(ma/2*1.4)}%\n```", inline=True)
            embed.add_field(name="Server started", value=f"<t:{int(ma1)}:R>", inline=True)
            embed.add_field(name="Memory used all service", value=f"```cs\n{me_tot} MB\n```", inline=True)
            embed.add_field(name="Ping server", value=f"```cs\n{int(sPing)} MS\n```", inline=True)
            embed.add_field(name="Ping reg.interaction", value=f"```cs\n{int(rPing)} MS\n```", inline=True)
            # Error handler/
        except Exception as er:embed.add_field(name="Error", value=f"```\n{er}\n```", inline=True) 
        await interaction.response.send_message(embed=embed, ephemeral=True)
            # /reldnah rorrE

def setup(bot: commands.Bot):
    bot.add_cog(StatsCommand(bot))
