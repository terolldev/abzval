import disnake
from disnake.ext import commands
from disnake.utils import *
import sqlite3
from bot.error import *
import datetime
from eco.func.func import *

bd = 'bd.db'

db = sqlite3.connect(bd)
sql = db.cursor()

bot = commands.InteractionBot()

def check1(ids: int, id: int):
    for val in sql.execute(f"SELECT exp FROM user{ids} WHERE id = ?", (id,)):
        return val[0]

class Events(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_button_click(cog, interaction):
        try:
            if interaction.component.custom_id == "MAINPURSE":
                await interaction.response.send_message(embed=disnake.Embed(title=f"{interaction.message.content} Подтверждённый пользователь", description=f"Администрация сервера подтвердила что {interaction.message.content} является верифицированным лицом", color=check_server_bd(interaction.guild.id)[2]), ephemeral=True)
            elif interaction.component.custom_id == "dev":
                await interaction.response.send_message(
                embed=disnake.Embed(title=f"{interaction.message.content} Является разработчиком бота", 
                description=f"Данный пользователь разработчик бота, или-же со-создатель", 
                color=check_server_bd(interaction.guild.id)[2]), ephemeral=True)
            elif interaction.component.custom_id == "mod":
                await interaction.response.send_message(
                embed=disnake.Embed(title=f"{interaction.message.content} Является модератором бота", 
                description=f"Данный пользователь модератор бота", 
                color=check_server_bd(interaction.guild.id)[2]), ephemeral=True)
            elif interaction.component.custom_id == "cancle" or "confirm" or "cancle1" or "confirm1": return
            else:
                await Message.sendError(interaction, "Данное взаимодействие более не доступно!")
        except Exception as er:
            await Message.sendError(interaction, "Ошибка ответа на взаимодействие!")

    @commands.Cog.listener()
    async def on_slash_command_completion(cog, ctx: disnake.Message):
        create_bd(ctx.guild.id)
        createbd(ctx.guild.id)
        create_bd_cuscom(ctx.guild.id)
        int_server_bd(ctx.guild.id)
        int_user_bd(ctx.author.id)
        create(ctx.guild.id, ctx.author.id, 10)
        e = ctx.application_command.qualified_name
        if e == 'user' and 'crypto' and 'jack' and 'didan' and 'майнинг':
            sql.execute(f"UPDATE user{ctx.guild.id} SET exp = {check1(ctx.guild.id,ctx.author.id) + 1} WHERE id = {ctx.author.id}")
            db.commit()
        else: return

    @commands.Cog.listener()
    async def on_message(cog, ctx: disnake.Message):
        if ctx.author.discriminator == 0000: return
        elif ctx.author.bot == True: return
        if check_server_bd(ctx.guild.id)[3] == 0:
            return
        if ctx.content.startswith("b!") == True:
            commandName = ctx.content.replace("b!", "").split(" ")[0].lower()
            commandReply = check_command(ctx.guild.id, commandName)
            if commandName == "help":
                embed=disnake.Embed(title="Список всех команд на сервере:", color=check_server_bd(ctx.guild.id)[2])
                sql.execute(f"SELECT * FROM cuscom{ctx.guild.id}")
                for cmd in sql.fetchall():
                    embed.add_field(name=f"b!{cmd[0]}", value=cmd[2], inline=True)
                if len(embed.fields) < 1:
                    embed.title=""
                    embed.add_field(name="Я не нашел не одной команды на сервере", 
                    value="Если вы только создали её, подождите 5 минут\nВ противном случае напишите в тех.поддержку: </support:1013033014231580803>", inline=False)
                await ctx.reply(embed=embed)
            elif check_command(ctx.guild.id,commandName) is not None:
                try:
                    if '{' and '}' in commandReply[0]:
                        embed=disnake.Embed(description=fora(commandReply[0], ctx), color=check_server_bd(ctx.guild.id)[2])
                        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar)
                        await ctx.reply(embed=embed)
                    else:
                        embed=disnake.Embed(description=commandReply[0], color=check_server_bd(ctx.guild.id)[2])
                        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar)
                        await ctx.reply(embed=embed)
                except Exception as er:
                     embed=disnake.Embed(title="Во время обработки команды произошла ошибка",description=f"```py\n{er}\n```", color=check_server_bd(ctx.guild.id)[1])
                     await ctx.reply(embed=embed)
        else:return

    @commands.Cog.listener()
    async def on_modal_submit(cog, inter: disnake.ModalInteraction):
        if inter.custom_id == "embed_command":
            input = inter.text_values
            text = input['text']
            text = text.replace("\"", "'")
            change_last(inter.guild.id, inter.author.id, text)
        else: return

def setup(bot: commands.Bot):
    bot.add_cog(Events(bot))