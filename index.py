from tkinter import *
from tkinter import messagebox
import tkinter as tk
import psycopg2
from PIL import ImageTk, Image

#abrindo conexão com o banco de dados
conn = psycopg2.connect(
    dbname = 'meukwid',
    user = 'postgres',
    password = '4456',
    host = 'localhost',
    port = '5432'
)

cursor = conn.cursor()


principal = Tk()

class App():
    def __init__(self):
        self.principal = principal
        self.tela()
        self.divisaoTela()
        self.botoesDiv1()
        self.destruirWidgets()
        principal.mainloop()
        

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
        # Caixa de Número e Botão para informar, armazenar e exibir a quilometragem atual do carro
        self.kmrodado = Label(self.divisao1,font=('Arial', 10), text='Quilometragem do Kwid:', bg='#007CAD', fg='white',bd=4, highlightbackground='white', highlightthickness=1, width=19)
        self.kmrodado.place(relx=0.06, rely=0.01)
        self.km = Entry(self.divisao1)
        self.km.place(relx=0.06, rely=0.07, width= 100)
        self.confKm = Button(self.divisao1, text='OK', command=self.exibirkm)
        self.confKm.place(relx=0.62, rely=0.07, width= 64, height=21)
        # Título do menu
        self.menu = Label(self.divisao1, text='Partes do Carro:',font=('Arial', 10), fg="white", bg='#007CAD',bd=4, highlightbackground='white', highlightthickness=1, width=19)
        self.menu.place(relx=0.06, rely=0.17)
        # Botão Frente
        self.botaoFrente = Button(self.divisao1, font=('Arial', 10), text='Frente', command=lambda: self.botaoPress(self.destruirWidgets(), self.exibirImagem('C:/Users/flame/OneDrive/Área de Trabalho/Cursos/Meus Projetos/Meu Kwid/Projeto-MeuKwid/imagens/kwidfrente.png'), self.listas(frente=True, lado=False, tras=False, interno=False)))
        self.botaoFrente.place(relx=0.06, rely=0.24, relwidth=.9, relheight=.05)
        # Botão Lado
        self.botaoLado = Button(self.divisao1, font=('Arial', 10), text='Lateral', command=lambda: self.botaoPress(self.destruirWidgets(), self.exibirImagem('C:/Users/flame/OneDrive/Área de Trabalho/Cursos/Meus Projetos/Meu Kwid/Projeto-MeuKwid/imagens/kwidlado.png'), self.listas(frente=False, lado=True, tras=False, interno=False)))
        self.botaoLado.place(relx=0.06, rely=0.31, relwidth=.9, relheight=.05)
        # Botão Traseira
        self.botaTraseira = Button(self.divisao1, font=('Arial', 10), text='Traseira', command=lambda: self.botaoPress(self.destruirWidgets(), self.exibirImagem('C:/Users/flame/OneDrive/Área de Trabalho/Cursos/Meus Projetos/Meu Kwid/Projeto-MeuKwid/imagens/kwidtras.png'), self.listas(frente=False, lado=False, tras=True, interno=False)))
        self.botaTraseira.place(relx=0.06, rely=0.38, relwidth=.9, relheight=.05)
        # Botão Interno
        self.botaoInterno = Button(self.divisao1, font=('Arial', 10), text='Interior', command=lambda: self.botaoPress(self.destruirWidgets(), self.exibirImagem('C:/Users/flame/OneDrive/Área de Trabalho/Cursos/Meus Projetos/Meu Kwid/Projeto-MeuKwid/imagens/kwidinterno.png'), self.listas(frente=False, lado=False, tras=False, interno=True)))
        self.botaoInterno.place(relx=0.06, rely=0.45, relwidth=.9, relheight=.05)

        # Função para exibir e armazenar a quilometragem digitada no Label da divisao1
    def exibirkm(self):
        quantQuilometro = Label(self.divisao1,font=('Arial', 10), fg="white", bg='#007CAD', text=self.km.get()+' KMs', bd=4, highlightbackground='white', highlightthickness=1)
        quantQuilometro.place(relx=0.06, rely=0.11, width= 165)

        #pegar a quilometragem colhida no botao da divisao1 e armazenar num banco de dados
        quilometragem = self.km.get()
        cursor.execute(" update quilometragem set kmrodado = %s", (quilometragem,))
        conn.commit()
        conn.close()
    
    # Função ao pressionar botões
    def botaoPress(self, wid, img, lists):
        wid
        img
        lists
    
    # Função para destruir widgets
    def destruirWidgets(self):
        for widget in self.divisao3.winfo_children():
            widget.destroy()
    
    def destruirWidgets4(self):
        for widget in self.divisao4.winfo_children():
            widget.destroy()

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
    def listas (self, frente, lado, tras, interno):
        lista = Listbox(self.divisao3)
        # Adicionando barra de rolagem a lista
        barraRolagem = Scrollbar(self.divisao3)
        barraRolagem.pack(side=RIGHT, fill=Y)
        barraRolagem.config(command=lista.yview)
        lista.config(yscrollcommand=barraRolagem.set)
        itensFrente = {'Atuador': 100000, 'Cilindro Mestre':100000,'Disco Embreagem':100000, 'Embreagem':100000,'Platô':100000,'Rolamento Embreagem':100000,'Servo Freio':100000, 'Bomba Dágua':50000,'Túlipa':50000, 'Trizeta':5000, 'Caixa de Marcha':0, 'Cabeçote':0,'Coluna de Direção':0, 'Radiador':0, 'Reservatório de Água':0,'Cruzetas':0,'Motor':0, 'Parachoque':0,'Vidro Frontal':0,'Fluído de Freio':0, 'Limpador de P.Brisas': 30000, 'Coxim Direito':30000, 'Coxim Esquerdo':30000, 'Coxim Calço':30000, 'Bateria':1, 'Óleo Motor': 2, 'Setor de Direção': 3, 'Velas':4}

        itensLado = {'Amortecedor':30000, 'Amortecedor Traseiro':30000, 'Balança':50000,'Rolamento Roda':50000, 'Batente':0, 'Coxim Amortecedor':0, 'Catalizador':0, 'Porta':0, 'Porta Traseira':0, 'Pneu':0, 'Mola':0, 'Mola Traseira':0, 'Rolamento Amortecedor':0,  'Roda':0, 'Vidro':0, 'Vidro Traseiro':0, 'Maçaneta':0, 'Maçaneta Traseira':0}

        itensTras =  {'Cano de Descarga':0, 'Faról':0, 'Lâmpada de Farol':0, 'Limpador de P. Brisas':0, 'Parachoque':0, 'Porta-Mala':0, 'Vidro':0, 'Luz de Freio':0,}
        itensInterno = {'Banco':0, 'Banco Traseiro':0, 'Câmbio':0, 'Maçaneta':0, 'Maçaneta Traseira':0, 'Pedal Acelerador':0, 'Pedal Embreagem':0, 'Pedal Freio':0, 'Volante':0}
        
        # Eventos para atribuir informções ao item selecionado na lista
        def selecionarItemFrente (event):
                # Obtém o índice do item selecionado na lista
            indiceSelecionado = lista.curselection()[0]
            # Obtém o valor correspondente ao índice obtido acima
            valorSelecionado = itensFrente[list(itensFrente.keys())[indiceSelecionado]]

            #armazenando os valores das ultimas trocas das peças 
            cursor = conn.cursor()
            cursor.execute("create table if not exists itensFrente (nome varchar, basekm int)")
            conn.commit()
            for item, km in itensFrente.items():
                cursor.execute("insert into itensFrente (nome, basekm) values (%s, %s)", (item, km))
                conn.commit()

            if valorSelecionado == 100000:
                self.destruirWidgets4()
                div4 = Label(self.divisao4, text= 'Tempo de vida: 100.000 KM', bg='white', font = ('Arial', 10))
                div4.place(relx=.10, rely=.05)
                self.ultimaTroca()
            elif valorSelecionado == 50000:
                self.destruirWidgets4()
                div4 = Label(self.divisao4, text= 'Tempo de vida: 50.000 KM', bg='white', font = ('Arial', 10))
                div4.place(relx=.10, rely=.05)
                self.ultimaTroca()
            elif valorSelecionado == 30000:
                self.destruirWidgets4()
                div4 = Label(self.divisao4, text= 'Tempo de vida: 30.000 KM', bg='white', font = ('Arial', 10))
                div4.place(relx=.10, rely=.05)
                self.ultimaTroca()
            elif valorSelecionado == 0:
                self.destruirWidgets4()
                div4 = Label(self.divisao4, text= 'Tempo de vida indeterminado.\nFaça revisões constantemente\n no componente', bg='white', font = ('Arial', 10))
                div4.place(relx=.10, rely=.05)
                self.ultimaTroca()
            elif valorSelecionado == 1:
                self.destruirWidgets4()
                div4 = Label(self.divisao4, text= 'Tempo de vida: 2 anos', bg='white', font = ('Arial', 10))
                div4.place(relx=.10, rely=.05)
                self.ultimaTroca()
            elif valorSelecionado == 2:
                self.destruirWidgets4()
                div4 = Label(self.divisao4, text= 'Tempo de vida: 10.000 KM ou \n 6 meses de uso', bg='white', font = ('Arial', 10))
                div4.place(relx=.10, rely=.05)
                self.ultimaTroca()
            elif valorSelecionado == 3:
                self.destruirWidgets4()
                div4 = Label(self.divisao4, text= 'Faça revisões no componente\n a cada 20.000 KM',bg='white', font = ('Arial', 10))
                div4.place(relx=.10, rely=.05)
                self.ultimaTroca()
            elif valorSelecionado == 4:
                self.destruirWidgets4()
                div4 = Label(self.divisao4, text= 'Tempo de vida: 20.000 KM', bg='white', font = ('Arial', 10))
                div4.place(relx=.10, rely=.05)
                self.ultimaTroca()

    
        '''def selecionarItensLado (event):
            itemSelecionado = lista.get(lista.curselection())
            itens3070 = list(filter(lambda u: u in ['Amortecedor', 'Amortecedor Traseiro',], itensLado))
            itens50 = list(filter(lambda v: v in ['Balança','Rolamento Roda'], itensLado))
            itensIndeterminados = list(filter(lambda x: x in ['Batente', 'Coxim Amortecedor', 'Catalisador', 'Porta', 'Porta Traseira', 'Mola', 'Mola Traseira', 'Rolamento Amortecedor', 'Roda', 'Vidro', 'Vidro Traseiro', 'Maçaneta', 'Maçaneta Traseira'], itensLado))
            if itemSelecionado in itens3070:
                self.destruirWidgets4()
                self.ultimaTroca(tempo=Label(self.divisao4, text=f'Tempo de vida: 70000 km', bg='white', font=('Arial', 10)))
            elif itemSelecionado in itens50:
                self.destruirWidgets4()
                self.ultimaTroca(tempo=Label(self.divisao4, text=f'Tempo de vida: 50000 km', bg='white', font=('Arial', 10)))
            elif itemSelecionado in itensIndeterminados:
                self.destruirWidgets4()
                self.ultimaTroca(tempo=Label(self.divisao4, text='Tempo de vida: indeterminado.\n Cuide do componente!', bg='white', font=('Arial', 10)))
            elif itemSelecionado == 'Pneu':
                self.destruirWidgets4()
                self.ultimaTroca(tempo=Label(self.divisao4, text='Tempo de vida: 5 anos,\n ou até atingir a marca do Inmetro', bg='white', font=('Arial', 10)))
        
        def selecionarItemtras(event):
            itemSelecionado = lista.get(lista.curselection())
            itensIndeterminados = list(filter(lambda x: x in ['Cano de Descarga', 'Faról', 'Lâmpada de Farol', 'Limpador de P. Brisas', 'Parachoque', 'Porta-Mala', 'Vidro', 'Luz de Freio'], itensTras))
            if itemSelecionado in itensIndeterminados:
                self.destruirWidgets4()
                self.ultimaTroca(tempo=Label(self.divisao4, text='Tempo de vida: indeterminado.\n Cuide do componente!', bg='white', font=('Arial', 10)))

        def selecionarItemInterno (event):
            itemSelecionado = lista.get(lista.curselection())
            itensIndeterminados = list(filter(lambda x: x in ['Banco', 'Banco Traseiro', 'Câmbio', 'Maçaneta', 'Maçaneta Traseira', 'Pedal Acelerador', 'Pedal Embreagem', 'Pedal Freio', 'Volante'], itensInterno))
            if itemSelecionado in itensIndeterminados:
                self.destruirWidgets4()
                self.ultimaTroca(tempo=Label(self.divisao4, text='Tempo de vida: indeterminado.\n Cuide do componente!', bg='white', font=('Arial', 10)))'''
                        
        # Verifica qual lista será exibida ao pressionar os botões equivalentes na GUI
        if frente == True:
            for itens in itensFrente:
                lista.insert(END, itens)
            lista.pack()
            lista.bind("<<ListboxSelect>>", selecionarItemFrente)
        elif lado == True:
            for itens in itensLado:
                lista.insert(END, itens)
            lista.pack()
            lista.bind("<<ListboxSelect>>", selecionarItensLado)
        elif tras == True:
            for itens in itensTras:
                lista.insert(END, itens)
            lista.pack()
            lista.bind("<<ListboxSelect>>", selecionarItemtras)
        elif interno == True:
            for itens in itensInterno:
                lista.insert(END, itens)
            lista.pack()
            lista.bind("<<ListboxSelect>>", selecionarItemInterno)
    
    # Pergunta sobre quando foi a íltima vez que o componente foi trocado
    def ultimaTroca(self, tempo = Label()):
        tempo.place(relx=0.10, rely=0.05)
        pergunta = Label(self.divisao4, text='Em quantos km ocorreu\n a última troca?', font=('Arial', 10), bg='white')
        pergunta.place(relx=0.11, rely=0.40)
        self.kilom = Entry(self.divisao4, width=10, bg='light gray',)
        self.kilom.place(relx=.13, rely=.68)
        botao = Button(self.divisao4, text='Checar:', height=1, command=self.checar)
        botao.place(relx=.4, rely=0.65)
    
    def checar(self):
        ultimaT = self.kilom.get()
        cursor = conn.cursor ()
        cursor.execute("update itensfrente set ultimaT = %s", (ultimaT,))
        conn.commit()
        conn.close()
        
        # Função para calcular os kms para a troca do componente + um aviso se já estiver na hora de trocar o component

    def alerta(self):
        messagebox.showinfo('Mensagem do Sistema','Já está na hora de trocar o componente!')

App()
