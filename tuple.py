#packing 
address = ("10", "Downing Street", "GH15 9YS","London", "England" )
print (address)
print (type (address))
print (address [1])
for item in address:
    print (item)

#unpacking

numbers = (1,2)
n1,n2 = numbers
print (n1)
print (n2)

#1 item tuple
fruit = ("apple",)
print (type (fruit))

#tuple without bracket
nums = 1,5,7
print (type (nums))

#nums.append (9)
nums.pop