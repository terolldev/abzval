import disnake
from disnake import TextInputStyle
from disnake.ext import commands
import random
from disnake.utils import *
from eco.func.func import *

bot = commands.InteractionBot()

class Mining(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=60)
    @disnake.ui.button(label="Улучшить", style=disnake.ButtonStyle.primary)
    async def upgrade(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        id = interaction.author.id
        create(interaction.guild.id, id, 10)
        minig = check(interaction.guild.id, id, 'cash')
        upa = check(interaction.guild.id, id, 'bitmine')
        if int(minig) < 1_000_000:
            embed=disnake.Embed(description=f"**Причина:**\n> У вас недостаточно денег для улучшение. Ваш баланс: {check(interaction.guild.id, interaction.author.id, 'cash')}",
            color=check_server_bd(interaction.guild.id)[1], timestamp=datetime.datetime.now())
            embed.set_author(name='Извините', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
            embed.set_footer(text=f"{interaction.author}", icon_url=f"{interaction.author.avatar}")
            await interaction.response.send_message(embed=embed, ephemeral=True)
        elif upa > 9:
            embed=disnake.Embed(description=f"**Причина:**\n> Вы достигли лимита улучшение видео-карт",
            color=check_server_bd(interaction.guild.id)[1], timestamp=datetime.datetime.now())
            embed.set_author(name='Извините', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
            embed.set_footer(text=f"{interaction.author}", icon_url=f"{interaction.author.avatar}")
            await interaction.response.send_message(embed=embed, ephemeral=True)
        else:
            value1 = upa + 1
            newcash = int(minig) - 1_000_00
            sql.execute(f"UPDATE user{interaction.guild.id} SET bitmine = {int(value1)} WHERE id = '{id}'")
            sql.execute(f"UPDATE user{interaction.guild.id} SET cash = {int(newcash)} WHERE id = '{id}'")
            db.commit()
            embed1=disnake.Embed(title="Меню майнинга", description=f"Ваш уровень улучшение видео-карт: {value1}\nСтоимость улучшение: 1.000.000$", color=check_server_bd(interaction.guild.id)[2])
            await interaction.response.edit_message(embed=embed1 ,view=self)

    @disnake.ui.button(label="0/20", style=disnake.ButtonStyle.primary)
    async def minsa(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        id = interaction.author.id
        create(interaction.guild.id, id, 10)
        if check(interaction.guild.id, interaction.author.id, 'bitmine') < 1:
            button.label = 'Недоступно'
            button.disabled = True
            await interaction.response.edit_message(view=self)
        else:
            button.label = button.label.replace('/20', '')
            number = int(button.label) if button.label else 0
            if number + 1 >= 20:
                button.style = disnake.ButtonStyle.primary
                button.disabled = True
                button.emoji = None
                id = interaction.author.id
                bit = check(interaction.guild.id, interaction.author.id, 'bit')
                bitmine = check(interaction.guild.id, interaction.author.id, 'bitmine')
                sql.execute(f"UPDATE user{interaction.guild.id} SET bit = {int(bit + 20 * bitmine)} WHERE id = '{id}'")
                db.commit()
                button.label = f"Вы получили: {20 * bitmine} BTC"
                await interaction.response.edit_message(view=self)
            button.label = str(number + 1) + '/20'
            await interaction.response.edit_message(view=self)

class MiningCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.cooldown(rate=1, per=600, type=commands.BucketType.user)
    @bot.slash_command(description="Майнинг")
    @commands.guild_only()
    async def mining(self, inter):
        userr=inter.author
        id = userr.id
        create(inter.guild.id, id, 10)
        ss = check(inter.guild.id, id, "bam")
        ss12 = check(inter.guild.id, id, "bitmine")
        if ss == 1:
            embed=disnake.Embed(description=f"**Причина:**\n> Вы в чс бота!",
            color=check_server_bd(inter.guild.id)[1], timestamp=datetime.datetime.now())
            embed.set_author(name='Извините', icon_url='https://cdn.discordapp.com/attachments/959338373988900934/959396824173658132/749876351628083221.gif')
            embed.set_footer(text=f"{inter.author}", icon_url=f"{inter.author.avatar}")
            await inter.response.send_message(embed=embed, ephemeral=True)
        else:
           embed=disnake.Embed(title="Меню майнинга", description=f"Ваш уровень улучшение видео-карт: {ss12}\nСтоимость улучшение: 1,000,000$", color=check_server_bd(inter.guild.id)[2])
           await inter.response.send_message(embed=embed, ephemeral=True, view=Mining())

def setup(bot: commands.Bot):
    bot.add_cog(MiningCommand(bot))