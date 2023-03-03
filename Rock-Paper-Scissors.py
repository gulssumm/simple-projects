import random
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("rock-paper-scissiors")
window.configure(bg="#6B33FF")
window.geometry("500x500")


Label(window,text="******ROCK******PAPER******SCISSIORS******",
      justify="center",
      bg="#6B33FF",
      fg="#DA33FF",
      height=5,
      font="Verdana 9 bold"
      ).pack()

Label(window,text="Choose one of them!!!",bg="#8470FF",fg="white",height=3,width=30,
      font="Verdana 9 bold").place(x=100,y=120)


def func_1():
    for i in range(1, 5):
        list = ["rock", "paper", "scissiors"]
        computers_answer = random.choice(list)

    if computers_answer == "scissiors":
        messagebox.showinfo("Show info", "WIN WIN WIN!!!")
    elif computers_answer == "paper":
        messagebox.showinfo("Show info", "LOSE...")
    elif computers_answer == "rock":
        messagebox.showinfo("Show info", "DRAW :O")
Button_1 = Button(window,text="ROCK",command=func_1).place(x=220,y=210)



def func_2():
    for i in range(1, 5):
        list = ["rock", "paper", "scissiors"]
        computers_answer = random.choice(list)

    if computers_answer == "scissiors":
        messagebox.showinfo("Show info", "LOSE...")
    elif computers_answer == "paper":
        messagebox.showinfo("Show info", "DRAW :O")
    elif computers_answer == "rock":
        messagebox.showinfo("Show info", "WIN WIN WIN!!!")
Button_2 = Button(window,text="PAPER",command=func_1).place(x=220,y=280)



def func_3():
    for i in range(1, 5):
        list = ["rock", "paper", "scissiors"]
        computers_answer = random.choice(list)

    if computers_answer == "scissiors":
        messagebox.showinfo("Show info", "DRAW :O")
    elif computers_answer == "paper":
        messagebox.showinfo("Show info", "WIN WIN WIN!!!")
    elif computers_answer == "rock":
        messagebox.showinfo("Show info", "LOSE...")
Button_3 = Button(window,text="SCISSIORS",command=func_1).place(x=212,y=350)






window.mainloop()