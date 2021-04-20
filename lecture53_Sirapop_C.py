def vatcalculator(totalprice):
    result = totalprice + (totalprice * 7 / 100)
    return result

totalprice = float(input("Your Price: "))
print(vatcalculator(totalprice))