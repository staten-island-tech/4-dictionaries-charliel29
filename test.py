""" def language(x):
    print ("do something")
language("Cadee's computer never seems to work in the morning") """



""" def lang():
   s = 0
   t = 0
   x = input("Put your sentence here")
   for char in x:
     if char == "s" or char == "S":
         s=s+1
     elif char == "t" or char == "T":
         t=t+1
   if s >= t:
      print ("French")
   else:
      print ("English")
lang()
 """
     


""" def spaces():
    c = int(input ("How many parking spaces are there"))
    x = list(input("Put yesterday's parking spaces here"))
    y = list(input("Put todays's parking spaces here"))
    z= 0
    for i in range(c):
        if x[i] == "C" and y[i] == "C":
            z = z + 1
    print (f"There are {z} parking spaces.")
spaces() """


""" def occupied(n,y,t):
    both = 0
    for i in range(n):
        if (y[i] == "C" and t[i] == "C"):
            both +=1
    return both
print(occupied(5,"CCC..", "C.C.C")) """

Toy_store = [
    "item1" = { 
      "name" : "basketball",
      "price" : 29.99,
      "category" : "sports",
    },
    "item2" = {
        "name" : "Pokemon pack",
        "price" : 4.99,
        "category" : "cards",
    },
    "item3 = {
        "name" : "lego set",
        "pirce" : 25.99,
        "category" : "toys",
    },
    item4 = {
        "name" : "Hot wheels",
        "price" : 10.99,
        "category" : "toy cars",
    }
]
print ("Welcome to the Toy store,Here are the items that you can buy")
for index, item in enumerate(Toy_store):
    print (index , ":", item["name"])
x = input("What toy would you like to buy?: ")
for y in Toy_store:
    if x == Toy_store:[y]["name"]
    for z in Toy_store["item1"]:
        print (Toy_store[y][z])

