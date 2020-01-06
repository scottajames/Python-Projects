#Flips coin 100 times

import random

coin = 0

while coin < 100:
    coin+=1
    print(random.choice(["tails", "heads"]))
