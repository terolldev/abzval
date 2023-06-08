import datetime
from script.event import *
import sqlite3
import disnake
bd = 'bd.db'
ex="$"
db = sqlite3.connect(bd)
sql = db.cursor()

def create(ids: int, id: int, tot: int):
    sql.execute(f"SELECT id FROM user{ids} WHERE id = ?", (id,))
    if sql.fetchone() is None:
        bam = 0
        prem = 0
        bit = 0
        exp = 0
        bitmine = 0
        coin = 0
        pay = 0
        ver = 0
        man = '"Пусто"'
        show = 0
        cris = 0
        inventory = '{}'
        lastact = 0
        sql.execute(f"INSERT INTO user{ids} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (id, tot, bit, bam, prem, exp, bitmine, man, f"{datetime.datetime.now()}", coin, pay, ver, show, cris, inventory, lastact))
        db.commit()
        event("INT_TABLE", ids, id)
    else:
        return
    db.commit()
    return f"yes"

class ValueinBd():
    list = {
        "cash": "Баланс юзера", "bit": "Биткоины юзера", "bam": "Забанен ли?", "prem": "Есть ли премиум?",
        "exp": "Опыт (уровень это -> round(exp/100) )", "bitmine": "Улучшение видео-карт", 
        "use": "использован ли промо-код?", "coin": "Коины юзера", "pay": "заблокированы ли платежы?", "ver": "является ли верифицированным?",
        "man": "Ранг человека", "show": "Возможность просмотреть профиль", "cris": "кристаллики юзера", "inventory": "Инвентарь в JSON формате",
        "lastact": "Последняя активность участника в Unixtimestamp"
    }
    uniitem = {"1337": {"sell": 100_000, "buy": 100_000, "des": "крутая тема покупай"}}

def check(ids: int, id: int, type: str):
    event("SELECT", ids, id)
    for val in sql.execute(f"SELECT {type} FROM user{ids} WHERE id = ?", (id,)):
        if type == "*":return val
        else:return val[0]

def create_bd(id):
    sql.execute(f"""CREATE TABLE IF NOT EXISTS atrib{id} (
    id BIGINT,
    str TEXT,
    lastcode TEXT,
    act BIGINT,
    messages BIGINT,
    total_commands BIGINT
    )""")

def create_bd_item(ids):
    sql.execute(f"""CREATE TABLE IF NOT EXISTS items{ids} (
    name TEXT,
    des TEXT,
    sell BIGINT,
    buy BIGINT,
    usage INT DEFAULT 1,
    type INT,
    typeid BIGINT,
    icon TEXT
    )""")

def createbd(ids: int):
    sql.execute(f"""CREATE TABLE IF NOT EXISTS user{ids} (
    id BIGINT,
    cash BIGINT DEFAULT 10,
    bit BIGINT DEFAULT 0,
    bam INT DEFAULT 0,
    prem INT DEFAULT 0,
    exp BIGINT DEFAULT 0,
    bitmine INT DEFAULT 0,
    man TEXT NOT NULL,
    datecre TEXT,
    coin INT DEFAULT 0,
    pay INT DEFAULT 0,
    ver INT DEFAULT 0,
    show INT DEFAULT 0,
    cris BIGINT DEFAULT 0,
    inventory TEXT,
    lastact BIGINT
)""")

def create_bd_anw(ids):
    sql.execute(f"""CREATE TABLE IF NOT EXISTS anw{ids} (
    name TEXT,
    des TEXT,
    for TEXT,
    count BIGINT,
    forg TEXT,
    countg BIGINT,
    users TEXT
    )""")

def create_bd_cuscom(ids):
    sql.execute(f"""CREATE TABLE IF NOT EXISTS cuscom{ids} (
    name TEXT,
    reply TEXT,
    description TEXT
    )""")

def create_bd_user():
    sql.execute(f"""CREATE TABLE IF NOT EXISTS globaluser (
    id BIGINT,
    prems INT DEFAULT 0,
    ban INT DEFAULT 0,
    mod INT DEFAULT 0,
    tester INT DEFAULT 0,
    busting INT DEFAULT 0,
    endbusitng BIGINT DEFAULT 0
    )""")

def create_server_bd():
    sql.execute(f"""CREATE TABLE IF NOT EXISTS global (
    id BIGINT,
    dcolor INT,
    color INT,
    command INT DEFAULT 1,
    slash INT DEFAULT 0,
    prem INT DEFAULT 0,
    eco INT DEFAULT 1,
    ban INT DEFAULT 0,
    item INT DEFAULT 1,
    limitcash BIGINT DEFAULT 100000,
    limitbit BIGINT DEFAULT 10000,
    limitcoin BIGINT DEFAULT 100,
    enddate BIGINT DEFAULT 0,
    welcome TEXT,
    goodboy TEXT,
    channel BIGINT
    )
    """)

def checkInventory(ids, id)->dict:
    for value in sql.execute(f"SELECT inventory FROM user{ids} WHERE id = ?", (id,)):
        inve = value[0].replace('"', '\"')
        inv = eval(inve)
        return inv
    
def addInventory(ids, id, item: str):
    inv = checkInventory(ids, id)
    count=1
    if item in inv:
        count = inv[f"{item}"]+count
    inv.update({f"{item}": count})
    inv = f"{inv}".replace('"', "'")
    sql.execute(f"UPDATE user{ids} SET inventory = \"{inv}\" WHERE id = {id}")

def takeInventory(ids, id, item):
    inv = checkInventory(ids, id)
    count=1
    if item in inv:
        if inv[f"{item}"] == 1: 
            removeInventory(ids, id, item)
            return
        count = inv[f"{item}"]-count
    inv.update({f"{item}": count})
    inv = f"{inv}".replace('"', "'")
    sql.execute(f"UPDATE user{ids} SET inventory = \"{inv}\" WHERE id = {id}")

def removeInventory(ids, id, item: str):
    inv = checkInventory(ids, id)
    inv.pop(item)
    inv = f"{inv}".replace('"', "'")
    sql.execute(f"UPDATE user{ids} SET inventory = \"{inv}\" WHERE id = {id}")
    
def int_server_bd(ids: int):
    sql.execute(f"SELECT id FROM global WHERE id = ?", (ids,))
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO global VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (ids, 0xed4947, 0x5865F2, 1, 0, 0, 1, 0, 1,
        100_000, 1_000, 100, 0, "Привет {{username}}, мы рады тебя видеть!", "Увы {{username}} вышел, будем надеется что он вернётся", 0))
    db.commit()
    event("INT_TABLE", ids, None)
    

def int_user_bd(id: int):
    sql.execute(f"SELECT id FROM globaluser WHERE id = ?", (id,))
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO globaluser VALUES (?, ?, ?, ?, ?, ?, ?)", (id, 0, 0, 0, 0, 0, 0))
    db.commit()

def change_server_bd(ids: int, type: str, value: str | int):
    sql.execute(f"SELECT id FROM global WHERE id = ?", (ids,))
    if sql.fetchone() is None:
        event("INT_TABLE")
        sql.execute(f"INSERT INTO global VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (ids, 0xed4947, 0x5865F2, 1, 0, 0, 1, 0, 1,
        100_000, 1_000, 100, 0, "Привет {{username}}, мы рады тебя видеть!", "Увы {{username}} вышел, будет надеется что он вернётся", 0))
    if value.__class__ == "str":
        value=value.replace("\"", "'")
        sql.execute(f"UPDATE global SET {type} = \"{value}\" WHERE id = {ids}")
    else:
        sql.execute(f"UPDATE global SET {type} = {value} WHERE id = {ids}")
    db.commit()
    event("CHANGE_TABLE", ids, None)

def change_user_bd(id: int, type: str, value: int):
    sql.execute(f"SELECT id FROM globaluser WHERE id = ?", (id,))
    if sql.fetchone() is None:
        event("INT_TABLE")
        sql.execute(f"INSERT INTO globaluser VALUES (?, ?, ?, ?, ?, ?, ?)", (id, 0, 0, 0, 0, 0, 0))
    sql.execute(f"UPDATE globaluser SET {type} = {value} WHERE id = ?", (id,))
    db.commit()

def check_server_bd(ids: int) -> object:
    for value in sql.execute(f"SELECT * FROM global WHERE id = ?", (ids,)):
        return value
    event("CHECK_TABLE", ids, None)

def check_user_bd(id: int) -> object:
    for value in sql.execute(f"SELECT * FROM globaluser WHERE id = ?", (id,)):
        return value

def check_command(ids, name) -> object:
    for val in sql.execute(f"SELECT reply, description FROM cuscom{ids} WHERE name = ?", (name,)):
        return val
    event("CHECK_TABLE", ids, None)

def create_anw(ids, name, des, fore, count, forg, countg):
    sql.execute(f"SELECT name FROM anw{ids} WHERE name = ?", (name,))
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO anw{ids} VALUES (?, ?, ?, ?, ?, ?, ?)", (name, des, fore, count, forg, countg, '[]'))
    db.commit()

def check_anw(ids, name) -> object:
    for val in sql.execute(f"SELECT * FROM anw{ids} WHERE name = ?", (name,)):
        return val
    event("CHECK_TABLE", ids, None)

def change_anw(ids, name, type, value):
    print(f"UPDATE anw{ids} SET {type} = '{value}' WHERE name = '{name}'")
    sql.execute(f"SELECT name FROM anw{ids} WHERE name = ?", (name,))
    if sql.fetchone() is None:
        return "cin"
    else:
        print(value.__class__)
        if value.__class__ == "str":
            sql.execute(f"UPDATE anw{ids} SET {type} = '{value}' WHERE name = '{name}'")
        else:
            sql.execute(f"UPDATE anw{ids} SET {type} = {value} WHERE name = '{name}'")
    db.commit()

def delete_anw(ids, name):
    sql.execute(f"SELECT name FROM anw{ids} WHERE name = ?", (name,))
    if sql.fetchone() is None:
        return
    else:
        sql.execute(f"DELETE FROM anw{ids} WHERE name = ('{name}')")
        db.commit()

def create_command(ids, name, reply: str, description: str):
    sql.execute(f"SELECT name FROM cuscom{ids} WHERE name = ?", (name,))
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO cuscom{ids} VALUES (?, ?, ?)", (name, reply, description,))
    else:
        return "ciac"
    db.commit()
    event("INT_TABLE", ids, None)
    return f"yes"

def change_command(ids, name, newreply, description):
    sql.execute(f"SELECT name FROM cuscom{ids} WHERE name = ?", (name,))
    if sql.fetchone() is None:
        return "cin"
    else:
        sql.execute(f"UPDATE cuscom{ids} SET reply = \'{newreply}\' WHERE name = ?", (name,))
        sql.execute(f"UPDATE cuscom{ids} SET description = \'{description}\' WHERE name = ?", (name,))
    db.commit()
    event("CHANGE_TABLE", ids), None

def delete_command(ids, name):
    sql.execute(f"SELECT name FROM cuscom{ids} WHERE name = ?", (name,))
    if sql.fetchone() is None:
        return
    else:
        sql.execute(f"DELETE FROM cuscom{ids} WHERE name = ('{name}')")
        db.commit()
# -------

def fora(text: str, ctx: disnake.Message) -> str:
    if "{{" and "}}" in text:
        text1 = text.split('{{')
        ub = text1[1].split('}}')
        text11 = text1[1].replace(ub[1], '')
        text11 = text11.replace('}', '')
        text11 = text11.replace('{', '')
        oldtext = text11
        text11 = text11.replace('create(', '')
        text11 = text11.replace("print(", "")
        text11 = text11.replace("wpti", "print")
        text11 = text11.replace("bot.", "")
        text11 = text11.replace("change_user(", "")
        text11 = text11.replace("change_last(", "")
        text11 = text11.replace("change_command(", "")
        text11 = text11.replace("create_bd_cuscom(", "")
        text11 = text11.replace("change_server_bd", "")
        text11= text11.replace("int_server_bd", "")
        text11= text11.replace("change_user_bd", "")
        text11= text11.replace("check_user_bd", "")
        text11 = text.replace(oldtext, str(eval(text11)))
        text1 = text11.replace('{', '')
        text1 = text1.replace('}', '')
        return text1
    else:
        return text


def check_user(ids, id, val: str) -> str:
    for val in sql.execute(f"SELECT {val} FROM atrib{ids} WHERE id = ?", (id,)):
        return val[0]
    event("CHECK_TABLE", ids, id)

def change_user(ids, id, val: str):
    sql.execute(f"SELECT id FROM atrib{ids} WHERE id = ?", (id,))
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO atrib{ids} VALUES (?, ?, ?, ?, ?, ?)", (id, val, None, 0, 0, 0))
    else:
        sql.execute(f"UPDATE atrib{ids} SET str = {val} WHERE id = '{id}'")
    db.commit()
    event("CHANGE_TABLE", ids, id)
    return f"yes"

def create_use(ids, id):
    sql.execute(f"SELECT id FROM atrib{ids} WHERE id = ?", (id,))
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO atrib{ids} VALUES (?, ?, ?, ?, ?, ?)", (id, None, None, 0, 0, 0))
        event("INT_TABLE", ids, id)

def add_user(ids, id, val: str, value: int):
    sql.execute(f"SELECT id from atrib{ids} WHERE id = ?", (id,))
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO atrib{ids} VALUES (?, ?, ?, ?, ?, ?)", (id, None, None, 0, 0, 0))
        event("INT_TABLE", ids, id)
    else:
        sql.execute(f"UPDATE atrib{ids} SET {val} = {value} WHERE id = '{id}'")
    db.commit()
    event("CHANGE_TABLE", ids, id)

def change_last(ids, id, val: str):
    sql.execute(f"SELECT id FROM atrib{ids} WHERE id = ?", (id,))
    if sql.fetchone() is None:
        event("INT_TABLE")
        sql.execute(f"INSERT INTO atrib{ids} VALUES (?, ?, ?, ?, ?, ?)", (id, None, val, 0, 0, 0))
    else:
        sql.execute(f"UPDATE atrib{ids} SET lastcode = \"{val}\" WHERE id = '{id}'")
    db.commit()
    event("CHANGE_TABLE", ids, id)
    return f"yes"

def check_last(ids, id) -> str:
    for val in sql.execute(f"SELECT lastcode FROM atrib{ids} WHERE id = ?", (id,)):
        return val[0]
    event("CHECK_TABLE", ids, id)

class Text:
    content="""
Используя нашего бота (**абзвал бот**),
вы автоматически соглашаетесь с нашими текущими условиями и положениями, TOS Discord, нашей политикой конфиденциальности,
всеми применимыми законами и правилами и соглашаетесь с тем,
что вы несете единоличную ответственность за соблюдение местных законов.
Если вы не согласны с каким-либо из этих условий,
вам запрещается использовать этого бота.
Материалы, содержащиеся в этом боте,
защищены применимыми законами об авторском праве и товарных знаках.
 - - - 
Если вы нарушайте, или же мешайте/базоюзите/ломайте бота то вы можете быть занесены в чс бота
Администрация имеет право отказать в вашей апилляции!
Разработчик или же тех администратор имеет право обнулить ваш баланс без весомой причины!
Администрация проекта средства на покупку каково либо предмета на возращает!
Мы не являемся коммерческой организацией. Все денежные средства идут на разработку/обеспечение разработчика. Дабы иметь мотивацию
 - - -
Оскорбление администрации/бота = ЧС!
Распространение слухов/багов/лести = ЧС!
Попытка краша/рейда бота = ЧС!
Оскорбление бота/тех.поддержки = ЧС!

Я и мой бот = Мои правила!
Если что-то не нравится ваше место в определёном кАнале.

 - - - 
 - - -
 - - -
Настоящие условия использования регулируются и толкуются в соответствии с законодательством Российской Федерации.
Вы должны безоговорочно подчиниться законам и исключительной юрисдикции судов этого штата.
 - - -
Бот использует API с сайта [www.blockchain.com](https://www.blockchain.com/)
"""