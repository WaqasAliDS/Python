f=open("E:\\data\\book.txt","r")
s=f.read()
print(s)
print(type(s)) #currently it is in string format.
import json
book=json.loads(s)#now it has been converted into dictionary using loads command.
print(book)
print(type(book))

print(book['bob'])
print(book['bob']['phone'])

