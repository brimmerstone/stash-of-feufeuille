
print("enter text with numbers i guess")
N = input().replace(',','')
list = [_ for _ in N.split(" ")]

digits = ["ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"]
teens  = ["TEN","ELEVEN","TWELVE"  ,"THIR","FOUR","FIF","SIX","SEVEN","EIGH","NINE"]
tens   = ["","",  "TWEN","THIR","FOR","FIF","SIX","SEVEN","EIGH","NINE"]
tn = "TEEN"; ty = "TY"
exp3n = ["THOUSAND"  ,"M","B",'TR',"QUADR","QUINT","SEXT","SEPT","OCT","NON"]
fx = "ILLION"


def separator(num):
    num = str(num)[::-1]
    txt = ""
    for i in range(len(num)):
        if i%3==0 and i>0:
            txt += " "
        txt += num[i]
    txt = txt[::-1]
    list = [_.lstrip("0") for _ in txt.split(" ")]
    return list


def numtotext(num):

    txt = ""
    nlist = separator(num)
    seps = len(nlist)-1
    for i in nlist:
        if len(i) == 3:
            txt += digits[int(i[-3])] + " HUNDRED"
        if len(i) >= 2:
            if i[-2] == '1':
                if i[-1] >= '3':
                    txt += " " + teens[int(i[-1])] + tn
                else:
                    txt += " " + teens[int(i[-1])]
            elif i[-2] == '0' and i[1] > '0':
                txt += " " + digits[int(i[-1])]
            elif i[-2] == '0' and i[1] == '0':
                txt = txt + " "
            else:
                txt += " " + tens[int(i[-2])] + ty
                if i[-1] > '0':
                    txt += " " + digits[int(i[-1])]
        elif i == "":
            txt = txt
        elif i[-1] > '0':
            txt += " " + digits[int(i[-1])]
        if seps >= 1:
            if i == "":
                txt = txt
            else:
                txt += " " + exp3n[seps-1]
            if seps > 1:
                txt += fx
        seps -= 1

    return txt

for i,word in enumerate(list):
    if word.isdigit():
        list[i] = numtotext(word)
    else:
        list[i] = word.upper()

final = " ".join(list)
print(final)