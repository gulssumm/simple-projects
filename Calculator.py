from tkinter import *
window = Tk()
window.title("CALCULATOR")
screen_width=window.winfo_screenwidth()//2-160   #we get the computer's screen size
screen_high=window.winfo_screenheight()//2-150
window.configure(bg="#6B33FF")
window.geometry("550x550+{}+{}".format(screen_width,screen_high))
window.iconbitmap("calculator_icon.png")
#window.resizable(height=False,width=False)  #ekranı büyütüp küçültmeyi yapamicaz

Label(
    window,
    text="-----------------------------------------------------------CALCULATOR-----------------------------------------------------------",
    bg="#6B33FF",
    fg="#DA33FF",
    width=1000,
    height=3,
    justify="center",
    ).pack()
number_1 = Entry(window,width=30,justify="right")
number_1.place(x=150,y=50)
number_2 = Entry(window,width=30,justify="right")
number_2.place(x=150,y=80)
answer = Label(window,text="",width=30,bg="#DA33FF",justify="center")
answer.place(x=150,y=120)


def sum():
    if number_1.get().isdigit() and number_2.get().isdigit():
        n1=float(number_1.get())
        n2=float(number_2.get())
        answer.configure(text="Answer is  " + str(n1+n2))
button_1 = Button(window, text="+",width=8,height=3,activebackground="purple",command=sum)
button_1.place(x=240,y=180)
def subtract():
    if number_1.get().isdigit() and number_2.get().isdigit():
        n1=float(number_1.get())
        n2=float(number_2.get())
        answer.configure(text="Answer is  " + str(-(n1-n2)))
button_2 = Button(window, text="-",width=8,height=3,activebackground="purple",command=subtract)
button_2.place(x=240,y=260)
def divide():
    if number_1.get().isdigit() and number_2.get().isdigit():
        n1=float(number_1.get())
        n2=float(number_2.get())
        answer.configure(text="Answer is  " + str(n1/n2))
button_3 = Button(window, text="/",width=8,height=3,activebackground="purple",command=divide)
button_3.place(x=240,y=340)
def multiply():
    if number_1.get().isdigit() and number_2.get().isdigit():
        n1=float(number_1.get())
        n2=float(number_2.get())
        answer.configure(text="Answer is  " + str(n1*n2))
button_4 = Button(window, text="*",width=8,height=3,activebackground="purple",command=multiply)
button_4.place(x=240,y=420)

number_1.focus()   #cursor is here






window.mainloop()