expense_list = [2340, 2500, 2100, 3100, 2980]
month_list=["January", "February", "March", "April", "May"]
expense=input("Please enter the amount of expense:")
expense=int(expense)

month=-1

for i in range(len(expense_list)):
    if expense_list[i]==expense:
        month=i
        break
if month!=-1:
    print(f'You spent {expense} in month of {month_list[month]}')
else:
    print("You did'nt spent this amount")