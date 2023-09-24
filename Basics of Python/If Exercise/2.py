sugar_level=input("Enter your sugar level:")
sugar_level=int(sugar_level)
if sugar_level<80:
    print("Sugar is low.")
elif sugar_level>100:
    print("Sugar is high.")
else:
    print("Sugar is normal.")

