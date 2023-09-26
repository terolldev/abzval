def logging(author, guild, database, value, count, reason):
    file = open(f"./logs/abzvalnewlog.txt", "a", encoding="UTF-8")
    file.write(f"GUILD: {guild}, AUTHOR: {author}, \n--------------------\nDATABASE: {database}, VALUE: {value}, COUNT: {count}, REASON: {reason}\n_____________________________\n\n")