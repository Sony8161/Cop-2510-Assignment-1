# Duong Lam #68618275 Tip calculator
''' This program will allow you to input your total subtotal while eating out, and what % you want to tip
and the script will give you how much to tip, and how much the total is.
'''


subtotal = int(input("Enter the subtotal: $"))


tip_amount = int(input("Enter tip amount(as a %):"))

tips = (tip_amount / 100)
actual_tips = (subtotal * tips)

print("Subtotal: $ {:0,.2f}".format(subtotal))

print("Tips: $ {:0,.2f}".format(actual_tips))

Total = (actual_tips + subtotal)

print("Total: $ {:0,.2f}".format(Total))

 
