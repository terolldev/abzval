import disnake
from disnake import TextInputStyle
from asyncio.tasks import sleep
from disnake.ext import commands
import sqlite3
import requests
import time
import json
import random
from disnake.utils import *
from eco.func.func import *

bot = commands.InteractionBot()

ex = "$"

bd = 'bd.db'

db = sqlite3.connect(bd)

sql = db.cursor()

def bit():
    url = "https://www.blockchain.com/ru/ticker"
    j = requests.get(url)
    data = json.loads(j.text)
    price = data['USD']['buy']
    global bittime
    bit_time = time.time()
    bittime = format_dt(bit_time, 'R')
    return price

class Button(disnake.ui.View):
    def __init__(self, text11):
        super().__init__()
        self.add_item(disnake.ui.Button(label=f"{text11}", style=disnake.ButtonStyle.primary, 
        disabled=True))

class Select(disnake.ui.View):
    def __init__(self, text11):
        super().__init__()
        self.add_item(disnake.ui.Select(placeholder=text11, options=[
            disnake.SelectOption(
            label="Информация"),disnake.SelectOption(label="Модерация",)], disabled=True))

class Embed1Command(disnake.ui.Modal):
      def __init__(self, inter):
        components = [
          disnake.ui.TextInput(
              label="Текст",
              placeholder="Переменные: {cash}, {bit}, {bam}, {prem}, {:2+2:}, {%def:send(3)%}, {ex}, {bit_curs}, {bittime}",
              custom_id="text",
              style=TextInputStyle.paragraph,
              min_length=1,
              value=check_last(inter.guild.id, inter.author.id),
              max_length=250,
              required=True
            )
        ]
        super().__init__(
            title="Отправить эмбед",
            custom_id="embed_command",
            components=components,
        )
      async def callback(self, inter: disnake.ModalInteraction):
            try:
                color = disnake.Colour.blurple()
                input = inter.text_values
                text = input['text']
                # custom virable number method
                id = inter.author.id
                cash = check(inter.guild.id, id, 'cash')
                bit = check(inter.guild.id, id, 'bit')
                exp = check(inter.guild.id, id, 'exp')
                bitmine = check(inter.guild.id, id, 'bitmine')
                # ----------------------------
                text = text.replace('{ex}', ex)
                if check(inter.guild.id, id, 'cash') == None:
                    text = text.replace('{cash}', 'null')
                    text = text.replace('{bit}', 'null')
                    text = text.replace('{bam}', 'null')
                    text = text.replace('{prem}', 'null')
                    text = text.replace('{exp}', 'null')
                    text = text.replace('{lvl}', 'null')
                    text = text.replace('{man}', 'null')
                    text = text.replace('{bitmine}', 'null')
                    text = text.replace('{author}', f'{inter.author.id}')
                    text = text.replace('||', '\n')
                else:
                    text = text.replace('{cash}', str(check(inter.guild.id, id, 'cash'))+ex)
                    text = text.replace('{bit}', str(check(inter.guild.id, id, 'bit')) + 'BTC')
                    text = text.replace('{bam}', str(check(inter.guild.id, id, 'bam')))
                    text = text.replace('{prem}', str(check(inter.guild.id, id, 'prem')))
                    text = text.replace('{exp}', str(check(inter.guild.id, id, 'exp')))
                    text = text.replace('{lvl}', str(check(inter.guild.id, id, 'exp') / 100))
                    text = text.replace('{man}', str(check(inter.guild.id, id, 'man')))
                    text = text.replace('{bitmine}', str(check(inter.guild.id, id, 'bitmine')))
                    text = text.replace('||', '\n')
                    s = False
                    color = disnake.Colour.blurple()
                if '{:' and ':}' in text:
                    eph =False
                    s=False
                    text1 = text.split('{:')
                    ub = text1[1].split(':}')
                    text11 = text1[1].replace(ub[1], '')
                    text11 = text11.replace(':}', '')
                    oldtext = text11
                    text11 = text11.replace('create(', '')
                    text11 = text11.replace("print(", "")
                    text11 = text11.replace("wpti", "print")
                    text11 = text11.replace("bot(", "")
                    text11 = text11.replace("change_user(", "")
                    text11 = text11.replace("change_last(", "")
                    text11 = text11.replace("change_command(", "")
                    text11 = text11.replace("create_bd_cuscom(", "")
                    text11 = text11.replace("create_use(", "")
                    text11 = text11.replace("add_user(", "")
                    text11 = text11.replace("change_server_bd", "")
                    text11= text11.replace("int_server_bd", "")
                    text11 = text.replace(text11, str(eval(text11)))
                    texti = text11
                    color = disnake.Colour.blurple()
                    text1 = text.replace('{:', '')
                    text1 = text1.replace(':}', '')
                    text1 = texti
                elif '{%' and '%}' in text:
                            text15 = text.split('{%')
                            ub = text15[1].split('%}')
                            text11 = text15[1].replace(ub[1], '')
                            text11 = text11.replace('%}', '')
                            text911 = text11
                            if 'def:' in text11:
                                deff = text11.split('def:')
                                if 'send' and 's' in deff[1]:
                                    if '(' and ')' in deff[1]:
                                        text1 = text.split('(')
                                        ub = text1[1].split(')')
                                        text11 = text1[1].replace(ub[1], '')
                                        text11 = text11.replace(')', '')
                                        if text11 == '':
                                            text11 = "Hello, World!"
                                        embed1=disnake.Embed(description=text11, 
                                        color=disnake.Colour.random())
                                        embed1.set_author(name=inter.author, icon_url=inter.author.avatar)
                                        await inter.channel.send(embed=embed1)
                                        eph = True
                                        s = True
                                        color = disnake.Colour.blurple()
                                        text3 = f"Успешно выполнил: \n||\n{text911}"
                                    else:
                                        eph =False
                                        s=False
                                        text1 = "```py\nArgumentError: argument null\n```"
                                        color = disnake.Colour.red()
                                elif 'addButton' in deff[1]:
                                    text1 = text.split('(')
                                    ub = text1[1].split(')')
                                    text11 = text1[1].replace(ub[1], '')
                                    text11 = text11.replace(')', '')
                                    if text11 == '':
                                        text11 = "Крутая кнопка"
                                    textbtu = text1[0].replace('{:', '')
                                    textbtu = textbtu.replace(':}', '')
                                    textbtu = textbtu.replace('{%', '')
                                    textbtu = textbtu.replace('%}', '')
                                    textbtu = textbtu.replace('addButton', '')
                                    textbtu = textbtu.replace('def:', '')
                                    ub[1] = ub[1].replace('%}', '')
                                    embed1=disnake.Embed(description=f"{textbtu + ub[1]}", 
                                    color=disnake.Colour.random())
                                    embed1.set_author(name=inter.author, icon_url=inter.author.avatar)
                                    await inter.channel.send(embed=embed1, view=Button(text11))
                                    eph = True
                                    s = True
                                    color = disnake.Colour.blurple()
                                    text3 = f"Успешно выполнил: \n||\n{text911}"
                                elif 'addSelect' in deff[1]:
                                    text1 = text.split('(')
                                    ub = text1[1].split(')')
                                    text11 = text1[1].replace(ub[1], '')
                                    text11 = text11.replace(')', '')
                                    if text11 == '':
                                        text11 = "Крутой Select"
                                    textbtu = text1[0].replace('{:', '')
                                    textbtu = textbtu.replace(':}', '')
                                    textbtu = textbtu.replace('{%', '')
                                    textbtu = textbtu.replace('%}', '')
                                    textbtu = textbtu.replace('addSelect', '')
                                    textbtu = textbtu.replace('def:', '')
                                    ub[1] = ub[1].replace('%}', '')
                                    embed1=disnake.Embed(description=f"{textbtu + ub[1]}", 
                                    color=disnake.Colour.random())
                                    embed1.set_author(name=inter.author, icon_url=inter.author.avatar)
                                    await inter.channel.send(embed=embed1, view=Select(text11))
                                    eph = True
                                    s = True
                                    color = disnake.Colour.blurple()
                                    text3 = f"Успешно выполнил: \n||\n{text911}"
                                elif 'checkAtr' in deff[1]:
                                    eph =False
                                    s=False
                                    text1 = text.split('{%')
                                    ub = text1[1].split('%}')
                                    text11 = text1[1].replace(ub[1], '')
                                    text11 = text11.replace('%}', '')
                                    text11 = text11.replace("def:", "")
                                    text11 = text11.replace("checkAtr", "")
                                    text11 = text11.replace("(", "")
                                    text11 = text11.replace(")", "")
                                    if text11 == "":
                                        text11 = inter.author.id
                                    eph =False
                                    s=False
                                    new = check_user(inter.guild.id, text11, "str")
                                    text11 = str(text11).replace(str(text11), str(new))
                                    text1 = text11
                                    color = disnake.Colour.blurple()
                                else:
                                    eph =False
                                    s=False
                                    text1 = "```py\nMethodError: Method null\n```"
                                    color = disnake.Colour.red()
                            else:
                                eph=False
                                s=False
                                text1 = f"```py\nFuncError: Func [{text11.replace('`', '')}] null.\nUse (def:)\n```"
                                color = disnake.Colour.red()
                else:
                    s = False
                    eph = False
                    text1 = text
            except ValueError:
                text1 = "```py\nValueError: invalid literal for int() with base 10:\n```"
                color = disnake.Colour.red()
                s=False
            except IndexError:
                text1 = "```py\nIndexError: invalid virable\n```"
                color = disnake.Colour.red()
                s=False
            except disnake.errors.HTTPException:
                text1 = "Disnake.Error: HTTPException"
                color = disnake.Colour.red()
                s=False
            except SyntaxError as er:
                text1 = f"```py\nSyntaxErorr: {str(er)}\n```"
                color = disnake.Colour.red()
                s=False
            except NameError as er:
                text1 = f"```py\nNameErorr: {str(er)}\n```"
                color = disnake.Colour.red()
                s=False
            except TypeError as er:
                text1 = f"```py\nTypeErorr: {str(er)}\n```"
                color = disnake.Colour.red()
                s=False
            except ZeroDivisionError as er:
                text1 = f"```py\nZeroDivisionError: {str(er)}\n```"
                color = disnake.Colour.red()
                s=False
            except AttributeError as er:
                text1 = f"```py\nAttributeError: {str(er)}\n```"
                color = disnake.Colour.red()
                s=False
            if s == False:
                text1 = text1.replace('%}', '')
                text1 = text1.replace('{%', '')
                text1 = text1.replace('{:', '')
                text1 = text1.replace(':}', '')
                embed = disnake.Embed(description=f"{text1}", color=color)
                eph=False
                await inter.response.send_message(embed=embed, ephemeral=eph)
            elif s == True:
                embed = disnake.Embed(description=f"{text3}", color=color)
                eph=False
                await inter.response.send_message(embed=embed, ephemeral=eph)

class EmbedCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.has_permissions(manage_messages=True)
    @bot.slash_command(description="Отправить сообщение")
    @commands.guild_only()
    async def embed(self, inter):
        await inter.response.send_modal(modal=Embed1Command(inter))

    @commands.has_permissions(administrator=True)
    @bot.slash_command()
    @commands.guild_only()
    async def atret(self, inter, id_user, val):
        if len(val) > 49:
            return await inter.response.send_message(embed=disnake.Embed(description="```py\nAtributeError: Max len(). pls writhe text < 50 symbol\n```", color=disnake.Colour.red()), ephemeral=1)
        sql.execute(f"UPDATE atrib{inter.guild.id} SET str = \"{val}\" WHERE id = '{id_user}'")
        db.commit()
        await inter.response.send_message(f"Изменил {id_user}[`atr`], на `{val}`", ephemeral=1)

def setup(bot: commands.Bot):
    bot.add_cog(EmbedCommand(bot))