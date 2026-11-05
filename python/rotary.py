from random import randint,choice

abc_ord  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
qwerty   = "QWERTYUIOPASDFGHJKLZXCVBNM"
qwevert  = "QAZWSXEDCRFVTGBYHNUJMIKOLP"
dvorak   = "PYFGCRLAOEUIDHTNSQJKXBMWVZ"
colemak  = "QWFPGJLUYARSTDHNEIOZXCVBKM"
linotype = "ETAOINSHRDLUCMFWYPVBGKQJXZ"

orders = [abc_ord,qwerty,dvorak,colemak,qwevert,linotype]

def shift(text:str,n:int,order:str=None):
    if order is None:
        order = orders[0]
    else:
        match order.upper():
            case "Q" | "QWE" | "QWERTY":
                order = orders[1]
            case "D" | "DVO" | "DVORAK":
                order = orders[2]
            case "C" | "COL" | "COLEMAK":
                order = orders[3]
            case "QV" | "QWEVERT":
                order = orders[4]
            case "L" | "LINOTYPE" | "ETAOIN":
                order = orders[5]
            case "A" | "ABC" | "ALPHABET" | _:
                order = orders[0]

    new = ""
    for i in text:
        if i.upper() in abc_ord:
            char = order[(order.index(i.upper())+n)%26]
            if i.islower():
                new += char.lower()
            else:
                new += char
        else:
            new += i
    return new

txt = input("I: ")

gen = 10
logs = []
for i in range(gen):
    nth = randint(1,25)
    ord = choice(["A","Q","D","C","QV","L"])
    logs.append((ord,nth))
    txt = shift(txt,nth,ord)
    print(f"{i}: {txt} {logs[-1]}")
print(logs)

ziplog = []
cur = logs[0][0]
cval = logs[0][1]

for i in logs[1:]:
    if cur == i[0]:
        cval += i[1]
    else:
        if cval%26 > 0:
            ziplog.append((cur,cval%26))
        cur = i[0]
        cval = i[1]
if cval%26 > 0:
    ziplog.append((cur,cval%26))
print(ziplog)