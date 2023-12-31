from tkinter import *
from PIL import ImageTk, Image

# Criando a estrutura mestre do app
class MeuKwid():
    def __init__(self):
        self.telaPrincipal = TelaPrincipal()

# Criando a estrutura da tela principal
class TelaPrincipal():
    def __init__(self):
        self.tela = Tk()
        self.tela.title('Meu Kwid')
        self.tela.geometry('980x640')
        self.tela.resizable('False', 'False')
        self.tela.config(background='#004D6B')
        self.divisoes = DivisoesTela(self.tela)
        self.tela.mainloop()

# Divisões da Tela e os metódos relacionados
class DivisoesTela():
    def __init__(self, tela):
        # Divisao 1
        self.divisao1 = Frame(tela, bd=1, bg='#007CAD', highlightbackground='#00374D', highlightthickness=1)
        self.divisao1.place(relx=0.02, rely=0.05, relwidth=0.2, relheight=0.9)
        # Divisao 2
        self.divisao2 = Frame(tela, bd=4, bg='white', highlightbackground='#00374D', highlightthickness=2)
        self.divisao2.place(relx=0.25, rely=0.05, relwidth=0.72, relheight=0.65)
        # Divisao 3
        self.divisao3 = Frame(tela, bd=4, bg='white', highlightbackground='#00374D', highlightthickness=2 )
        self.divisao3.place(relx=0.25, rely=0.71 ,relwidth=0.15, relheight=0.24)
        # Divisao 4
        self.divisao4 = Frame(tela, bd=4, bg='white', highlightbackground='#00374D', highlightthickness=2)
        self.divisao4.place(relx=.405, rely=0.71, relwidth=0.26, relheight=0.24)
        # Divisao 5
        self.divisao5 = Frame(tela, bd=4, background='white', highlightbackground='#00374D', highlightthickness=2 )
        self.divisao5.place(relx=0.67, rely=0.71, relwidth= 0.3, relheight=0.24)
        self.botoesDiv1 = self.BotoesDiv1()    

    def BotoesDiv1(self):
        # Caixa de Número e Botão para informar, armazenar e exibir a quilometragem atual do carro
        self.kmrodado = Label(self.divisao1, font=('Arial', 10), text='Quilometragem do Kwid:', bg='#007CAD', fg='white',bd=4, highlightbackground='white', highlightthickness=1, width=19)
        self.kmrodado.place(relx=0.06, rely=0.01)
        self.km = Entry(self.divisao1)
        self.km.place(relx=0.06, rely=0.07, width= 100)
        self.confKm = Button(self.divisao1, text='OK')
        self.confKm.place(relx=0.62, rely=0.07, width= 64, height=21)
        # Título do menu
        self.menu = Label(self.divisao1, text='Partes do Carro:',font=('Arial', 10), fg="white", bg='#007CAD',bd=4, highlightbackground='white', highlightthickness=1, width=19)
        self.menu.place(relx=0.06, rely=0.17)
        # Botão Frente
        self.botaoFrente = Button(self.divisao1, font=('Arial', 10), text='Frente', command= lambda: self.botaoPress(self.exibirImagem('C:/Users/flame/OneDrive/Área de Trabalho/Cursos/Meus Projetos/Meu Kwid/Projeto-MeuKwid/imagens/kwidfrente.png'), self.exibirLista()))
        self.botaoFrente.place(relx=0.06, rely=0.24, relwidth=.9, relheight=.05)
        # Botão Lado
        self.botaoLado = Button(self.divisao1, font=('Arial', 10), text='Lateral', command= lambda: self.exibirImagem('C:/Users/flame/OneDrive/Área de Trabalho/Cursos/Meus Projetos/Meu Kwid/Projeto-MeuKwid/imagens/kwidlado.png'))
        self.botaoLado.place(relx=0.06, rely=0.31, relwidth=.9, relheight=.05)
        # Botão Traseira
        self.botaTraseira = Button(self.divisao1, font=('Arial', 10), text='Traseira', command= lambda: self.exibirImagem('C:/Users/flame/OneDrive/Área de Trabalho/Cursos/Meus Projetos/Meu Kwid/Projeto-MeuKwid/imagens/kwidtras.png'))
        self.botaTraseira.place(relx=0.06, rely=0.38, relwidth=.9, relheight=.05)
        # Botão Interno
        self.botaoInterno = Button(self.divisao1, font=('Arial', 10), text= 'Interno', command= lambda: self.exibirImagem('C:/Users/flame/OneDrive/Área de Trabalho/Cursos/Meus Projetos/Meu Kwid/Projeto-MeuKwid/imagens/kwidinterno.png'))
        self.botaoInterno.place(relx=0.06, rely=0.45, relwidth=.9, relheight=.05)

    def botaoPress(self, img, lista):
        self.img = img
        self.lista = lista
        
    
    def exibirLista(self, frente, lado, tras, interno):
        self.frente = frente
        self.lado = lado
        self.tras = tras
        self.interno = interno
        lista = Lista()
        frente = lista.frente
        

        # Função para exibir a imagem
    def exibirImagem(self, imagem):
        # Carrega a imagem
        self.imagem = imagem
        imagem = Image.open(self.imagem)
        largura, altura = 690, 388
        imagem = imagem.resize((largura, altura))
        # Converter a imagem para Tkinter
        imagem_tk = ImageTk.PhotoImage(imagem)
        label_imagem = Label(self.divisao2, image=imagem_tk)
        label_imagem.place(relx=0, rely=0.015)
        label_imagem.image = imagem_tk 

class Lista():
    def __init__(self):
        lista = Listbox(div3)
        barraRolagem = Scrollbar(div3)
        barraRolagem.pack(side=RIGHT, fill=Y)
        barraRolagem.config(command=lista.yview)
        lista.config(yscrollcommand=barraRolagem.set)
        divisoesTela = DivisoesTela()
        div3 = divisoesTela.divisao3
        self.frente = frente
        frente = {'Atuador': 100000, 'Cilindro Mestre':100000,'Disco Embreagem':100000, 'Embreagem':100000,'Platô':100000,'Rolamento Embreagem':100000,'Servo Freio':100000, 'Bomba Dágua':50000,'Túlipa':50000, 'Trizeta':5000, 'Caixa de Marcha':0, 'Cabeçote':0,'Coluna de Direção':0, 'Radiador':0, 'Reservatório de Água':0,'Cruzetas':0,'Motor':0, 'Parachoque':0,'Vidro Frontal':0,'Fluído de Freio':0, 'Limpador de P.Brisas': 30000, 'Coxim Direito':30000, 'Coxim Esquerdo':30000, 'Coxim Calço':30000, 'Bateria':1, 'Óleo Motor': 2, 'Setor de Direção': 3, 'Velas':4}
    
MeuKwid()