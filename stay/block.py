import disnake
from disnake import TextInputStyle
from disnake.ext import commands
import random
from disnake.utils import *
from eco.func.func import *

bot = commands.InteractionBot()

class BlockCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @bot.slash_command(description="Заблокировать переводы на свой аккаунт")
    async def block_pay(self, ctx):
            asd=check(ctx.guild.id, ctx.author.id, "pay")
            create(ctx.guild.id, ctx.author.id, 10)
            if asd == 0:
                sql.execute(f"UPDATE user{ctx.guild.id} SET pay = {1} WHERE id = '{ctx.author.id}'")
                db.commit()
                await ctx.response.send_message(embed=disnake.Embed(description="Вы заблокировали переводы на свой аккаунт", 
                color=check_server_bd(ctx.guild.id)[2]), ephemeral=True)
            elif asd == 1:
                sql.execute(f"UPDATE user{ctx.guild.id} SET pay = {0} WHERE id = '{ctx.author.id}'")
                db.commit()
                await ctx.response.send_message(embed=disnake.Embed(description="Вы разблокировали переводы на свой аккаунт", 
                color=check_server_bd(ctx.guild.id)[2]), ephemeral=True)
    
    @bot.slash_command(description="Скрыть свой профиль от лишних глаз")
    async def show_block(self, ctx):
            asd=check(ctx.guild.id, ctx.author.id, "show")
            create(ctx.guild.id, ctx.author.id, 10)
            if asd == 0:
                sql.execute(f"UPDATE user{ctx.guild.id} SET show = {1} WHERE id = '{ctx.author.id}'")
                db.commit()
                await ctx.response.send_message(embed=disnake.Embed(description="Вы скрыли свой профиль.\nНо администрация сервера всё ещё может его просмотреть", 
                color=check_server_bd(ctx.guild.id)[2]), ephemeral=True)
            elif asd == 1:
                sql.execute(f"UPDATE user{ctx.guild.id} SET show = {0} WHERE id = '{ctx.author.id}'")
                db.commit()
                await ctx.response.send_message(embed=disnake.Embed(description="Вы открыли свой профиль", 
                color=check_server_bd(ctx.guild.id)[2]), ephemeral=True)

def setup(bot: commands.Bot):
    bot.add_cog(BlockCommand(bot))