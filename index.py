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
        self.listaFrente()
        self.acaoBotaoFrente()
        self.listaLado()
        self.acaoBotaoLado()
        self.listaTras()
        self.acaoBotaoTras()
        self.listaInterno()
        self.acaoBotaoInterno()

    # Aspectos da tela principal
    def tela(self):
        self.principal.title('Meu Kwid')
        self.principal.configure(background='#004D6B')
        self.principal.geometry('980x640')
        self.principal.resizable(False, False)

    # Definindo as divisões da tela principal
    def divisaoTela(self):
        # Divisão 1
        self.divisao1 = Frame(self.principal, bd=4, bg='#007CAD', highlightbackground='#00374D', highlightthickness=2)
        self.divisao1.place(relx=0.02, rely=0.05, relwidth=0.2, relheight=0.9)
        # Divisao 2
        self.divisao2 = Frame(self.principal, bd=4, bg='white', highlightbackground='#00374D', highlightthickness=2)
        self.divisao2.place(relx=0.25, rely=0.05, relwidth=0.72, relheight=0.65)
        # Divisao 3
        self.divisao3 = Frame(self.principal, bd=4, bg='white', highlightbackground='#00374D', highlightthickness=2 )
        self.divisao3.place(relx=0.25, rely=0.71 ,relwidth=0.15, relheight=0.24)
        # Divisao 4
        self.divisao4 = Frame(self.principal, bd=4, bg='white', highlightbackground='#00374D', highlightthickness=2)
        self.divisao4.place(relx=.405, rely=0.71, relwidth=0.26, relheight=0.24)
        # Divisao 5
        self.divisao5 = Frame(self.principal, bd=4, background='white', highlightbackground='#00374D', highlightthickness=2 )
        self.divisao5.place(relx=0.67, rely=0.71, relwidth= 0.3, relheight=0.24)
        # Inserção de botões referentes a estrutura do carro na divisão 1 da tela principal
    def botoesDiv1(self):
        # Botão Frente
        self.botaoFrente = Button(self.divisao1, text='Frente', command=lambda: self.acaoBotaoFrente())
        self.botaoFrente.place(relx=0.06, rely=0.03, relwidth=.9, relheight=.05)
        # Botão Lado
        self.botaoLado = Button(self.divisao1, text='Lateral', command=lambda: self.acaoBotaoLado())
        self.botaoLado.place(relx=0.06, rely=0.1, relwidth=.9, relheight=.05)
        # Botão Traseira
        self.botaTraseira = Button(self.divisao1, text='Traseira', command=lambda: self.acaoBotaoTras())
        self.botaTraseira.place(relx=0.06, rely=0.17, relwidth=.9, relheight=.05)
        # Botão Interno
        self.botaoInterno = Button(self.divisao1, text='Interior', command=lambda: self.acaoBotaoInterno())
        self.botaoInterno.place(relx=0.06, rely=0.24, relwidth=.9, relheight=.05)
    
    # Ações do botão frente
    def acaoBotaoFrente(self):
        #limpando os widgets inicializados anteriormente
        for widget in self.divisao3.winfo_children():
            widget.destroy()
        self.exibirImagem('C:/Users/flame/OneDrive/Área de Trabalho/Cursos/Meus Projetos/Meu Kwid/Projeto-MeuKwid/imagens/kwidfrente.png')
        self.listaFrente()
    # Ações do botão lado
    def acaoBotaoLado(self):
        #limpando os widgets inicializados anteriormente
        for widget in self.divisao3.winfo_children():
            widget.destroy()
        self.exibirImagem('C:/Users/flame/OneDrive/Área de Trabalho/Cursos/Meus Projetos/Meu Kwid/Projeto-MeuKwid/imagens/kwidlado.png')
        self.listaLado()
    # Ações botão trás 
    def acaoBotaoTras(self):
        for widget in self.divisao3.winfo_children():
            widget.destroy()
        self.exibirImagem('C:/Users/flame/OneDrive/Área de Trabalho/Cursos/Meus Projetos/Meu Kwid/Projeto-MeuKwid/imagens/kwidtras.png')
        self.listaTras()
    # Ações botão interno
    def acaoBotaoInterno(self):
        for widgets in self.divisao3.winfo_children():
            widgets.destroy()
        self.exibirImagem('C:/Users/flame/OneDrive/Área de Trabalho/Cursos/Meus Projetos/Meu Kwid/Projeto-MeuKwid/imagens/kwidinterno.png')
        self.listaInterno()

    # Função para exibir a imagem
    def exibirImagem(self, imagem):
        # Carrega a imagem
        self.imagem = imagem
        imagem = Image.open(self.imagem)
        largura, altura = 750, 427
        imagem = imagem.resize((largura, altura))
        imagem_tk = ImageTk.PhotoImage(imagem)
        label_imagem = Label(self.divisao2, image=imagem_tk)
        label_imagem.image = imagem_tk 
        label_imagem.place(relx= -0.05, rely=-0.01)
        
    # Lista de itens por parte do carro
    # Frente
    def listaFrente (self):
        itensFrente = ['Atuador', 'Bateria', 'Bomba Dágua', 'Caixa de Marcha', 'Cabeçote', 'Cilindro Mestre', 'Coluna de Direção', 'Coxim Direito', 'Coxim Esquerdo', 'Coxim Calço', 'Coxim Amortecedor','Cruzetas', 'Disco Embreagem', 'Embreagem', 'Fluído de Freio', 'Motor', 'Óleo Motor', 'Parachoque', 'Para-brisa', 'Platô', 'Vidro Frontal', 'Limpador de P.Brisas', 'Radiador', 'Reservatório de Água', 'Rolamento Embreagem', 'Setor de Direção', 'Servo Freio', 'Túlipa', 'Trizeta', 'Velas']
        frente = Listbox(self.divisao3)
        # Adcionando barra de rolagem a lista
        barraRolagem = Scrollbar(self.divisao3)
        barraRolagem.pack(side=RIGHT, fill=Y)
        barraRolagem.config(command=frente.yview)
        frente.config(yscrollcommand=barraRolagem.set)
        for itens in itensFrente:
            frente.insert(END, itens)
        frente.pack()
    # Lado
    def listaLado(self):
        itensLado = ['Amortecedor', 'Amortecedor Traseiro', 'Balança', 'Batente', 'Coxim Amortecedor', 'Catalizador', 'Silencioso', 'Porta', 'Porta Traseira', 'Pneu', 'MOla', 'Mola Traseira', 'Rolamento Amortecedor', 'Rolamento Roda', 'Roda', 'Vidro', 'Vidro Traseiro', 'Maçaneta', 'Maçaneta Traseira']
        lado = Listbox(self.divisao3)
        barraRolagem = Scrollbar(self.divisao3)
        barraRolagem.pack(side=RIGHT, fill=Y)
        barraRolagem.config(command=lado.yview)
        lado.config(yscrollcommand=barraRolagem.set)
        for itens in itensLado:
            lado.insert(END, itens)
        lado.pack()
    # Traseira
    def listaTras(self):
        itensTras = [ 'Cano de Descarga', 'Faról', 'Lâmpada de Farol', 'Limpador de P. Brisas', 'Parachoque', 'Porta-Mala', 'Vidro', 'Luz de Freio']
        tras = Listbox(self.divisao3)
        barraRolagem = Scrollbar(self.divisao3)
        barraRolagem.pack(side=RIGHT, fill=Y)
        barraRolagem.config(command=tras.yview)
        tras.config(yscrollcommand=barraRolagem.set)
        for itens in itensTras:
            tras.insert(END, itens)
        tras.pack()
    # Interno
    def listaInterno(self):
        itensInterno = ['Banco', 'Banco Traseiro', 'Câmbio', 'Maçaneta', 'Maçaneta Traseira', 'Pedal Acelerador', 'Pedal Embreagem', 'Pedal Freio', 'Volante' ]
        interno = Listbox(self.divisao3)
        barraRolagem = Scrollbar(self.divisao3)
        barraRolagem.pack (side=RIGHT, fill=Y)
        barraRolagem.config(command=interno.yview)
        interno.config(yscrollcommand=barraRolagem.set)
        for itens in itensInterno:
            interno.insert(END, itens)
        interno.pack()

App()
