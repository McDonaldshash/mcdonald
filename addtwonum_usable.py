from tkinter import *
from tkinter import messagebox
from PIL import *


root = Tk()
root.title("Add numbers")

def add():
	ans_1_in.get()
	ans_2_in.get()
	b = int(ans_2_in.get())
	a = int(ans_1_in.get())
	ans_overall.insert(INSERT,a+b)


def clear():
	ans_overall.delete(0,END)


def about():
	messagebox.showinfo("About","Please subscibe for more help"	)



def sub():
	ans_overall.forget()
	ans_1_in.get()
	ans_2_in.get()
	b = int(ans_2_in.get())
	a = int(ans_1_in.get())
	ans_overall.insert(INSERT,a-b)


main_heading = Label(root,text="Enter numbers")
f_num = Label(root,text="Enter first number")
s_num = Label(root,text="Enter second number")
ans_num = Label(root,text="ans")
ans_1_in = Entry(root)
ans_2_in = Entry(root)
add_button = Button(root,text="Add Numbers",command=add)
ans_overall = Entry(root)
subtract_button=Button(root,text="Subtact numbers",command= sub)
ans_heading = Label(root,text="Answer:")
clear_button = Button(root,text="   Clear Text   ",command=clear)
help_button = Button(root,text="About This App",command=about)

ans_heading.grid(row=4,column=1)
ans_overall.grid(row=4,column=2)
add_button.grid(row=3,column=2)
main_heading.grid(row=0,column=2)
f_num.grid(row=1,column=1)
s_num.grid(row=2,column=1)
ans_1_in.grid(row=1,column=2)
ans_2_in.grid(row=2,column=2)
subtract_button.grid(row=3,column=1)
clear_button.grid(row=5,column=2)
help_button.grid(row=5,column=1)

root.mainloop()