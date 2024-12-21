import tkinter as t

#Pencere
window=t.Tk()
window.title("Python Tkinter")
window.minsize(width=450,height=300)
def click_button():
    user_input = my_entry.get()
    print(user_input)

#Label
my_label=t.Label(text="this is a label",font=('Arial',30,'normal'))
#my_label.config(bg='black',fg='white')
#my_label.pack(side='top')
#my_label.place(x=0, y=0)
my_label.grid(row=0,column=0)

#button
my_button=t.Button(text='this is a button', command=click_button)
#my_button.pack()
#my_button.place(x=225-63, y=150-14)
# my_button.update()
# print(my_button.winfo_height())
# print(my_button.winfo_width())
my_button.grid(row=1,column=1)

#entry
my_entry=t.Entry(width=20)
#my_entry.pack()
#my_entry.place(x=300,y=200)
my_entry.grid(row=3,column=2)

window.mainloop()