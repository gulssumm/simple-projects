from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("^^Rıddle^^")
window.geometry("750x650")
window.configure(bg="#70C0FF")
window.iconbitmap("heart.jpeg")


Label(window,text="^^^^WELCOME TO THE CHALLENGE^^^^",
      bg="#70C0FF",
      fg="#8A70FF",
      font="Verdana 14 bold",
      height=2,
      width=50,
      justify="center").pack()


#1.RIDDLE
Label(window,text="1.riddle: What has to be broken before you can use it?",
      font="Verdana 9 bold",
      bg="#8A70FF",
      fg="white",
      justify=LEFT).place(x=5,y=55)
Entry(window,justify=LEFT).place(x=5,y=85)
def check_1():
      messagebox.showinfo("Show Info","The answer is ^^an egg^^")
Button(window,text="Check",justify=LEFT,bg="#F9FF70",fg="#8A70FF",command=check_1).place(x=5,y=115)


#2.RIDDLE
Label(window,text="2.riddle: I’m tall when I’m young, and I’m short when I’m old. What am I?",
      font="Verdana 9 bold",
      bg="#8A70FF",
      fg="white",
      justify=LEFT).place(x=5,y=175)
Entry(window,justify=LEFT).place(x=5,y=205)
def check_2():
      window_2 = Toplevel(window)
      window_2.geometry("200x150")
      Label(window_2, text="The answer is ^^a candle^^", justify="center").pack()
      window_2.mainloop()
Button(window,text="Check",justify=LEFT,bg="#F9FF70",fg="#8A70FF",command=check_2).place(x=5,y=235)


#3.RIDDLE
Label(window,text="3.riddle: What is full of holes but still holds water?",
      font="Verdana 9 bold",
      bg="#8A70FF",
      fg="white",
      justify=LEFT).place(x=5,y=295)
Entry(window,justify=LEFT).place(x=5,y=325)
def check_3():
      window_3 = Toplevel(window)
      window_3.geometry("200x150")
      Label(window_3, text="The answer is ^^a sponge^^", justify="center").pack()
      window_3.mainloop()
Button(window,text="Check",justify=LEFT,bg="#F9FF70",fg="#8A70FF",command=check_3).place(x=5,y=355)


#4.RIDDLE
Label(window,text="4. Riddle: What can’t talk but will reply when spoken to?",
      font="Verdana 9 bold",
      bg="#8A70FF",
      fg="white",
      justify=LEFT).place(x=5,y=415)
Entry(window,justify=LEFT).place(x=5,y=445)
def check_4():
      window_4 = Toplevel(window)
      window_4.geometry("200x150")
      Label(window_4, text="The answer is ^^an echo^^", justify="center").pack()
      window_4.mainloop()
Button(window,text="Check",justify=LEFT,bg="#F9FF70",fg="#8A70FF",command=check_4).place(x=5,y=475)








window.mainloop()