import disnake
from disnake import TextInputStyle
from disnake.ext import commands
import random
from disnake.utils import *
from eco.func.func import *

bot = commands.InteractionBot()

class DevModal(disnake.ui.Modal):
      def __init__(self):
        components = [
          disnake.ui.TextInput(
              label="Код",
              placeholder="Данный инстумент очень опасен, и доступен только владельцу бота",
              custom_id="text",
              style=TextInputStyle.paragraph,
              min_length=1,
              max_length=250,
              required=True
            )
        ]
        super().__init__(
            title="Выполнить код debug'а",
            custom_id="run_code",
            components=components,
        )
      async def callback(self, inter: disnake.ModalInteraction):
        input = inter.text_values
        text = input['text']
        try:
            defu=eval(text)
        except:
            defu=f"Error!"
        await inter.response.send_message(embed=disnake.Embed(
    description=f"```js\n{defu}\n```",
    color=disnake.Colour.blurple()
))

class DevCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.has_permissions(manage_messages=True)
    @bot.slash_command(description="dev")
    async def dev(self, inter):
        if inter.author.id == 665271319545511939:await inter.response.send_modal(modal=DevModal())
        else:await inter.response.send_message(embed=disnake.Embed(description="You not owner this bot!", color=check_server_bd(inter.guild.id)[2]), ephemeral=True)


    @commands.has_permissions(manage_messages=True)
    @bot.slash_command(description="status", guild_ids=[1044340714932293724, 966808361251270737])
    async def status(self, inter, status: str):
        if inter.author.id == 665271319545511939:
            await self.bot.change_presence(
            activity=disnake.Streaming(
                name=f'{status}',
                 url='https://www.twitch.tv/tim_eiger', twitch_name="discord", game="Minecraft"))
        else:await inter.response.send_message(embed=disnake.Embed(description="You not owner this bot!", color=check_server_bd(inter.guild.id)[2]), ephemeral=True)

    # @commands.Cog.listener()
    # async def on_application_command(self, inter: disnake.ApplicationCommandInteraction):
    #     if check_command(inter.guild.id, inter.application_command.qualified_name) is not None:
    #         reply = check_command(inter.guild.id, inter.application_command.qualified_name)[0]
    #         await inter.response.send_message(reply, ephemeral=True)
    #     else: return

    @commands.Cog.listener("on_application_command")
    async def chack_command(self, interaction: disnake.CommandInteraction):
        namee = interaction.data.name
        if check_command(interaction.guild.id, namee) is not None:
             reply = check_command(interaction.guild.id, namee)[0]
             await interaction.response.send_message(fora(reply, interaction), ephemeral=True)
        else: return

    @commands.cooldown(rate=1, per=360, type=commands.BucketType.guild)
    @commands.has_permissions(administrator=True)
    @bot.slash_command(description="создание временной слеш команды")
    async def create_slash(self, inter, name, description):
        command = disnake.SlashCommand(name=name, description=description)
        await self.bot.create_guild_command(inter.guild.id, command)
        await inter.response.send_message(embed=disnake.Embed(description=f"You create timed slash_command!\nName: {command.name}\nDescription: {command.description}", color=check_server_bd(inter.guild.id)[2]), ephemeral=True)


    @create_slash.autocomplete("name")
    async def language_autocomp(inter: disnake.CommandInteraction, string: str):
        sql.execute(f"SELECT * FROM cuscom{inter.guild.id}")
        commands = []
        server_command = []
        server = inter.bot.get_guild_slash_commands(inter.guild.id)
        for command in server:
            server_command.append(command.name)
        for cmd in sql.fetchall():
            if cmd[0] in server_command:
                pass
            else:
                commands.append(f"{cmd[0]}")
        string = string.lower()
        return [lang for lang in commands if string in lang.lower()]

    @bot.slash_command(description="send", guild_ids=[1044340714932293724, 966808361251270737])
    async def send(self, ctx, member: disnake.User, content):
        if ctx.author.id in [665271319545511939]:
            if member == None:
                await ctx.reply("Пользователь не найден!")
            else:
                await member.send(embed=disnake.Embed(title=f"Сообщение от: {ctx.author}", description=f"```cs\n{content}\n```", color=check_server_bd(ctx.guild.id)[2]))
                await ctx.reply(embed=disnake.Embed(description=f"Я успешно отправил сообщение пользователю {member.mention}", color=check_server_bd(ctx.guild.id)[2]))

def setup(bot: commands.Bot):
    bot.add_cog(DevCommand(bot))