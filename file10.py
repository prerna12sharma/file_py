file=open("file9.txt","r")
f=file.read()
file2=f.split("\n")
count=0
for i in file2:
    if i:
        count+=1
print(count)
file.close()