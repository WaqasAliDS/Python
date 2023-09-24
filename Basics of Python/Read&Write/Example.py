f=open("E:\\data\\funny.txt","r")
f_out=open("E:\\data\\funny_wc.txt","w")
for line in f:
    token=line.split(" ")
    f_out.write("Word Count:"+str(len(token))+line)

f.close()
f_out.close()
