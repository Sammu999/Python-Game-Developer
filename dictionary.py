capital={"London":"UK","New Delhi":"India","Paris":"France","Washington":"USA"}
print(capital)
print(capital.keys())
print(capital.values())
#Retrieve item using key
print (capital ["London"])
#Retrieve all items
for i in capital:
    print(i,capital[i])
#Add item
capital["Rome"]= "Italyy"
print(capital)
#Update item
capital["Rome"]= "Italy"
print(capital)
#Delete item
del capital["Paris"]
print(capital)