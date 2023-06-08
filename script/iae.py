exp = 1
massive = ["==","<",">","<=",">="]
text=input()
def iae():
    if "if" in text:
        cont = text.split("if")
        cont1 = cont[1].split(":")
        cont = cont1[0]
        cont = cont.replace(" ", "")
        if "==" in cont:a="=="
        elif "<=" in cont:a="<="
        elif ">=" in cont:a=">="
        elif ">" in cont:a=">"
        elif "<" in cont:a="<"
        else:
            print("ERROR: symbol is not in massive please use: [==, <, >, <=, >=]")
            return
        text11 = cont1[1]
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
        cont1[1]= text11.replace("check_user_bd", "")
        if a == "==":
            contt = cont.split("==")
            if eval(contt[0]) == eval(contt[1]):
                print(eval(cont1[1]))
        elif a == "<=":
            contt = cont.split("<=")
            if eval(contt[0]) <= eval(contt[1]):
                print(eval(cont1[1]))
        elif a == ">=":
            contt = cont.split(">=")
            if eval(contt[0]) >= eval(contt[1]):
                print(eval(cont1[1]))
        elif a == "<":
            contt = cont.split("<")
            if eval(contt[0]) < eval(contt[1]):
                print(eval(cont1[1]))
        elif a == ">":
            contt = cont.split(">")
            if eval(contt[0]) > eval(contt[1]):
                print(eval(cont1[1]))

iae()