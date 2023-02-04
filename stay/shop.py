import disnake
from disnake import TextInputStyle
from disnake.ext import commands
import random
from disnake.utils import *
from eco.func.func import *

bot = commands.InteractionBot()

class ShopCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    items=[
        "Премиум"
    ]

    @bot.slash_command(description="Купить что-то", options=[disnake.Option(name="name", type=disnake.OptionType.string, required=True, choices=items)])
    @commands.guild_only()
    async def buy(self, ctx, name):
        user = ctx.author
        id = user.id
        ss = check(ctx.guild.id, id, "bam")
        if ss == 1:
            await ctx.response.send_message("Вы в чс бота!", ephemeral=True)
        else:
            if name == "Премиум":
                if check(ctx.guild.id,id,'prem') == 1:
                    await ctx.response.send_message(embed=disnake.Embed(description=f"У вас уже есть премка", 
                    color=check_server_bd(ctx.guild.id)[1]), ephemeral=True)
                else:
                    cash = int(check(ctx.guild.id,id,'cash'))
                    if cash < 2000000:
                        await ctx.response.send_message(embed=disnake.Embed(description=f"У вас нет столько денег", 
                        color=check_server_bd(ctx.guild.id)[1]), ephemeral=True)
                    elif cash > 2000000:
                        newcash = cash - 2_000_000
                        sql.execute(f"UPDATE user{ctx.guild.id} SET cash = {newcash} WHERE id = '{id}'")
                        sql.execute(f"UPDATE user{ctx.guild.id} SET prem = {1} WHERE id = '{id}'")
                        db.commit()
                        await ctx.response.send_message(embed=disnake.Embed(description=f"Вы купили Premium за 2,000,000{ex}", 
                        color=check_server_bd(ctx.guild.id)[2]))
            else:
                    await ctx.response.send_message(embed=disnake.Embed(description=f"Нет такого предмета, Вот список доступных:\n**Премиум**: 2,000,000$", 
                    color=check_server_bd(ctx.guild.id)[1]), ephemeral=True)

def setup(bot: commands.Bot):
    bot.add_cog(ShopCommand(bot))