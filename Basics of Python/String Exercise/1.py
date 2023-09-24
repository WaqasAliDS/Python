Monthly_Expense=[2200,2350,2600,2130,2190]
# 1. Extra dollars spent in FEB will be:
Extra_dollar=Monthly_Expense[1]-Monthly_Expense[0]
print(Extra_dollar)
# 2. Expense in first quarter:
first_quarter_exp=Monthly_Expense[0]+Monthly_Expense[1]+Monthly_Expense[2]
print(first_quarter_exp)
# 3. If I spent 2000$ in any month,
x=2000 in Monthly_Expense
print(x) # "2000 is not in the list"
# 4. Adding june expense in monthly expense list:
Monthly_Expense.append(1980)
print(Monthly_Expense)
# 5. Aprile refund correction.
Aprile_refund=200
Aprile=Monthly_Expense[3]-Aprile_refund
Monthly_Expense.insert(3,Aprile)
print(Monthly_Expense)
