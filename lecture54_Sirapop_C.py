def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return showMenu()
    else:
        return login()

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    return Selectmenu()

def Selectmenu():
    userSelected = int(input(">>"))
    if userSelected == 1:
        price = int(input("your price: "))
        print(vatcal(price))

    elif userSelected == 2:
        return pricecal()

def vatcal(totalPrice):
        vat = 7
        result = totalPrice + (totalPrice * vat / 100)
        return result

def pricecal():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    print(price1+price2)
    return vatcal(price1 + price2)


login()