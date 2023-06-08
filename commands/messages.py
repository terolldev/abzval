import disnake
from disnake.ext import commands
from disnake.utils import *
from eco.func.func import *
from disnake import TextInputStyle
from bot.error import *

bot = commands.InteractionBot()

class Val1(disnake.ui.Modal):
      def __init__(self, inter):
        components = [
          disnake.ui.TextInput(
              label="Текст",
              placeholder="Ведите текст",
              custom_id="msg1",
              value=check_server_bd(inter.guild.id)[13],
              style=TextInputStyle.long,
              min_length=1,
              max_length=100,
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
        wel = check_server_bd(inter.guild.id)[13].replace("{{username}}", f"{inter.author}").replace("{{usermention}}", inter.author.mention)
        goo = check_server_bd(inter.guild.id)[14].replace("{{username}}", f"{inter.author}").replace("{{usermention}}", inter.author.mention)
        embed=embed=disnake.Embed(title="Изменить кастомные сообщение",
        description=f"Канал для отправки: <#{check_server_bd(inter.guild.id)[15]}>", color=check_server_bd(inter.guild.id)[2])
        embed.add_field(name="Welcome", value=f"{wel}", inline=False)
        embed.add_field(name="Goodboy", value=f"{goo}", inline=False)
        await inter.response.edit_message(embed=embed,view=Set(inter))
        
class Val2(disnake.ui.Modal):
      def __init__(self, inter):
        components = [
          disnake.ui.TextInput(
              label="Текст",
              placeholder="Ведите текст",
              custom_id="msg2",
              value=check_server_bd(inter.guild.id)[14],
              style=TextInputStyle.long,
              min_length=1,
              max_length=100,
              required=True
            )
        ]
        super().__init__(
            title="Сообщений при выходе",
            custom_id="msgg",
            components=components,
        )
      async def callback(self, inter: disnake.ModalInteraction):
        change_server_bd(inter.guild.id, "goodboy", inter.text_values['msg2'])
        wel = check_server_bd(inter.guild.id)[13].replace("{{username}}", f"{inter.author}").replace("{{usermention}}", inter.author.mention)
        goo = check_server_bd(inter.guild.id)[14].replace("{{username}}", f"{inter.author}").replace("{{usermention}}", inter.author.mention)
        embed=embed=disnake.Embed(title="Изменить кастомные сообщение",
        description=f"Канал для отправки: <#{check_server_bd(inter.guild.id)[15]}>", color=check_server_bd(inter.guild.id)[2])
        embed.add_field(name="Welcome", value=f"{wel}", inline=False)
        embed.add_field(name="Goodboy", value=f"{goo}", inline=False)
        await inter.response.edit_message(embed=embed,view=Set(inter))

class Set(disnake.ui.View):
    def __init__(self, inter):
        super().__init__(timeout=60)

    @disnake.ui.button(label="Welcome", style=disnake.ButtonStyle.blurple)
    async def w(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if interaction.user.id == interaction.author.id:
            await interaction.response.send_modal(Val1(interaction))

    @disnake.ui.button(label="Goodboy", style=disnake.ButtonStyle.blurple)
    async def g(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        if interaction.user.id == interaction.author.id:
            await interaction.response.send_modal(Val2(interaction))

    @disnake.ui.channel_select(placeholder="Укажите канал для отправки сообщений",
    max_values=1, channel_types=[disnake.ChannelType.text, disnake.ChannelType.news])
    async def reply(self, channel: disnake.ui.ChannelSelect, inter: disnake.MessageInteraction):
        change_server_bd(inter.guild.id, "channel", channel.values[0].id)
        wel = check_server_bd(inter.guild.id)[13].replace("{{username}}", f"{inter.author}").replace("{{usermention}}", inter.author.mention)
        goo = check_server_bd(inter.guild.id)[14].replace("{{username}}", f"{inter.author}").replace("{{usermention}}", inter.author.mention)
        embed=embed=disnake.Embed(title="Изменить кастомные сообщение",
        description=f"Канал для отправки: <#{check_server_bd(inter.guild.id)[15]}>", color=check_server_bd(inter.guild.id)[2])
        embed.add_field(name="Welcome", value=f"{wel}", inline=False)
        embed.add_field(name="Goodboy", value=f"{goo}", inline=False)
        await inter.response.edit_message(embed=embed,view=Set(inter))

class MesagesCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.has_permissions(administrator=True)
    @bot.slash_command(description="Изменить настройки сообщений")
    async def message(self, inter):
        wel = check_server_bd(inter.guild.id)[13].replace("{{username}}", f"{inter.author}").replace("{{usermention}}", inter.author.mention)
        goo = check_server_bd(inter.guild.id)[14].replace("{{username}}", f"{inter.author}").replace("{{usermention}}", inter.author.mention)
        embed=embed=disnake.Embed(title="Изменить кастомные сообщение",
        description=f"Канал для отправки: <#{check_server_bd(inter.guild.id)[15]}>", color=check_server_bd(inter.guild.id)[2])
        embed.add_field(name="Welcome", value=f"{wel}", inline=False)
        embed.add_field(name="Goodboy", value=f"{goo}", inline=False)
        await inter.response.send_message(embed=embed,view=Set(inter))

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
            mes = mes.replace("{{username}}", f"{member.name}")
            mes = mes.replace("{{usermention}}", f"{member.mention}")
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
            mes = mes.replace("{{username}}", f"{member.name}")
            mes = mes.replace("{{usermention}}", f"{member.mention}")
            embed=disnake.Embed(title="Участник вышел с сервера", description=mes, color=check_server_bd(memb.guild.id)[2])
            await channel.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(MesagesCommand(bot))
