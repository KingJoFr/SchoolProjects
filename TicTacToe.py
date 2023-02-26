from tkinter import *

class TicTacToe:
    def aboutMe(self):
        pass

    def play(self):
        print("You clicked play.")

    def __init__(self):
        self.window = Tk()
        self.window.title("Tic-Tac-Toe")
        self.window.geometry("1140x1100")
        self.window.resizable(False,False) #dont allow window resizing

        #add font for all windows
        self.window.option_add("*Font", "Times 16 normal")
        self.window.option_add("*Foreground","#000000") # default foreground color
        self.window.configure(bg='#FFF8dc')

        #create a menu bar
        self.menubar = Menu(self.window)
        self.window.config(menu=self.menubar)

        self.GameMenu = Menu(self.menubar)
        self.menubar.add_cascade(label="Game", menu = self.GameMenu)

        # add menu items to Game
        self.GameMenu.add_command(label="Play", command=self.play)
        self.GameMenu.add_command(label="Quit")
        self.GameMenu.add_command(label='Exit', command=exit)

        #self.AboutMenu.add_command(label='About me')
        #self.AboutMenu.add_command(label="Instructions")
        #header Label
        header = Label(self.window, text = 'Tic-Tac-Toe', font = ('Times 18 bold'), bg = '#FFF8dc', fg = '#D2691E')
        #load images
        self.ImageX = PhotoImage(file ="/home/kingjofr/Downloads/PythonX.png")
        self.ImageP = PhotoImage(file ="/home/kingjofr/Downloads/PythonPython.png")
        self.ImageV = PhotoImage(file ="/home/kingjofr/Downloads/PythonVertical.png")
        self.ImageO = PhotoImage(file ="/home/kingjofr/Downloads/PythonO.png")
        self.ImageH = PhotoImage(file ="/home/kingjofr/Downloads/PythonHorizontal.png")
        self.ImageBase = PhotoImage(file ="/home/kingjofr/Downloads/PythonBase.png")
        

        #set default values
        self.b11Val, self.b12Val, self.b13Val = 0,0,0
        self.b21Val, self.b22Val, self.b23Val = 0,0,0
        self.b31Val, self.b32Val, self.b33Val = 0,0,0


        #build and place buttons
        self.b11 = Button(self.window, image = self.ImageBase, command = self.cycle11, highlightthickness = 0, bd = 0)
        self.b11.grid(row = 1, column = 1, sticky = 'W', ipadx = 0, ipady = 0, padx=(20,0), pady=(50,0))
        self.b11 = Button(self.window, image = self.ImageBase, command = self.cycle11, highlightthickness = 0, bd = 0)
        self.b11.grid(row = 1, column = 1, sticky = 'W', ipadx = 0, ipady = 0, padx=(20,0), pady=(50,0))
        self.b11 = Button(self.window, image = self.ImageBase, command = self.cycle11, highlightthickness = 0, bd = 0)
        self.b11.grid(row = 1, column = 1, sticky = 'W', ipadx = 0, ipady = 0, padx=(20,0), pady=(50,0))

        self.b21 = Button(self.window, image = self.ImageBase, command = self.cycle11, highlightthickness = 0, bd = 0)
        self.b21.grid(row = 1, column = 1, sticky = 'W', ipadx = 0, ipady = 0, padx=(20,0), pady=(50,0))
        self.b22 = Button(self.window, image = self.ImageBase, command = self.cycle11, highlightthickness = 0, bd = 0)
        self.b22.grid(row = 1, column = 1, sticky = 'W', ipadx = 0, ipady = 0, padx=(20,0), pady=(50,0))
        self.b23 = Button(self.window, image = self.ImageBase, command = self.cycle11, highlightthickness = 0, bd = 0)
        self.b23.grid(row = 1, column = 1, sticky = 'W', ipadx = 0, ipady = 0, padx=(20,0), pady=(50,0))

        self.b11 = Button(self.window, image = self.ImageBase, command = self.cycle11, highlightthickness = 0, bd = 0)
        self.b11.grid(row = 1, column = 1, sticky = 'W', ipadx = 0, ipady = 0, padx=(20,0), pady=(50,0))
        self.b11 = Button(self.window, image = self.ImageBase, command = self.cycle11, highlightthickness = 0, bd = 0)
        self.b11.grid(row = 1, column = 1, sticky = 'W', ipadx = 0, ipady = 0, padx=(20,0), pady=(50,0))
        self.b11 = Button(self.window, image = self.ImageBase, command = self.cycle11, highlightthickness = 0, bd = 0)
        self.b11.grid(row = 1, column = 1, sticky = 'W', ipadx = 0, ipady = 0, padx=(20,0), pady=(50,0))
        

        self.radioVar = IntVar()
        self.radio1 = Radiobutton(self.window, font= ('Times', 25), text = 'X', variable = self.radioVar, value = 'X', command = self.select)
        self.radio2 = Radiobutton(self.window, font= ('Times', 25), text = 'O', variable = self.radioVar, value = 'O', command = self.select)
        self.radio1.grid(row = 1, column = 6, sticky='N')
        self.radio2.grid(row = 1, column = 7, sticky = 'N')
        

        self.window.mainloop()

    def cycle1(self):
        if self.radioVar.get() == 'X':
            self.b11.configure(image=self.ImageX)
            self.b11Val = 1
        else:
            self.b11.configure(image=self.ImageO)
            self.b11Val = -1
        self.b11["state"] = 'disabled'
        if self.isWinner():print(f"{self.winner} has won the game")
    def select(self):
        pass
    def isWinner(self):
        self.winner = "X"
        return true

TicTacToe() # create gui
