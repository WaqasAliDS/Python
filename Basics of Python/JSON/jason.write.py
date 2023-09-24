book={}
book['tom']={'name':'tom',
             'address':'street 5, NK',
             'phone':'03353470167'}
book['bob']={'name':'bob',
             'address':'street 10, NN',
             'phone':'03040483167'}
import json
s=json.dumps(book)

with open("E:\\data\\book.txt","w") as f:
    f.write(s)
    
