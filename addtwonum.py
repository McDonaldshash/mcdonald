from tkinter import *

root = Tk()
root.title("Add numbers")

def add():
	pass




def sub():
	pass


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

ans_heading.grid(row=4,column=1)
ans_overall.grid(row=4,column=2)
add_button.grid(row=3,column=2)
main_heading.grid(row=0,column=2)
f_num.grid(row=1,column=1)
s_num.grid(row=2,column=1)
ans_1_in.grid(row=1,column=2)
ans_2_in.grid(row=2,column=2)
subtract_button.grid(row=3,column=1)


root.mainloop()