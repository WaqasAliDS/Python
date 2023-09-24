#i=1
#Q=str
#while i<=5:
#  Q = input("Are you tired?")
 #   if Q=="no":
  ## elif Q=='yes':
    #    print("You did'nt finish the race.")
    #if i==5:
     #   print("Hurray you finished the race.")
i=0
for i in range(5):
    print(f"you ran {i+1}kms.")
    t=input("Are you tired?")
    if t=="yes":
        break
if i==4:
    print(f"Hurray! you just finished{i+1}kms race.")
else:
    print("You did not finished the race.")










