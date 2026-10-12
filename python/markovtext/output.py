# to whoever who deleted all that code
# a sincere fuck you

import csv
from string import ascii_uppercase
from random import randint

vals = [i for i in ascii_uppercase + '0123456789' + " '-.,:!?"]
n = len(vals)

txtlen = 200
txt = ""

with open('table.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    data = list(reader)

cur = " "
tempdict = {}
for i in range(txtlen):
    total = 0
    curx = vals.index(cur)
    for y in range(n):
        for x in range(n):
            if x == curx:
                tempdict[vals[y]] = data[y][x]
                total += int(data[y][x])
    sel = randint(1, total)
    for i in tempdict:
        sel -= int(tempdict[i])
        if sel <= 0:
            break
    txt += i; cur = i

print(txt)