# Forloops

# allow the programer to repeat, or what we call loop

# write a program that prints the number 1 through 10 (each on new line)

fav_foods =["Eggs", "Fried Chicken", "Mac n Cheese"]

# for <var> in <list>:

for i in range (0,10):
    print(i)

for food in fav_foods:
    print(food)
    # Runs all of the lines inside the far loop
    # When it reaches the bottom the list, it runs again
    # And moves on to the next item in the list
    # It ends when there are no list items left


for i in range (10,0, -1): # Start, Stop, Step
    print(i)



# Sum of a list
nums = [68, 70, 419, 421, 665]
sum = 0
for n in nums:
    sum = sum + n 

print(sum)



# Square of each number

ints = [3,2,5,4,1]
newlist = []

for i in ints:
    newlist.append(i*i)

print(newlist)

# Character count

stringy = input("please enter a string\n>")
nomvowels = 0
for s in stringy:

    if s.lower() in ["a", "e", "i", "o", "u"]:
        numvowels = numvowels + 1

print(numvowels)



# Print Mult. table
try:
    multi = int(input("Gimme an int yo!\n>"))

except:
    print("womp womp")


for i in range(0, multi + 1):
    print(str(multi) + " x " + str(i) + "=" + str(multi*i))




# lists of names
names = ["Peter" "John"  "Pual" "Luke"]
for name in names:
    print("Hello, " + name + "!")
