from forex_python.converter import CurrencyCodes
from tkinter import *

c = CurrencyCodes()


def get_currency_symbol(event):
    c = CurrencyCodes()
    print(c.get_symbol(input()))


mainwindow = Tk()

text_box1 = Label(mainwindow, text='EUR')
text_box1.grid(row=0, column=1)

text_box2 = Label(mainwindow, text='Euro Member Countries ')
text_box2.grid(row=0, column=2)

text_box3 = Label(mainwindow, text='IDR')
text_box3.grid(row=1, column=1)

text_box4 = Label(mainwindow, text='Indonesia Rupiah')
text_box4.grid(row=1, column=2)

text_box5 = Label(mainwindow, text='BGN')
text_box5.grid(row=2, column=1)

text_box6 = Label(mainwindow, text='Bulgaria Lev')
text_box6.grid(row=2, column=2)

text_box7 = Label(mainwindow, text='ILS')
text_box7.grid(row=3, column=1)

text_box8 = Label(mainwindow, text='Israel Shekel')
text_box8.grid(row=3, column=2)

text_box9 = Label(mainwindow, text='GBP')
text_box9.grid(row=4, column=1)

text_box10 = Label(mainwindow, text='United Kingdom Pound')
text_box10.grid(row=4, column=2)

text_box11 = Label(mainwindow, text='DKK ')
text_box11.grid(row=5, column=1)

text_box12 = Label(mainwindow, text='Denmark Krone')
text_box12.grid(row=5, column=2)

text_box13 = Label(mainwindow, text='CAD')
text_box13.grid(row=6, column=1)

text_box14 = Label(mainwindow, text='Canada Dollar')
text_box14.grid(row=6, column=2)

text_box9 = Label(mainwindow, text='JPY')
text_box9.grid(row=7, column=1)

text_box10 = Label(mainwindow, text='Japan Yen')
text_box10.grid(row=7, column=2)

text_box11 = Label(mainwindow, text='HUF  ')
text_box11.grid(row=8, column=1)

text_box12 = Label(mainwindow, text='Hungary Forint')
text_box12.grid(row=8, column=2)

text_box13 = Label(mainwindow, text='RON ')
text_box13.grid(row=9, column=1)

text_box14 = Label(mainwindow, text='Romania New Leu')
text_box14.grid(row=9, column=2)

text_box15 = Label(mainwindow, text='MYR')
text_box15.grid(row=10, column=1)

text_box16 = Label(mainwindow, text='Malaysia Ringgit')
text_box16.grid(row=10, column=2)

text_box18 = Label(mainwindow, text='SEK')
text_box18.grid(row=11, column=1)

text_box19 = Label(mainwindow, text='Sweden Krona')
text_box19.grid(row=11, column=2)

text_box20 = Label(mainwindow, text='SGD')
text_box20.grid(row=12, column=1)

text_box21 = Label(mainwindow, text='Singapore Dollar')
text_box21.grid(row=12, column=2)

text_box22 = Label(mainwindow, text='HKD')
text_box22.grid(row=13, column=1)

text_box23 = Label(mainwindow, text='Hong Kong Dollar')
text_box23.grid(row=13, column=2)

text_box25 = Label(mainwindow, text='AUD ')
text_box25.grid(row=14, column=1)

text_box26 = Label(mainwindow, text='Australia Dollar')
text_box26.grid(row=14, column=2)

text_box27 = Label(mainwindow, text='CHF')
text_box27.grid(row=15, column=1)

text_box28 = Label(mainwindow, text='Switzerland Franc')
text_box28.grid(row=15, column=2)

text_box29 = Label(mainwindow, text='KRW ')
text_box29.grid(row=16, column=1)

text_box30 = Label(mainwindow, text='Korea (South) Won')
text_box30.grid(row=16, column=2)

text_box31 = Label(mainwindow, text='CNY')
text_box31.grid(row=17, column=1)

text_box32 = Label(mainwindow, text='China Yuan Renminbi')
text_box32.grid(row=17, column=2)

text_box33 = Label(mainwindow, text='TRY')
text_box33.grid(row=18, column=1)

text_box34 = Label(mainwindow, text='Turkey Lira')
text_box34.grid(row=18, column=2)

text_box35 = Label(mainwindow, text='HRK')
text_box35.grid(row=19, column=1)

text_box36 = Label(mainwindow, text='Croatia Kuna')
text_box36.grid(row=19, column=2)

text_box37 = Label(mainwindow, text='NZD')
text_box37.grid(row=20, column=1)

text_box38 = Label(mainwindow, text='New Zealand Dollar')
text_box38.grid(row=20, column=2)

text_box39 = Label(mainwindow, text='THB')
text_box39.grid(row=21, column=1)

text_box40 = Label(mainwindow, text='Thailand Baht')
text_box40.grid(row=21, column=2)

text_box41 = Label(mainwindow, text='USD')
text_box41.grid(row=22, column=1)

text_box42 = Label(mainwindow, text='United States Dollar')
text_box42.grid(row=22, column=2)

text_box43 = Label(mainwindow, text='NOK ')
text_box43.grid(row=23, column=1)

text_box44 = Label(mainwindow, text='Norway Krone')
text_box44.grid(row=23, column=2)

text_box45 = Label(mainwindow, text='RUB')
text_box45.grid(row=24, column=1)

text_box46 = Label(mainwindow, text='Russia Ruble')
text_box46.grid(row=24, column=2)

text_box47 = Label(mainwindow, text='INR')
text_box47.grid(row=25, column=1)

text_box48 = Label(mainwindow, text='India Rupee')
text_box48.grid(row=25, column=2)

text_box49 = Label(mainwindow, text='MXN ')
text_box49.grid(row=26, column=1)

text_box50 = Label(mainwindow, text=' Mexico Peso')
text_box50.grid(row=26, column=2)

text_box51 = Label(mainwindow, text='CZK ')
text_box51.grid(row=27, column=1)

text_box52 = Label(mainwindow, text='Czech Republic Koruna')
text_box52.grid(row=27, column=2)

text_box53 = Label(mainwindow, text='BRL  ')
text_box53.grid(row=28, column=1)

text_box54 = Label(mainwindow, text='Brazil Real')
text_box54.grid(row=28, column=2)

text_box55 = Label(mainwindow, text='PLN ')
text_box55.grid(row=29, column=1)

text_box56 = Label(mainwindow, text='Poland Zloty')
text_box56.grid(row=29, column=2)

text_box57 = Label(mainwindow, text='PHP')
text_box57.grid(row=30, column=1)

text_box58 = Label(mainwindow, text='Philippines Peso')
text_box58.grid(row=30, column=2)

text_box59 = Label(mainwindow, text='ZAR ')
text_box59.grid(row=31, column=1)

text_box60 = Label(mainwindow, text='South Africa Rand ')
text_box60.grid(row=31, column=2)

label_currency = Label(mainwindow, text='currency')
label_currency.grid(row=32, column=1)

textbox_currency = Entry(mainwindow)
textbox_currency.grid(row=32, column=2)

convert_symbol_button = Button(mainwindow, text='symbol')
convert_symbol_button.bind('<Button-1>', get_currency_symbol)
convert_symbol_button.grid(row=33, column=1)

label_symbol = Label(mainwindow, text=c.get_symbol(textbox_currency))
label_symbol.grid(row=33, column=2)

mainwindow.mainloop()
