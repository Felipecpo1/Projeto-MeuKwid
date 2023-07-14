from tkinter import *

principal = Tk()

class App():
    def __init__(self):
        self.principal = principal
        self.tela()
        principal.mainloop()
    def tela(self):
        self.principal.title('Meu Kwid')
        self.principal.configure(background='#00FF94')
        self.principal.geometry('980x720')
        self.principal.resizable(True, True)
        self.principal.maxsize(width = 1200, height= 800)
        self.principal.minsize(width= 600, height= 400)

App()

