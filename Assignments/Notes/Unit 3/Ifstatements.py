# If statements evaluate boolean expressions!
# They make decisions about which code to run next

# Take temp.
# Print "<temp.> is hot" if its >= 80
# Otherwise, print "<temp.> is not hot"

temp = input("Whats the tempature in F?\n>")
temp = int(temp)

# This should remind of writing a function

if temp >= 80:
    print(str(temp) + " 0 is hot!")

else: #<-- needs "if"
    print(str(temp) + " 0 is not hot...")

# Not all if statements need an else
# Else statemets are an option, they are optional
# ALL else statements cannot exsist alone 
# An if statememnt can only have one else
password = "skibbi68"
user_input = input("Enter password\n>")

if user_input == password:
    print("ACCESS GRANTED")

else: 
    print("ACCESS DENIED")


