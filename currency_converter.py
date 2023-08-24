import requests
from tkinter import *

window = Tk()
window.title("CURRENCY CONVERTER")
window.geometry("400x400")
window.maxsize(400, 400)
window.configure(bg="#70C0FA")

welcome = Label(window, width=20, height=3, text="WELCOME!!", font="bold", bg="#1C86EE", justify=CENTER)
welcome.place(x=80, y=50)
info_1 = Label(window, width=30, text="first currency(exp:EUR,GBP):", bg="#70C0FA", justify=LEFT)
info_1.place(x=10, y=150)
currency_1 = Entry(window, width=10, bg='white')
currency_1.place(x=230, y=150)
info_2 = Label(window, width=30, text="second currency(exp:EUR,GBP):", bg="#70C0FA", justify=LEFT)
info_2.place(x=5, y=190)
currency_2 = Entry(window, width=10, bg='white')
currency_2.place(x=230, y=190)
info_3 = Label(window, width=30, text="amount of money:", bg="#70C0FA", justify=LEFT)
info_3.place(x=20, y=230)
amount = Entry(window, width=10, bg='white')
amount.place(x=230, y=230)


def convert():
    if float(amount.get()) > 0:
        api_request = ('https://api.apilayer.com/fixer/convert?to=' + currency_2.get() + '&from=' + currency_1.get() +
               '&amount=' + str(amount.get()))
        payload = {}
        headers = {'apikey': 'YOUR API KEY'}
        response = requests.request('GET', api_request, headers=headers, data=payload)
        result = response.json()
        result_lbl = Label(window, text="Conversation result: {}".format(result['result']), bg="#C1FFC1")
        result_lbl.place(x=85, y=330)
        current_date = Label(window, text="today: {}".format(result['date']), bg="#C1FFC1")
        current_date.place(x=85, y=370)


convert_btn = Button(window, text="convert", justify=CENTER, width=10, bg="#1C86EE", command=convert)
convert_btn.place(x=150, y=280)
window.mainloop()
