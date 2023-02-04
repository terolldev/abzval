import disnake
from disnake.ext import commands
from eco.func.func import *
import datetime

bot = commands.InteractionBot()

class BanCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.has_permissions(ban_members = True)
    @bot.slash_command(description="Бан пользователя | User ban", options=[
        disnake.Option("пользователь", description="Укажите пользователя для бана!",   type=disnake.OptionType.user, required=True),
        disnake.Option(
              "причина", description="Укажите причину!", type=disnake.OptionType.string, required=False),],)
    @commands.guild_only()
    async def ban(self, inter, пользователь: disnake.Member, причина=None):
        if пользователь == inter.author:
            embed=disnake.Embed(description="**Причина:**\n> Нельзя указать самого себя!", color=check_server_bd(inter.guild.id)[1], timestamp=datetime.datetime.now())
            embed.set_author(name='Ошибка', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
            embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.response.send_message(embed=embed, ephemeral=True)
        elif причина == None:
            embed=disnake.Embed(title=f'> 🛠️ | Вы были забанены на сервере: {inter.guild.name}', description=f'**Модератор:** {inter.author.mention}\n**Причина:** Без причины', color=check_server_bd(inter.guild.id)[2])
            await пользователь.ban(reason=f'Mod: {inter.author}/{inter.author.id}')
            await пользователь.send(embed=embed)
            embed=disnake.Embed(title="> 🎉 | Забанен",
            description=f'**Модератор:** {inter.author.mention}\n**Пользователь:** {пользователь.mention}\n**Причина:** Без причины',
            color=check_server_bd(ctx.guild.id)[2], timestamp=datetime.datetime.now())
            embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.response.send_message(embed=embed)
        else:
            embed=disnake.Embed(title=f'> 🛠️ | Вы были забанены на сервере: {inter.guild.name}', description=f'**Модератор:** {inter.author.mention}\n**Причина:** {причина}', color=check_server_bd(inter.guild.id)[2])
            await пользователь.ban(reason=f'{причина} (Mod: {inter.author}/{inter.author.id})')
            await пользователь.send(embed=embed)
            embed=disnake.Embed(title="> 🎉 | Забанен",
            description=f'**Модератор:** {inter.author.mention}\n**Пользователь:** {пользователь.mention}\n**Причина:** {причина}',
            color=check_server_bd(inter.guild.id)[2], timestamp=datetime.datetime.now())
            embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.response.send_message(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(BanCommand(bot))