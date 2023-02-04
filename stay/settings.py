import disnake
from disnake.ext import commands
from disnake.utils import *
from eco.func.func import *
import time
from disnake import TextInputStyle

bot = commands.InteractionBot()

class Val(disnake.ui.Modal):
      def __init__(self):
        components = [
          disnake.ui.TextInput(
              label="Текст",
              placeholder="Ведите цвет в формате hex",
              custom_id="color",
              style=TextInputStyle.short,
              min_length=1,
              max_length=10,
              required=True
            )
        ]
        super().__init__(
            title="Цвет ошибок",
            custom_id="color",
            components=components,
        )
      async def callback(self, inter: disnake.ModalInteraction):
        inter.text_values['color'] = inter.text_values['color'].replace("#", "0x")
        try:
            change_server_bd(inter.guild.id, "dcolor", int(inter.text_values['color'], 16))
            await inter.response.send_message(embed=disnake.Embed(description=f"Вы изменили цвет ошибок на: `{inter.text_values['color']}`", color=int(inter.text_values['color'], 16)), ephemeral=1)
        except:
            await inter.response.send_message(embed=disnake.Embed(description=f"Ошибка! Укажите цифровой код цвета!", color=int(check_server_bd(inter.guild.id)[1])), ephemeral=1)

class Val1(disnake.ui.Modal):
      def __init__(self):
        components = [
          disnake.ui.TextInput(
              label="Текст",
              placeholder="Ведите цвет в формате hex",
              custom_id="color",
              style=TextInputStyle.short,
              min_length=1,
              max_length=10,
              required=True
            )
        ]
        super().__init__(
            title="Цвет сообщений",
            custom_id="color",
            components=components,
        )
      async def callback(self, inter: disnake.ModalInteraction):
        inter.text_values['color'] = inter.text_values['color'].replace("#", "0x")
        try:
            change_server_bd(inter.guild.id, "color", int(inter.text_values['color'], 16))
            await inter.response.send_message(embed=disnake.Embed(description=f"Вы изменили цвет сообщений на: `{inter.text_values['color']}`", color=int(inter.text_values['color'], 16)), ephemeral=1)
        except:
            await inter.response.send_message(embed=disnake.Embed(description=f"Ошибка! Укажите цифровой код цвета!", color=int(check_server_bd(inter.guild.id)[1])), ephemeral=1)

class Set(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=60)

    @disnake.ui.button(label="Цвет сообщений", style=disnake.ButtonStyle.blurple, emoji="🔵")
    async def mes(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if interaction.user.id == interaction.author.id:
            await interaction.response.send_modal(Val1())

    @disnake.ui.button(label="Цвет ошибок", style=disnake.ButtonStyle.red, emoji="🔴")
    async def err(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if interaction.user.id == interaction.author.id:
            await interaction.response.send_modal(Val())

    @disnake.ui.button(label="Включение/Выключение польз", style=disnake.ButtonStyle.gray, emoji="🔘", row=1)
    async def on_off(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if interaction.user.id == interaction.author.id:
            check = str(check_server_bd(interaction.guild.id)[4]).replace("0", "Выключено").replace("1", "Включено")
            check1 = str(check_server_bd(interaction.guild.id)[3]).replace("0", "Выключено").replace("1", "Включено")
            embed=disnake.Embed(
            title=f"Настройки сервера [{interaction.guild.name}]",
                color=check_server_bd(interaction.guild.id)[2]
            )
            embed.add_field(name=f"Цвет обычных сообщение", value=f"{check_server_bd(interaction.guild.id)[2]}", inline=True)
            embed.add_field(name=f"Цвет ошибок", value=f"{check_server_bd(interaction.guild.id)[1]}", inline=True)
            if check_server_bd(interaction.guild.id)[3] == 1:
                change_server_bd(interaction.guild.id, "command", 0)
                embed.add_field(name=f"Включены ли польз.команды?", value="Выключено", inline=True)
            elif check_server_bd(interaction.guild.id)[3] == 0:
                change_server_bd(interaction.guild.id, "command", 1)
                embed.add_field(name=f"Включены ли польз.команды?", value="Включено", inline=True)
            embed.add_field(name=f"Поддержка слешей?", value=check, inline=True)
            await interaction.response.edit_message(embed=embed)
                

class SettingsCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.has_permissions(administrator=True)
    @bot.slash_command(description="Изменить настройки сервера")
    async def settings(self, inter):
        check = str(check_server_bd(inter.guild.id)[4]).replace("0", "Выключено").replace("1", "Включено")
        check1 = str(check_server_bd(inter.guild.id)[3]).replace("0", "Выключено").replace("1", "Включено")
        embed=disnake.Embed(
            title=f"Настройки сервера [{inter.guild.name}]",
            color=check_server_bd(inter.guild.id)[2]
        )
        embed.add_field(name=f"Цвет обычных сообщение", value=f"{check_server_bd(inter.guild.id)[2]}", inline=True)
        embed.add_field(name=f"Цвет ошибок", value=f"{check_server_bd(inter.guild.id)[1]}", inline=True)
        embed.add_field(name=f"Включены ли польз.команды?", value=check1, inline=True)
        embed.add_field(name=f"Поддержка слешей?", value=check, inline=True)
        await inter.response.send_message(embed=embed, view=Set(), ephemeral=1)

def setup(bot: commands.Bot):
    bot.add_cog(SettingsCommand(bot))
