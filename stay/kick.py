import disnake
from disnake.ext import commands
from eco.func.func import *
import datetime

bot = commands.InteractionBot()

class KickCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.has_permissions(kick_members=True)
    @bot.slash_command(description="Кикнуть пользователя", options=[
        disnake.Option(
            "пользователь", description="Укажите пользователя для кика!", type=disnake.OptionType.user, required=True),
        disnake.Option(
            "причина", description="Укажите причину!", type=disnake.OptionType.string, required=False
        ),],)
    @commands.guild_only()
    async def kick(self, inter, пользователь: disnake.Member, причина=None):
        if причина == None:
            reason="Без причины"
        else:
            reason=причина
        await пользователь.kick(reason=f"Mod: {inter.author}")
        embed=disnake.Embed(title="> 🎉 | Кик",
            description=f'**Модератор:** {inter.author.mention}\n**Пользователь:** {пользователь.mention}\n**Причина:{reason}**',
            color=0x2e2f33, timestamp=datetime.datetime.now())
        embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
        await inter.followup.send_message(embed=embed)
        embed=disnake.Embed(title=f'> 🛠️ | Вы были кикнуты на сервере: {inter.guild.name}', description=f'**Модератор:** {inter.author.mention}\n**Причина:{reason}**', color=check_server_bd(inter.guild.id)[2])
        await пользователь.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(KickCommand(bot))