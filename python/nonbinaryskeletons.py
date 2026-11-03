from random import random
from time import sleep

sleeping = False

for i in range(128):
    bin = "".join(["0b"] + [str(round(random())) for _ in range(256)])
    print(bin[2:], int(bin, 2))
    if sleeping: sleep(0.1)