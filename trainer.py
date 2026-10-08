import csv
from string import ascii_uppercase

# filler = [[0]*n]*n  # reset material
# with open('table.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     # writer.writerows(filler) (CAUTION: it will reset the table)

#print(vals)
#print(filler)

vals = [i for i in ascii_uppercase + '0123456789' + " '-.,:!?"]
n = len(vals)

# column - preceding letters (R21-C17 = QU / C17 - Q / R21 - U
# row - following letters

while True:
    inp = input().upper()

    if inp.strip() == '':
        break

    txt = ''
    for i in inp:
        if i in vals:
            txt += i
        else:
            match i:
                case '&':
                    txt += 'AND'
                case '@':
                    txt += 'AT'
                case '#':
                    txt += ':'
                case ';':
                    txt += ','
                case _:
                    pass

    txt = txt.strip()
    if txt == '':
        break

    print(txt)

    for x in range(1,len(txt)):
        y = x-1
        posX = vals.index(txt[x])
        posY = vals.index(txt[y])
        with open('table.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            data = list(reader)
        data[posX][posY] = int(data[posX][posY]) + 1
        with open('table.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

# () LEVEL 2 MARKOV TEXT GENERATOR: WILL USE PHONOTACTICS TO GENERATE TEXT, FILTERS OUT INVALID WORDS BY CHECKING LETTER TYPE
#                                                                             actually that's kinda flawed because this is english
#