#A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
#Ask user for their salary and year of service and print the net bonus amount.

salary=int(input("enter a salary amount : "))
years=int(input("enter a years of experience: "))
if years>5:
    net_bonus_amount=salary*0.05
    print("net_bonus_amount: ",net_bonus_amount)
else:
    print("your not eligible for bonus")

