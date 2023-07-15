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
        self.exibirImagem()

    # Aspectos da tela principal
    def tela(self):
        self.principal.title('Meu Kwid')
        self.principal.configure(background='#004D6B')
        self.principal.geometry('980x640')
        self.principal.resizable(True, True)
        self.principal.maxsize(width=1200, height=800)
        self.principal.minsize(width=600, height=400)

    # Definindo as divisões da tela principal
    def divisaoTela(self):
        # Divisão 1
        self.divisao1 = Frame(self.principal, bd=4, bg='#007CAD', highlightbackground='#00374D', highlightthickness=2)
        self.divisao1.place(relx=0.02, rely=0.05, relwidth=0.2, relheight=0.9)
        # Divisao 2
        self.divisao2 = Frame(self.principal, bd=4, bg='#F0F0F0', highlightbackground='#00374D', highlightthickness=2)
        self.divisao2.place(relx=0.25, rely=0.05, relwidth=0.72, relheight=0.65)
        # Divisao 3
        self.divisao3 = Frame(self.principal, bd=4, bg='white', highlightbackground='#00374D', highlightthickness=2 )
        self.divisao3.place(relx=0.25, rely=0.71 ,relwidth=0.72, relheight=0.24)
    # Inserção de botões referentes a estrutura do carro na divisão 1 da tela principal
    def botoesDiv1(self):
        # Botão Frente
        self.botaoFrente = Button(self.divisao1, text='Frente', command=lambda: self.exibirImagem('C:/Users/flame/OneDrive/Área de Trabalho/Cursos/Meus Projetos/Meu Kwid/Projeto-MeuKwid/imagens/kwidfrente.png'))
        self.botaoFrente.place(relx=0.06, rely=0.03, relwidth=.9, relheight=.05)
        # Botão Lado
        self.botaoLado = Button(self.divisao1, text='Lateral', command=lambda: self.exibirImagem('C:/Users/flame/OneDrive/Área de Trabalho/Cursos/Meus Projetos/Meu Kwid/Projeto-MeuKwid/imagens/kwidlado.png') )
        self.botaoLado.place(relx=0.06, rely=0.1, relwidth=.9, relheight=.05)
        # Botão Traseira
        self.botaTraseira = Button(self.divisao1, text='Traseira', command=lambda: self.exibirImagem('C:/Users/flame/OneDrive/Área de Trabalho/Cursos/Meus Projetos/Meu Kwid/Projeto-MeuKwid/imagens/kwidtras.png'))
        self.botaTraseira.place(relx=0.06, rely=0.17, relwidth=.9, relheight=.05)
        # Botão Inferior
        self.botaoInfeiror = Button(self.divisao1, text='Inferior')
        self.botaoInfeiror.place(relx=0.06, rely=0.24, relwidth=.9, relheight=.05)
        # Botão Interno
        self.botaoInterno = Button(self.divisao1, text='Interior')
        self.botaoInterno.place(relx=0.06, rely=0.31, relwidth=.9, relheight=.05)

    # Função para exibir a imagem
    def exibirImagem(self, imagem):
        # Carrega a imagem
        self.imagem = imagem
        imagem = Image.open(self.imagem) 
        # Redimensiona a imagem para caber na divisao2
        largura, altura = 525, 392
        imagem = imagem.resize((largura, altura), Image.ANTIALIAS)
        # Cria um objeto de imagem Tkinter
        imagem_tk = ImageTk.PhotoImage(imagem)
        # Cria um label para exibir a imagem
        label_imagem = Label(self.divisao2, image=imagem_tk)
        label_imagem.image = imagem_tk  # Mantém uma referência para a imagem
        label_imagem.place(relx=0.12, rely=0)

App()