file=open("file3.txt","w")
file.write("yes i do it")
file.close()

file=open("file3.txt","r")
print(file.read())