import random


def drop_item():
    roll = random.randint(0,10000)
    if roll > 7000:
        print("N")

    elif roll > 9000:
        print("M")
        
    elif roll > 9900:
        print("R")
        
    elif roll > 9990:
        print("L")
        
    elif roll == 10000:
        print("UBER ITEM00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000")
        drop_item
    
    if input("Another again?\n>") == "y":
        drop_item()

    else:
        drop_item()
drop_item()

#  if input("Another again?\n>") == "y":
       # drop_item()
    