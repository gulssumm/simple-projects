from tkinter import *
from timeit import default_timer as timer
import random
import json


def speed_test():
    sentences = ['Lorem ipsum dolor sit amet', 'consectetur adipiscing elit',
                 'sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', 'Ut enim ad minim veniam',
                 'quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
                 'Duis aute irure dolor in reprehenderit in voluptate velit',
                 'esse cillum dolore eu fugiat nulla pariatur.', 'Excepteur sint occaecat cupidatat non proident,',
                 'sunt in culpa qui officia deserunt mollit anim id est laborum.']
    json_sentences = json.dumps(sentences, indent=2)
    chosen_snt = random.choice(sentences)
    start = timer()
    window = Tk()
    window.title("SPEED TEST")
    window.geometry("1000x500")
    window.maxsize(1000, 500)
    window.configure(bg="#70C0FF")

    welcome = Label(window, text="SPEED TEST", fg="purple", bg="#70C0FF", justify=CENTER,
                    font="bold 20", width=20, height=2, )
    welcome.place(x=250, y=30)
    l1 = Label(window, text=chosen_snt, font="times 15")
    l1.place(x=150, y=150)
    l2 = Label(window, text="start typing:", fg="purple", bg="#70C0FF", justify=LEFT, font="bold", height=1)
    l2.place(x=5, y=250)
    entry = Entry(window, width=100)
    entry.place(x=150, y=250)

    def check():
        if entry.get() == chosen_snt:
            end = timer()
            l3.configure(text=f'time: {round((end - start), 4)}s')
        else:
            l3.configure(text="Wrong Input!!")

    b1 = Button(window, text="Done", command=check, fg="white", bg="pink")
    b1.place(x=150, y=350)
    b2 = Button(window, text="Try Again", command=speed_test, fg="white", bg="pink")
    b2.place(x=250, y=350)
    l3 = Label(window, text="time:", font="times 15", fg="purple", bg="#70C0FF")
    l3.place(x=150, y=450)
    window.mainloop()


if __name__ == '__main__':
    speed_test()
