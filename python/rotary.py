from random import randint,choice

abc_ord = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
qwe_ord = "QWERTYUIOPASDFGHJKLZXCVBNM"
dvo_ord = "PYFGCRLAOEUIDHTNSQJKXBMWVZ"
col_ord = "QWFPGJLUYARSTDHNEIOZXCVBKM"

orders = [abc_ord,qwe_ord,dvo_ord,col_ord]

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
    ord = choice(["A","Q","D","C"])
    logs.append((ord,nth))
    txt = shift(txt,nth,ord)
    print(f"O: {txt}")
print(logs)

ziplog = []
cur = logs[i][0]
cval = logs[i][1]

for i in logs[1:]:
    if cur == i[0]:
        cval += i[1]
    else:
        ziplog.append((cur,cval))
        cur = i[0]
        cval = i[1]
    ziplog.append((cur,cval))
print(ziplog)

# print("O: "+rotate(txt,13)) # ROT13