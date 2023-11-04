from tkinter import *
#<a href="https://www.flaticon.com/free-icons/plus-minus" title="plus minus icons">Plus minus icons created by WR Graphic Garage - Flaticon</a>
#<a href="https://www.flaticon.com/free-icons/negative" title="negative icons">Negative icons created by Yogi Aprelliyanto - Flaticon</a>
class MenuDemo:
    def __init__(self):
        window = Tk()
        window.title("Menu Demo")

        #Create a menu bar
        menubar = Menu(window) # Create a menu
        window.config(menu = menubar) #display the menu bar

        #create a pulldown menu, and add it to the menu bar
        operationMenu = Menu(menubar, tearoff = 0) # create a pulldown menu
        menubar.add_cascade(label = "Operation", menu = operationMenu)
        operationMenu.add_command(label = "Add", command = self.add) # Menu for Add operation
        operationMenu.add_command(label = "Subtract", command = self.subtract)
        operationMenu.add_separator()
        #operationMenu.add_command(label = "Multiply", command = self.multiply)
        #operationMenu.add_command(label = "Divide", command = self.divide)

        #create more pulldown menus
        exitmenu = Menu(menubar)
        menubar.add_cascade(label = "Exit", menu = exitmenu)
        exitmenu.add_command(label = "Quit", command = window.quit)

        #Add a tool bar frame
        frame0 = Frame(window) #create and add a fram to window
        frame0.grid(row = 1, column = 1, sticky=E)

        #create images
        plus = PhotoImage(file = "/home/kingjofr/Desktop/SchoolProjects/Images/plus.png")
        minus = PhotoImage(file = "/home/kingjofr/Desktop/SchoolProjects/Images/markcd.png")

        Button(frame0, image = plus, command = self.add).grid(row = 1, column = 1, sticky = W)
        Button(frame0, image = minus, command = self.subtract).grid(row = 1, column = 2)

        #Add labels and entries to frame1
        frame1 = Frame(window)
        frame1.grid(row = 2, column = 1, pady=10)
        Label(frame1, text = "Number 1:").pack(side = LEFT)
        self.v1 = StringVar()
        Entry(frame1, width = 5, textvariable = self.v1, justify =RIGHT).pack(side = LEFT)
        Label(frame1, text = "Number 2:").pack(side = LEFT)
        self.v2 = StringVar()
        Entry(frame1, width = 5, textvariable = self.v2, justify = RIGHT).pack(side = LEFT)
        Label(frame1, text = "Result:").pack(side = LEFT)
        self.v3 = StringVar()
        Entry(frame1, width = 5, textvariable = self.v3, justify = RIGHT).pack(side = LEFT)

        # Add buttons to frame2
        frame2 = Frame(window) # create and add frame to window
        frame2.grid(row = 3, column = 1, pady = 10, sticky = E)
        Button(frame2, text = "Subtract", command = self.subtract).pack(side = LEFT)

        mainloop()

    def add(self): #perfoms addition
        self.v3.set(float(self.v1.get()) + float(self.v2.get()))

    def subtract(self):
        self.v3.set(float(self.v1.get()) - float(self.v2.get()))
                    
MenuDemo()