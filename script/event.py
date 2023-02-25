import sqlite3
import json
bd = 'bd.db'

db = sqlite3.connect(bd)
sql = db.cursor()

def change_anw(ids, name, type, value):
    sql.execute(f"SELECT name FROM anw{ids} WHERE name = ?", (name,))
    if sql.fetchone() is None:
        return "cin"
    else:
        sql.execute(f"UPDATE anw{ids} SET {type} = {value} WHERE name = ?", (name,))
    db.commit()

def check_user(ids, id, val: str) -> str:
    for val in sql.execute(f"SELECT {val} FROM atrib{ids} WHERE id = ?", (id,)):
        return val[0]

def check(ids: int, id: int, type: str):
    for val in sql.execute(f"SELECT {type} FROM user{ids} WHERE id = ?", (id,)):
        if type == "*":return val
        else:return val[0]

############################################################################################################

def event(type: str, ids: int, id: int):
    if id == None:return
    else:
        sql.execute(f"SELECT * FROM anw{ids}")
        for anw in sql.fetchall():
            if f"{id}" in anw[6]: return
            if "voice_activity" in anw:
                anw2 = anw[2].replace("voice_activity", "act")
                c = int(check_user(ids, id, anw2))
            else:c = int(check_user(ids, id, anw[2]))
            if c >= anw[3]:
                count = check(ids, id, anw[4])
                sql.execute(f"UPDATE user{ids} SET {anw[4]} = {int(count+anw[5])}")
                users = []
                user = anw[6].replace("[", "").replace("]", "").split(",")
                for u in user:
                    users.append(u)
                users.append(id)
                print(users)
                change_anw(ids, anw[0], "users", f"'{users}'")
                db.commit()
                print(f"Change {id}")
                return
            else: return