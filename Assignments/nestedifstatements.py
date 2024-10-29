prime = True 
cost = 20
age = 17
consent = False

if prime: 
    if age >= 18:
        print("FREE SHIPPING APPLIED")
    elif consent:
         print("FREE SHIPPING APPLIED")
    else: 
         print("NO FREE SHIPPING")

elif cost >= 25:
    if age >= 18:
        print("FREE SHIPPING APPLIED")
    elif consent:
         print("FREE SHIPPING APPLIED")
    else: 
         print("NO FREE SHIPPING")

else:
     print("NO FREE SHIPPING")


# need an umbrella if its raining and you are going outside

raining = input("Is it raining outside?\n>")
outside = input("Going outside?\n>")

if raining. lower() == "yes":
    if outside.lower("yes"):
          print("Bring umbrella")
    else: 
     print("No umbrella needed!")
    



