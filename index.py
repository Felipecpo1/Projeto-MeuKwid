from tkinter import *
from PIL import ImageTk, Image

principal = Tk()

class App():
    def __init__(self):
        self.principal = principal
        self.tela()
        self.divisaoTela()
        self.botoesDiv1()
        principal.mainloop()
    #aspectos da tela principal
    def tela(self):
        self.principal.title('Meu Kwid')
        self.principal.configure(background='#004D6B')
        self.principal.geometry('980x720')
        self.principal.resizable(True, True)
        self.principal.maxsize(width = 1200, height= 800)
        self.principal.minsize(width= 600, height= 400)
    #definindo as divisões da tela principal
    def divisaoTela(self):
        #divisão 1
        self.divisao1 = Frame(self.principal, bd=4, bg='#007CAD', highlightbackground='#00374D', highlightthickness=2)
        self.divisao1.place(relx=0.02, rely=0.05, relwidth=0.2, relheight=0.9)
        #divisao 2
        self.divisao2 = Frame(self.principal, bd=4, bg='#B7FFF2', highlightbackground='#00374D', highlightthickness=2)
        self.divisao2.place(relx=0.25, rely=0.05, relwidth=0.72, relheight=0.9)
    #Inserção de botões referentes a estrutura do carro na divisão 1 da tela principal
    def botoesDiv1(self):
        #botão Frente
        self.botaoFrente = Button(self.divisao1, text='Frente')
        self.botaoFrente.place(relx=0.06, rely=0.03, relwidth=.9, relheight=.05)
        #botão Lado
        self.botaoLado = Button(self.divisao1, text='Lateral')
        self.botaoLado.place(relx=0.06, rely=0.1, relwidth=.9, relheight=.05)
        #botão Traseira
        self.botaTraseira = Button(self.divisao1, text='Traseira')
        self.botaTraseira.place(relx=0.06, rely=0.17, relwidth=.9, relheight=.05)
        #botão Inferior
        self.botaoInfeiror = Button(self.divisao1, text='Inferior')
        self.botaoInfeiror.place(relx=0.06, rely=0.24, relwidth=.9, relheight=.05)
        #botão Interno
        self.botaoInterno = Button(self.divisao1, text='Interior')
        self.botaoInterno.place(relx=0.06, rely=0.31, relwidth=.9, relheight=.05)
    #Carregando imagens para anexá-las aos botões
    def imagemKwid (self):
        self.imagemFrente = Image.open('/imagens/kwidfrente.webp')
App()

