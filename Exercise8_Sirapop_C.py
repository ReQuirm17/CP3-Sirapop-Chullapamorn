user = input("Your username: ")
password = input("Your Password: ")
if user == "customer" and password == "idNum1452":
    print("--------------------------")
    print("Welcome to Shopping Center")
    print("--------------------------")
    print("This is our items in shop")
    print("--------------------------")
    print("Mango x", 1, 30, "THB  ")
    print("Milk x", 1, 90, "THB " )
    print("soap x", 1, 45, "THB")
    print("Snack Bar x",  1, 70, "THB")
    print("--------------------------")
    userselect = input("what do you want?: ")

mg = "Mango"
mk = "Milk"
sp = "soap"
sb = "Snack Bar"
pricemg = 30
pricemk = 90
pricesp = 45
pricesb = 70

if userselect == mg:
    amount = int(input("amount?: "))
    T = (amount*pricemg)
    print("-----------")
    print("Receive")
    print("Mango x",amount,T,"THB")
    print("-----------")
    print("Thankyou:)")
elif userselect == mk:
    amount = int(input("amount?: "))
    T = amount * pricemk
    print("-----------")
    print("Receive")
    print("Milk x",amount,T,"THB")
    print("-----------")
    print("Thankyou:)")
elif userselect == sp:
    amount = int(input("amount?: "))
    T = amount * pricesp
    print("-----------")
    print("Receive")
    print("soap x",amount,T,"THB")
    print("-----------")
    print("Thankyou:)")
else:
    amount = int(input("amount?: "))
    T = amount * pricesb
    print("-----------")
    print("Receive")
    print("Snack bar x",amount,T,"THB")
    print("-----------")
    print("Thankyou:)")


























