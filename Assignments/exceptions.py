def divide_two_numbers():
    try: # always enter the "try" block
        x = int(input("What is the first number\n>"))
        y = int(input("What is the second number\n>"))
        print(x/y)

# if = try
# else = except

    except: 
    # If something in the try block craetes an errror
    # the try block stops immediately
    # the only way except runs is by an error
        print("Invalid input")
        divide_two_numbers()
       
divide_two_numbers()

# elif = except with error type

except ValueError:
    print("please enter a valid numerical symbol, try again.")
    divide_two_numbers()