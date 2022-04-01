from tkinter import *
import random
from tkinter import messagebox
from PIL import *

root  = Tk()
root.title("Quizz App")


def about():
    messagebox.showinfo("About","Subcribe for more Vedios")



def clear():
    entry_answer.delete(0,END)
    entry_answer.forget()


def check():
    entry_answer.get()
    d = int(entry_answer.get())
    print(d)

    c= int(a+b)
    print(c)
    if int(c) == int(d) :
        answer_show.config(text ="Correct!",fg="green")
    else:
        answer_show.config(text="Wrong!",fg="red")


def reload():
    global a
    global b
    a = random.randrange(8)
    b = random.randrange(8)
    question1.config(text=int(a))
    question2.config(text=int(b))


heading = Label(root,text="                  Welcome to Quizz")
question1 = Label(root,text="")
question2 = Label(root,text="")
enter_button = Button(root,text="Check Answer",command=check)
refresh_button = Button(root,text="Reload Again",command = reload)
plus = Label(root,text="+")
equal_label = Label(root,text="=")
entry_answer = Entry(root)
answer_show = Label(root,text="")
clear_button = Button(root,text="Clear",padx=10,pady=40,command=clear)
About_me = Button(root,text="About App",command = about) 


About_me.place(x=70,y=120)
clear_button.place(x=10,y=60)
answer_show.place(x=70,y=150)
entry_answer.place(x=100,y=30)
equal_label.place(x=75,y=30)
refresh_button.place(x=70,y=90)
enter_button.place(x=70,y=60)
heading.place(x=0,y=0)
question1.place(x=0,y=30)
question2.place(x=50,y=30)
plus.place(x=25,y=30)

root.mainloop()