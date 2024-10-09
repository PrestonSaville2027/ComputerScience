hurricane = int(input("What is the wind speed of the hurricane in MPH?\n>"))

if hurricane < 74:
    print("It's a tropical strom")

elif hurricane < 96:
    print("It's a category 1")

elif hurricane < 111:
    print("It's a category 2")

elif hurricane < 130:
    print("It's a category 3")

elif hurricane < 157:
    print("It's a category 4")

else:
    print("It's a category 5")

