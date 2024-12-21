from tkinter import *
my_window=Tk()
#title
my_window.title('pencere baslıgı')

#zemin rengi
my_window.configure(bg='#495E57')

#konum-boyut
my_window.geometry('500x500+200+200')

#resize
my_window.resizable(width=True, height=True)
#my_window.minsize(400,400)
#my_window.maxsize(500,500)

#fullscreen
my_window.attributes('-fullscreen',1)
my_window.bind('<Escape>',lambda event: my_window.attributes('-fullscreen',0))

my_window.mainloop()