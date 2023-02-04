import disnake
from disnake.ext import commands
from disnake import Webhook
from disnake import TextInputStyle
import random
import aiohttp
from eco.func.func import *

bot = commands.InteractionBot()

class MyModal2(disnake.ui.Modal):
      def __init__(self):
        components = [
          disnake.ui.TextInput(
              label="Суть запроса",
              placeholder="Укажите текст",
              custom_id="syt",
              style=TextInputStyle.short,
              min_length=1,
              max_length=300
            ),
          disnake.ui.TextInput(
              label="Подробнее",
              placeholder="Укажите текст",
              custom_id="name1",
              style=TextInputStyle.paragraph,
              min_length=20,
              max_length=300
            ),
        ]
        super().__init__(
            title="Тех.Поддержка",
            custom_id="abz.support",
            components=components,
            timeout=300
        )
      async def callback(self, inter: disnake.ModalInteraction):
        async with aiohttp.ClientSession() as session:
            input = inter.text_values
            webhook = Webhook.from_url('https://discord.com/api/webhooks/1044720968540631080/aKBlSXYs92iLKIqg23gncw9DhXsn3uVo9Xn_sdi3A5lyp1NZuQURjss6AG86H950bQvx', session=session)
            embed=disnake.Embed(title=f"{input['syt']}", description=f"{input['name1']}", color=disnake.Colour.random())
            embed.set_author(name=inter.author, icon_url=inter.author.avatar)
            embed.set_footer(text=f"id: {inter.author.id}")
            await webhook.send(username="abz.support", embed=embed)

            await inter.response.send_message(embed=disnake.Embed(description="Вы успешно отправили запрос",
            color=check_server_bd(inter.guild.id)[2]), ephemeral=True)

class SupCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @bot.slash_command(description="Отправить запрос в тех.поддержку")
    async def support(self, inter):
        if check(inter.guild.id, inter.author.id, "bam") == 1:
            await inter.response.send_message("Вы в чс бота!", ephemeral=True)
        else:
            await inter.response.send_modal(modal=MyModal2())

def setup(bot: commands.Bot):
    bot.add_cog(SupCommand(bot))