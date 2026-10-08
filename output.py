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

for i in range(txtlen):
    pass