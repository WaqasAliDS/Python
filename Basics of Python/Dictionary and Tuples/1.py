d={"china":143,"india":136,"usa":32,"Pakistan":26}
a=input('''Select the type input from the following:
1. print
2. add
3. remove
4. query
:''')

if a=="print":
    for key in d:
        print("",key,"",d[key])

elif a=="add":
    b=input("Please enter the name of country you want to add:")
    if b in d:
        print("This country already exist in the dictionary.")
    else:
        c=input(f"Enter the total population of {b}.")
        d[b]=c
        print(d)
elif a=="remove":
    r=input("Enter the name of the country you want to remove:")
    if r in d:
        del d[r]
        print(d)
    else:
        print(f"{r} does'nt exist")
else:
    q=input("which country you want to query:")
    print(d[q])










