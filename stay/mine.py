import disnake
from disnake.ext import commands
import random
from disnake.utils import *
from eco.func.func import *

bot = commands.InteractionBot()
class Criss(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=120)

    @disnake.ui.button(label="0/10", style=disnake.ButtonStyle.primary, emoji="⛏")
    async def cris_button(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
            if interaction.user.id == interaction.author.id:
                button.label = button.label.replace('/10', '')
                number = int(button.label) if button.label else 0
                nice = self
                cris = random.randint(random.randint(12, 31), random.randint(31, 61))
                embed=disnake.Embed(title="Шахта", description=f"Поздравляю вы выкопали: `{cris}` кристалликов", color=check_server_bd(interaction.guild.id)[2])
                if number + 1 >= 10:
                    nice = None
                    embed.description="Вы выкопали максимальное количиство кристалликов, вернитесь через 1 час"
                button.label = str(number + 1) + '/10'
                newbal = check(interaction.guild.id, interaction.author.id, "cris") + cris
                sql.execute(f"UPDATE user{interaction.guild.id} SET cris = {int(newbal)} WHERE id = '{interaction.author.id}'")
                db.commit()
                await interaction.response.edit_message(embed=embed,view=nice)

class MineCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.cooldown(rate=1, per=3600, type=commands.BucketType.user)
    @bot.slash_command(description="Работа! Шахта!")
    async def mine(self, inter):
        if check(inter.guild.id, inter.author.id, 'cash') == None:
            create(inter.guild.id, inter.author.id, 10)
        embed=disnake.Embed(title="Шахта", description="Нажмите кнопку ниже что-бы начать копать", color=check_server_bd(inter.guild.id)[2])
        await inter.response.send_message(embed=embed, view=Criss(), ephemeral=True)

def setup(bot: commands.Bot):
    bot.add_cog(MineCommand(bot))