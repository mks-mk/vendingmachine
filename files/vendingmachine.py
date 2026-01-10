print("WELCOME TO PYHTON VENDING MACHINE")
milk_price=30
curd_price=20
item=input("Which one would you like to buy: \"milk\",\"curd\", Or \"Both\" :")
if item=="milk":
    milk_qty=float(input("\"Thank you for your choice\"\nNow please enter the quantity in Litr:"))
    milk_cost=milk_qty*milk_price
    print("kindly enter the rupees: "+str(milk_cost)+"₹"+" below")
    cost_paid=float(input("Kindly enter the amount to be paid: "))
    if cost_paid==milk_cost:
        print("Thank you, please collect your",item)
    else:
        print("Wrong Entry! please check ")
elif item=="curd":
    curd_qty=float(input(("\"Thank you for your choice\"\nNow please enter the quantity in Litr:")))
    curd_cost=curd_price*curd_qty
    print("kindly enter the rupees: "+str(curd_cost)+"₹"+" below")
    cost_paid=float(input("Kindly enter the amount to be paid: "))
    if cost_paid==curd_cost:
        print("Thank you, please collect your",item)
    else:
        print("Wrong Entry! please check ")
elif item=="both":
    milk_qty=float(input("\"Tank you for choice\"\nNow please enter the quantity of Milk in Litr:"))
    curd_qty=float(input("Enter the quantity of curd in Litr:"))
    both_cost=(milk_price*milk_qty)+(curd_price*curd_qty)
    print("kindly enter the rupees: "+str(both_cost)+"₹"+" below")
    cost_paid=float(input("Kindly enter the amount to be paid: "))
    if cost_paid==both_cost:
         print("Thank you, please collect",item)
    else:
        print("Wrong Entry! please check ")
else:
    print("please Enter the correct choice !")
