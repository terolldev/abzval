import disnake
from disnake.ext import commands
from disnake.utils import *
from eco.func.func import *
from disnake import TextInputStyle

bot = commands.InteractionBot()

class Val1(disnake.ui.Modal):
      def __init__(self):
        components = [
          disnake.ui.TextInput(
              label="Текст",
              placeholder="Ведите текст",
              custom_id="msg1",
              style=TextInputStyle.short,
              min_length=1,
              max_length=35,
              required=True
            )
        ]
        super().__init__(
            title="Сообщений при входе",
            custom_id="msg",
            components=components,
        )
      async def callback(self, inter: disnake.ModalInteraction):
        change_server_bd(inter.guild.id, "welcome", inter.text_values['msg1'])
        await inter.response.send_message("Удачно!")
        
class Val2(disnake.ui.Modal):
      def __init__(self):
        components = [
          disnake.ui.TextInput(
              label="Текст",
              placeholder="Ведите текст",
              custom_id="msg2",
              style=TextInputStyle.short,
              min_length=1,
              max_length=35,
              required=True
            )
        ]
        super().__init__(
            title="Сообщений при выходе",
            custom_id="msgg",
            components=components,
        )
      async def callback(self, inter: disnake.ModalInteraction):
        change_server_bd(inter.guild.id, "goodboy", inter.text_values['msg1'])
        await inter.response.send_message("Удачно!")

class Set(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=60)

    @disnake.ui.button(label="Изменить текст сообщений", style=disnake.ButtonStyle.blurple)
    async def mes(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if interaction.user.id == interaction.author.id:
            await interaction.response.send_modal(Val1())

class MesagesCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(cog, member: disnake.User):
        if member.bot == True:pass
        else:
            members=cog.bot.get_all_members()
            for memb in members:
                if memb.id == member.id:pass
                else:pass
            mes = check_server_bd(memb.guild.id)[13]
            if mes == None or "":return
            else:pass
            channel = check_server_bd(memb.guild.id)[15]
            channel = cog.bot.get_channel(channel)
            if channel == 0:return
            mes = mes.replace("{username}", f"{member.name}")
            mes = mes.replace("{usermention}", f"{member.mention}")
            embed=disnake.Embed(title="Участник зашел на сервер", description=mes, color=check_server_bd(memb.guild.id)[2])
            await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(cog, member: disnake.User):
        if member.bot == True:pass
        else:
            members=cog.bot.get_all_members()
            for memb in members:
                if memb.id == member.id:pass
                else:pass
            mes = check_server_bd(memb.guild.id)[14]
            if mes == None or "":return
            else:pass
            channel = check_server_bd(memb.guild.id)[15]
            channel = cog.bot.get_channel(channel)
            if channel == 0:return
            mes = mes.replace("{username}", f"{member.name}")
            mes = mes.replace("{usermention}", f"{member.mention}")
            embed=disnake.Embed(title="Участник вышел с сервера", description=mes, color=check_server_bd(memb.guild.id)[2])
            await channel.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(MesagesCommand(bot))
