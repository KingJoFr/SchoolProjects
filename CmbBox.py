from tkinter import *

class CmbBox:
    def __init__(self):
        window = Tk()  # create a window
        window.title("Combo Box Demo") # Set title

        #create photo objects
        self.afgan = PhotoImage(file = "/home/kingjofr/Desktop/SchoolProjects/Images/af.png")
        self.alban = PhotoImage(file = "/home/kingjofr/Desktop/SchoolProjects/Images/al.png")

        #create a combo box to select a country
        var = StringVar() # StringVar for Option menu Item Values
        var.set("Afghanistan") # Initial Value
        cmbBox = OptionMenu(window, var, "Afghanistan", "Albania", command = self.processSelection).pack(fill = BOTH)
         
        self.canvas = Canvas(window)
        self.canvas.create_image(100, 50, image = self.afgan, tag = "image")
        self.canvas.pack()

        window.mainloop() # create an event loop

        #display image for selected country
    def processSelection(self, selectedItem):
        self.canvas.delete("image")
        if selectedItem == "Afghanistan":  #flag image for afghanistan
            self.canvas.create_image(100, 50, image = self.afgan, tag = "image")
        elif selectedItem == "Albania": #flag image Albania
            self.canvas.create_image(100, 50, image = self.alban, tag = "image")

CmbBox() # create GUI