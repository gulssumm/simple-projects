from tkinter import *
from tkinter import messagebox
import random

def button(frame):
    button_1 = Button(frame, text="  ", font=('arial', 60, 'bold'), width=3, bg='light blue')
    return button_1


def change_choice():
    global choice_1
    for i in ['O', 'X']:
        if i != choice_1:
            choice_1 = i
            break


def reset():
    global choice_1
    for i in range(3):
        for j in range(3):
            button_1[i][j]["text"] = " "      # button is empty
            button_1[i][j]["state"] = NORMAL  # button can be clicked
    choice_1 = random.choice(['O', 'X'])


def check():
    for i in range(3):
        if(button_1[i][0]["text"]==button_1[i][1]["text"]==button_1[i][2]["text"]==choice_1 or
        button_1[0][i]["text"]==button_1[1][i]["text"]==button_1[2][i]["text"]==choice_1):
            messagebox.showinfo("Congrats!!", "'" + choice_1 + "' has won")
            reset()
    if (button_1[0][0]["text"] == button_1[1][1]["text"] == button_1[2][2]["text"] == choice_1 or
        button_1[0][2]["text"] == button_1[1][1]["text"] == button_1[2][0]["text"] == choice_1):
        messagebox.showinfo("Congrats!!", "'" + choice_1 + "' has won")
        reset()
    elif (button_1[0][0]["state"] == button_1[0][1]["state"] == button_1[0][2]["state"] == button_1[1][0]["state"] == button_1[1][1]["state"] == button_1[1][2]["state"] ==button_1[2][0]["state"] == button_1[2][1]["state"] == button_1[2][2]["state"] == DISABLED):
        messagebox.showinfo("Tied!!", "The match ended in a draw")
        reset()


def clicking(row, col):
    button_1[row][col].config(text=choice_1, state=DISABLED)
    check()
    change_choice()
    label.config(text=choice_1 + "'s Chance")


window = Tk()
window.title("TIC-TAC-TOE")
window.geometry('580x650')
window.resizable(0, 0)     # stable window
button_1 = [[], [], []]    # matrix
choice_1 = random.choice(['O', 'X'])
for i in range(3):
    for j in range(3):
        button_1[i].append(button(window))
        button_1[i][j].config(command=lambda row=i, col=j: clicking(row, col))
        button_1[i][j].grid(row=i, column=j)
label = Label(text=choice_1 + "'s Chance", font=('arial', 20, 'bold'))
label.grid(row=3, column=0, columnspan=3)
window.mainloop()
