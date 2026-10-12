from random import choice
from string import ascii_uppercase

letters = [i for i in ascii_uppercase]
tingles = "SHIT FUCK DAMN OMFG LMAO ACAB BFDI LGBT YOLO"
# its gonna take a lot to list all of the known 4 letter words and abbreviations, and i will get bored or cringe at some point
# so im gonna use a select few
gadzooks = [i for i in tingles.split()]
tickmarx = [0 for i in gadzooks]

att = 0
maxatt = 100000
for i in range(maxatt):
    string = ''
    for i in range(4):
        string += choice(letters)
    print(string)
    att += 1
    if string in gadzooks:
        tickmarx[gadzooks.index(string)] += 1

print("Words found: ",end='');
for i,n in enumerate(tickmarx):
    for m in range(n):
        print(gadzooks[i],end=' ')
