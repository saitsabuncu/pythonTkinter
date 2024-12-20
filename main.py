import tkinter as t

#Pencere
window=t.Tk()
window.title("Python Tkinter")
window.minsize(width=450,height=300)

#Label
my_label=t.Label(text="this is a label",font=('Arial',30,'normal'))
my_label.config(bg='black',fg='white')
my_label.pack()

window.mainloop()
