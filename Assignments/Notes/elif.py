# the if statement has two buddies 
# the first buudy = else

x = 10

if x > 10:
    print("x is a positive number")

else:
    print("x is a negitive number")

# the second buddy is elif

light = input("What color is the light?\n>")

if light.lower() == "green":
    print("GO")

elif light.lower() == "yellow":
    print("stop if safe")

elif light.lower() == "red":
    print("stop")

else: 
    print("yield")