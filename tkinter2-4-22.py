from tkinter import * # Import tkinter
from tkinter import font

master = Tk()
master.geometry("500x100")
master.title("My first window")



label1 = Label(master, text = "Where am I?", font = ("times new roman", 25))
label2 = Label(master, text = "Python is great", font = ("Times New Roman", 18))
label1.pack()
label2.pack()

button1 = Button(master, text = "Button 1")

button1.pack()

master.configure(bg = "blue")

master.mainloop()