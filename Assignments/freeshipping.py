# create a fun. caled free shipping
# would you qualiify for free shipping
# you are a Prime memeber or order is a least 25 
# you are at least 18 years or have parents consent 
# your fun. take four parameters
# prime (bool) cost (float) age(int) consent (bool)
def free_shipping(prime, cost, age, consent):
    try:
        age >= 18 or consent == True and prime == True or cost >= 25 
        print("You are eligible")
    except:
        print("You are not elibable for free shipping, sorry!")
free_shipping()
