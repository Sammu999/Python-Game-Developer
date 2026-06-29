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
#nums.pop

#Homework
temperature = (28, 31, 29, 33, 35, 30, 27, 32, 34, 29)

print("Day 2 to Day 5:", temperature[1:5])

print("Max temperature:", max(temperature))
print("Min temperature:", min(temperature))

above_30 = sum(t > 30 for t in temperature)
print("Days above 30°C:", above_30)

temp_list = list(temperature)
temp_list.append(33)
print("Updated list:", temp_list)