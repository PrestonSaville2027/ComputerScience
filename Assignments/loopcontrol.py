# allow you to change how loops operate 
# they do things like quit the loop, skip the current loop, or even do nothing at all
# break, contiune, pass


#break:
#exits a loop prematurely, happens immeditely when ran
# program contiunes where the loop ende
# example


bag_of_fruit = ["apple", "orange", "bug", "kiwi", "watermelon"]

for fruit in bag_of_fruit:
    if fruit == "bug":
       print("a bug!")
       break
    else:
     print("You ate a " + fruit)

#contuine
#skips the current loop
# it does exit the current loop, just moves on to the next iteration



orders = [15, 30, 35, 23, 100, 3, 10, 22]


for order in orders:
   if order < 20:
      continue
   print("$" + str(order) + "order discounted 5% to $" + str(order * 0.95))



#pass
# nothing

#ussally a placeholder

def enter_forest():
   pass