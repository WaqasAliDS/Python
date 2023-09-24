Pakistani=["Biryani","Qorma","Haleem","Daal"]
Chinese=["Chowmein","Frice Rice","Dumplings"]
Italian=["Pizza","Pasta","croissant"]

Dish=input("Enter the name of the dish:")

if Dish in Pakistani:
    print("Pakistani")
elif Dish in Chinese:
    print("Chinese")
elif Dish in Italian:
    print("Italian")
else:
    print("I don't know!")
