# dictionaries is a type of collection 
# a list is a collection of items 

#store data in key-value pairs
# You can retrevie data quickly by using a unique key





Preston = {
    "name": "Preston",
    "age": 16,
    "city": "st. Michael"
}






#each key must be unique 




print(Preston["name"])




# .get allows you to get a value without erroring


print(Preston.get("names", "not found"))





Preston["names"] = "USAAAAAAAAAAAAAAAAAAAAAA"






Preston.pop("pets") 








# iterate through a dictionary using a for loop
for key, value in Preston.items():
    print(key + " = " + str(value))















print(Preston.keys())


