import sqlite3
bd = 'bd.db'

db = sqlite3.connect(bd)
sql = db.cursor()

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

def check_user(ids, id, val: str) -> str:
    for val in sql.execute(f"SELECT {val} FROM atrib{ids} WHERE id = ?", (id,)):
        return val[0]

def check(ids: int, id: int, type: str):
    for val in sql.execute(f"SELECT {type} FROM user{ids} WHERE id = ?", (id,)):
        if type == "*":return val
        else:return val[0]

############################################################################################################

def event(type: str, ids: int=None, id: int=None):
    if ids != None and id is None and type == "CHECK_TABLE":
        print("create table exist")
    if (ids, id) != None:
        sql.execute(f"SELECT * FROM anw{ids}")
        for anw in sql.fetchall():
            if f"{id}" in anw[6]: return
            if anw[5] >= anw[3]:
                count = check(ids, id, anw[4])
                print(count)
                sql.execute(f"UPDATE user{ids} SET {anw[4]} = {int(count+anw[5])}")
                users = []
                user = eval(anw[6])
                for u in user:
                    users.append(u)
                users.append(id)
                sql.execute(f"UPDATE anw{ids} SET users = '{users}' WHERE name = '{anw[0]}'")
                db.commit()
                print(f"Change {id}")
                return
            else: return