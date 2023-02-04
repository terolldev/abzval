import disnake
from disnake.ext import commands
import random
from disnake.utils import *
from eco.func.func import *

bot = commands.InteractionBot()

class CrisCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
    @bot.slash_command(description="Продать кристаллики")
    async def cris_sell(self, inter, cris: commands.Range[1, 10000]):
        if check(inter.guild.id, inter.author.id, "cash") == None:
            create(inter.guild.id, inter.author.id, 10)
        seller = 31 # $
        if check(inter.guild.id, inter.author.id, "cris") < cris:
            embed=disnake.Embed(description=f"**Причина:**\n> У вас недостаточно кристалликов!",
            color=check_server_bd(inter.guild.id)[1], timestamp=datetime.datetime.now())
            embed.set_author(name='Извините', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
            embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.response.send_message(embed=embed, ephemeral=True)
        else:
            total = cris*seller
            totalmon=int(check(inter.guild.id, inter.author.id, "cash")+total)
            sql.execute(f"UPDATE user{inter.guild.id} SET cash = {int(totalmon)} WHERE id = '{inter.author.id}'")
            newcris = int(check(inter.guild.id,inter.author.id,"cris") - cris)
            sql.execute(f"UPDATE user{inter.guild.id} SET cris = {int(newcris)} WHERE id = '{inter.author.id}'")
            db.commit()
            embed=disnake.Embed(title="Продажа кристалликов", description=f"Вы продали `{cris}` кристалликов за {int(total):,} $", color=check_server_bd(inter.guild.id)[2])
            embed.set_footer(text=f"Ваш новый баланс: {int(totalmon):,}")
            await inter.response.send_message(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(CrisCommand(bot))