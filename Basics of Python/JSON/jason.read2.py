f=open("E:\\data\\book.txt","r")
s=f.read()
import json
book=json.loads(s)#now it has been converted into dictionary using loads command.

command = ""
while command != 'exit':
    command = input('Enter a command(options: new,get,save): ')
    if command == "new":
        name = input('Enter name of the person')
        p = input('Phone number: ')
        a = input('Address: ')
        book[name] = {'phone': p, 'address': a}
        print(book)
    elif command == 'get':
        name = input('Enter name of the person')
        if name in book:
            print(book[name])
        else:
            print('person not found in address book')
    elif command == 'save':
        s = json.dumps(book)

        with open("E:\\data\\book.txt", "w") as f:
            f.write(s)
