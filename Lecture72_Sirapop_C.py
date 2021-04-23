Menulist = []
def showBill():
    total = 0
    print("-------My food: -------")
    for number in  range(len(Menulist)):
        print(Menulist[number][0], Menulist[number][1])

while True:
    Menuname = input("Please Enter Menu: ")
    if (Menuname.lower() == 'exit'):
        break
    else:
        Menuprice = input("Price: ")
        Menulist.append([Menuname,Menuprice])
print(Menulist)
showBill()




