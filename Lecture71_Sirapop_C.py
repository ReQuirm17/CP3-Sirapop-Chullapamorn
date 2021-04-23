Menulist = []
Pricelist = []

def showBill():
    total = 0
    print("-------My food: -------")
    for number in  range(len(Menulist)):
        print(Menulist[number], Pricelist[number])
        total += int(Pricelist[number])
    print("total: ", total)

while True:
    Menuname = input("Please Enter Menu: ")
    if (Menuname.lower() == 'exit'):
        break
    else:
        Menuprice = input("Price: ")
        Menulist.append(Menuname)
        Pricelist.append(Menuprice)
showBill()




