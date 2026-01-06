file=open("data.txt","w")
file.write("Hello!")
file.close()

file=open("data.txt","a")
file.write("Hello!")
file.close()

file=open("data.txt","r")
read = file.read()
print(read)
file.close()

with open("data.txt","a") as file:
    file.write("Hello!")