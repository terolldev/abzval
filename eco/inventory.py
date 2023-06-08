import disnake
from disnake.ext import commands
from bot.error import *
from disnake.utils import *
from eco.func.func import *

bot = commands.InteractionBot()

class confirm(disnake.ui.View):
    def __init__(self, inter: disnake.ModalInteraction, buy: int, name: str):
        super().__init__(timeout=60)
        self.name = name
        self.buy = buy

    @disnake.ui.button(custom_id="confirm", label="Подтвердить", style=disnake.ButtonStyle.green)
    async def confirm_button(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
        newbalance = check(inter.guild.id, inter.author.id, "cash")-self.buy
        sql.execute(f"UPDATE user{inter.guild.id} SET cash = {newbalance} WHERE id = {inter.author.id}")
        addInventory(inter.guild.id, inter.author.id, f"{self.name}")
        embed=disnake.Embed(title=f"Вы купили предмет: {self.name} за {int(self.buy):,} $", color=check_server_bd(inter.guild.id)[2])
        await inter.response.edit_message(embed=embed, view=None)

    @disnake.ui.button(custom_id="cancle", label="Отказаться", style=disnake.ButtonStyle.red)
    async def cancle_button(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
        embed=disnake.Embed(title=f"Вы отказались покупать: {self.name} за {int(self.buy):,} $", color=check_server_bd(inter.guild.id)[2])
        await inter.response.edit_message(embed=embed, view=None)

class confirm1(disnake.ui.View):
    def __init__(self, inter: disnake.ModalInteraction, sell: int, name: str):
        super().__init__(timeout=60)
        self.name = name
        self.sell = sell

    @disnake.ui.button(custom_id="confirm1", label="Подтвердить", style=disnake.ButtonStyle.green)
    async def confirm_button(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
        newbalance = check(inter.guild.id, inter.author.id, "cash")+self.sell
        sql.execute(f"UPDATE user{inter.guild.id} SET cash = {newbalance} WHERE id = {inter.author.id}")
        takeInventory(inter.guild.id, inter.author.id, f"{self.name}")
        embed=disnake.Embed(title=f"Вы продали предмет: {self.name} за {int(self.sell):,} $", color=check_server_bd(inter.guild.id)[2])
        await inter.response.edit_message(embed=embed, view=None)

    @disnake.ui.button(custom_id="cancle1", label="Отказаться", style=disnake.ButtonStyle.red)
    async def cancle_button(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
        embed=disnake.Embed(title=f"Вы отказались продавать: {self.name} за {int(self.sell):,} $", color=check_server_bd(inter.guild.id)[2])
        await inter.response.edit_message(embed=embed, view=None)

class InventoryCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @bot.slash_command(description="Система инвентаря")
    async def inventory(self, inter):pass

    @inventory.sub_command(description="Просмотреть инвентарь")
    async def check(self, inter):
        embed=disnake.Embed(title=f"Инвентарь {inter.author.name}", color=check_server_bd(inter.guild.id)[2])
        items = checkInventory(inter.guild.id, inter.author.id)
        for i in items.keys():
            embed.add_field(f"{i}", f"Количиство: **{items[i]}**")
        if len(embed.fields) < 1:
            embed.description = "В нём нечего нет :<"
        await inter.response.send_message(embed=embed)
        
    @inventory.sub_command(description="Купить предмет")
    async def buy(self, inter, item: str):
        i = ValueinBd().uniitem
        if item in i:
            buy = i[f"{item}"]["buy"]
            if check(inter.guild.id, inter.author.id, "cash") >= buy:
                embed=disnake.Embed(title="Подтверждение", description=f"Вы хотите купить **`{item}`** за **{int(buy):,} $**?", color=check_server_bd(inter.guild.id)[2])
                await inter.response.send_message(embed=embed,view=confirm(inter, buy, item), ephemeral=True)
            elif check(inter.guild.id, inter.author.id, "cash") < buy:
                await Message.sendError(inter, "У вас недостаточно денег")
        else:
            await Message.sendError(inter, "Такого предмета нету!")

    @buy.autocomplete("item")
    async def language_autocomp(inter: disnake.CommandInteraction, string: str):
        string = string.lower()
        return [lang for lang in ValueinBd().uniitem.keys() if string in lang.lower()]

    @inventory.sub_command(description="Продать предмет в инвентаре")
    async def sell(self, inter, item: str):
        i = ValueinBd().uniitem
        if item in i:
            if item in checkInventory(inter.guild.id, inter.author.id):
                sell = i[f"{item}"]["sell"]
                embed=disnake.Embed(title="Подтверждение", description=f"Вы хотите продать **`{item}`** за **{int(sell):,} $**?", color=check_server_bd(inter.guild.id)[2])
                await inter.response.send_message(embed=embed,view=confirm1(inter, sell, item), ephemeral=True)
            else:
                Message.sendError(inter, "У вас нету данного предмета")
        else:
            await Message.sendError(inter, "Данного предмете в базе не найдено, обратитесь к администратору!!")

    @sell.autocomplete("item")
    async def language_autocomp(inter: disnake.CommandInteraction, string: str):
        string = string.lower()
        return [lang for lang in checkInventory(inter.guild.id, inter.author.id).keys() if string in lang.lower()]

    @bot.slash_command()
    async def addinv(self, inter, item):
        addInventory(inter.guild.id, inter.author.id, item)
        await inter.response.send_message("Успешно")
    @bot.slash_command()
    async def removint(self, inter, item):
        takeInventory(inter.guild.id, inter.author.id, item)
        await inter.response.send_message("Успешно")

def setup(bot: commands.Bot):
    bot.add_cog(InventoryCommands(bot))