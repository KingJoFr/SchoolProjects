from tkinter import * #Import tkinter


class ButtonDemo:
    def __init__(self):
        self.window = Tk() # root window
        self.btOK = Button(self.window, text = 'Ok', fg = 'red', command = self.processOK) 
        self.btOK.pack() #Place the button in the window
        self.btOpen = Button(self.window, text = 'close', command = self.changeText)
        self.btOpen.pack()


        self.window.mainloop() # Create an event loop
    def processOK(self):
        print('Ok button clicked')
    def changeText(self):
        self.text = 'Open'