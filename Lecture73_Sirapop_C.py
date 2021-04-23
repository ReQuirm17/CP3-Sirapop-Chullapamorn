systemMenu = {"ข้าวมันไก่":45, 'ข้าวหมกไก่': 30, 'ข้าวหน้าไก่ทอด':50}
Menulist = []
def showBill():
    total = 0
    print("-------My food: -------")
    for number in  range(len(Menulist)):
        print(Menulist[number][0], Menulist[number][1])
        total += int(Menulist[number][1])
    print("total", total)

while True:
    Menuname = input("Please Enter Menu: ")
    if (Menuname.lower() == 'exit'):
        break
    else:
        Menulist.append([Menuname,systemMenu[Menuname]])

print(Menulist)
showBill()


