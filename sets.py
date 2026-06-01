numbers = [1,3,5,6,3,5]
nums = set (numbers)
print (nums)
print (type (nums))

#add items
nums.add (2)
print (nums)

#remove items
nums.remove (6)
print (nums)
#nums.remove (10)
nums.discard (10)

fruits = {"orange", "apple", "banana","lime", "pear"}
citrus_fruits = {"lemon", "lime", "orange", "grapefruit"}
#union
print (fruits.union(citrus_fruits))
print (fruits|citrus_fruits)

#intersection
print (fruits.intersection(citrus_fruits))
print (fruits & citrus_fruits)

#difference
print (fruits.difference(citrus_fruits))
print (fruits - citrus_fruits)

#symmetric difference
print (fruits.symmetric_difference(citrus_fruits))
print (fruits ^ citrus_fruits)


