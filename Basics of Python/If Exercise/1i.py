india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city=input("Enter the name of the city:")
if city in india:
    print("This city is located in India")
elif city in pakistan:
    print("This city is located in Pakistan")
elif city in bangladesh:
    print("This city is located in Bangladesh")
else:
    print("This city is not belongs to the given list.")
