file=open("file12.txt","r")
file1=open("filedelhi.txt","w")
file2=open("shimla.txt","w")
file3=open("otherstate.txt","w")
file4=file.read()
f=file4.split("\n")
i=0
while i<len(f):
    if "delhi" in f[i]:
        file1.write(f[i])
        file1.write("\n")
    elif "shimla" in f[i]:
        file2.write(f[i])
        file2.write("\n")
    else:
        file3.write(f[i])
        file3.write("\n")
    i+=1
file.close() 