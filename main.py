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
my_label.config(bg='black',fg='white')
my_label.pack()

#button
my_button=t.Button(text='this is a button', command=click_button)
my_button.pack()

#entry
my_entry=t.Entry(width=20)
my_entry.pack()

window.mainloop()
