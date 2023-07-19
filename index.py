from tkinter import *
from PIL import ImageTk, Image

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
        self.divisao4 = Label(self.divisao4, text="", bg='white')
        self.divisao4.pack()
        # Divisao 5
        self.divisao5 = Frame(self.principal, bd=4, background='white', highlightbackground='#00374D', highlightthickness=2 )
        self.divisao5.place(relx=0.67, rely=0.71, relwidth= 0.3, relheight=0.24)

        # Inserção de botões referentes a estrutura do carro na divisão 1 da tela principal
    def botoesDiv1(self):
        # Caixa de Número e Botão para informar, armazenar e exibir a quilometragem atual do carro
        self.kmrodado = Label(self.divisao1, text='Quilometragem do Kwid:', bg='#007CAD', fg='white')
        self.kmrodado.place(relx=0.06, rely=0.01)
        self.km = Entry(self.divisao1)
        self.km.place(relx=0.06, rely=0.05, width= 100)
        self.confKm = Button(self.divisao1, text='OK', command=self.exibirkm)
        self.confKm.place(relx=0.62, rely=0.05, width= 64, height=21)
        # Título do menu
        self.menu = Label(self.divisao1, text='Partes do Carro:',font=10, fg="white", bg='#007CAD',bd=4, highlightbackground='white', highlightthickness=1, width=14)
        self.menu.place(relx=0.06, rely=0.18)
        # Botão Frente
        self.botaoFrente = Button(self.divisao1, text='Frente', command=lambda: self.botaoPress(self.destruirWidgets(), self.exibirImagem('C:/Users/flame/OneDrive/Área de Trabalho/Cursos/Meus Projetos/Meu Kwid/Projeto-MeuKwid/imagens/kwidfrente.png'), self.listas(frente=True, lado=False, tras=False, interno=False)))
        self.botaoFrente.place(relx=0.06, rely=0.27, relwidth=.9, relheight=.05)
        # Botão Lado
        self.botaoLado = Button(self.divisao1, text='Lateral', command=lambda: self.botaoPress(self.destruirWidgets(), self.exibirImagem('C:/Users/flame/OneDrive/Área de Trabalho/Cursos/Meus Projetos/Meu Kwid/Projeto-MeuKwid/imagens/kwidlado.png'), self.listas(frente=False, lado=True, tras=False, interno=False)))
        self.botaoLado.place(relx=0.06, rely=0.34, relwidth=.9, relheight=.05)
        # Botão Traseira
        self.botaTraseira = Button(self.divisao1, text='Traseira', command=lambda: self.botaoPress(self.destruirWidgets(), self.exibirImagem('C:/Users/flame/OneDrive/Área de Trabalho/Cursos/Meus Projetos/Meu Kwid/Projeto-MeuKwid/imagens/kwidtras.png'), self.listas(frente=False, lado=False, tras=True, interno=False)))
        self.botaTraseira.place(relx=0.06, rely=0.41, relwidth=.9, relheight=.05)
        # Botão Interno
        self.botaoInterno = Button(self.divisao1, text='Interior', command=lambda: self.botaoPress(self.destruirWidgets(), self.exibirImagem('C:/Users/flame/OneDrive/Área de Trabalho/Cursos/Meus Projetos/Meu Kwid/Projeto-MeuKwid/imagens/kwidinterno.png'), self.listas(frente=False, lado=False, tras=False, interno=True)))
        self.botaoInterno.place(relx=0.06, rely=0.48, relwidth=.9, relheight=.05)
    
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
        itensFrente = ['Atuador', 'Bateria', 'Bomba Dágua', 'Caixa de Marcha', 'Cabeçote', 'Cilindro Mestre', 'Coluna de Direção', 'Coxim Direito', 'Coxim Esquerdo', 'Coxim Calço', 'Cruzetas', 'Disco Embreagem', 'Embreagem', 'Fluído de Freio', 'Motor', 'Óleo Motor', 'Parachoque', 'Platô', 'Vidro Frontal', 'Limpador de P.Brisas', 'Radiador', 'Reservatório de Água', 'Rolamento Embreagem', 'Setor de Direção', 'Servo Freio', 'Túlipa', 'Trizeta', 'Velas']

        itensLado = ['Amortecedor', 'Amortecedor Traseiro', 'Balança', 'Batente', 'Coxim Amortecedor', 'Catalizador', 'Porta', 'Porta Traseira', 'Pneu', 'Mola', 'Mola Traseira', 'Rolamento Amortecedor', 'Rolamento Roda', 'Roda', 'Vidro', 'Vidro Traseiro', 'Maçaneta', 'Maçaneta Traseira']

        itensTras = [ 'Cano de Descarga', 'Faról', 'Lâmpada de Farol', 'Limpador de P. Brisas', 'Parachoque', 'Porta-Mala', 'Vidro', 'Luz de Freio']
        itensInterno = ['Banco', 'Banco Traseiro', 'Câmbio', 'Maçaneta', 'Maçaneta Traseira', 'Pedal Acelerador', 'Pedal Embreagem', 'Pedal Freio', 'Volante' ]

        # Eventos para atribuir informções ao item selecionado na lista
        def selecionarItemFrente (event):
            # Obtém o item selecionado na lista
            itemSelecionado = lista.get(lista.curselection())
            # Verifica os itens selecionados
            itens100 = list(filter(lambda x: x in ['Atuador', 'Embreagem', 'Rolamento Embreagem', 'Platô', "Disco Embreagem", 'Servo Freio', 'Cilindro Mestre'], itensFrente))
            itens50 = list(filter(lambda y: y in ["Bomba Dágua", "Túlipa", "Trizeta"], itensFrente))
            itensIndeterminados = list(filter(lambda z: z in['Caixa de Marcha','Vidro Frontal', 'Radiador', 'Motor', 'Parachoque', 'Cabeçote','Coluna de Direção','Cruzetas','Reservatório de Água'], itensFrente))
            itens30 = list(filter(lambda u: u in ['Coxim Direito', 'Coxim Esquerdo', 'Coxim Calço', 'Limpador de P.Brisas'], itensFrente))
            if itemSelecionado in itens100:
                self.destruirWidgets4()
                # Atualiza o texto na divisão 4
                self.divisao4.config(text="Tempo de vida: 100 mil km")
            elif itemSelecionado == 'Bateria' or itemSelecionado == 'Fluído de Freio':
                self.destruirWidgets4()
                self.divisao4.config(text='Tempo de vida: 2 anos')
            elif itemSelecionado in itens50:
                self.destruirWidgets4()
                self.divisao4.config(text="Tempo de vida: 50 mil km")
            elif itemSelecionado in itensIndeterminados:
                self.destruirWidgets4()
                self.divisao4.config(text="Esse componente não possui \n tempo de vida útil determinado.\n Por favor, faça revisões e tome\n devidos cuidados")
            elif itemSelecionado in itens30:
                self.destruirWidgets4()
                self.divisao4.config(text=' Tempo de vida: 30 mil km')
            elif itemSelecionado == 'Velas':
                self.destruirWidgets4()
                self.divisao4.config(text=' Tempo de vida: 20 mil km')
            elif itemSelecionado == 'Óleo Motor':
                self.destruirWidgets4()
                self.divisao4.config(text=' Tempo de vida: 10 mil km\n ou 6 meses de uso')
            elif itemSelecionado == 'Setor de Direção':
                self.destruirWidgets4()
                self.divisao4.config(text='Faça revisões periodicamente')
    
        def selecionarItensLado (event):
            itemSelecionado = lista.get(lista.curselection())
            itens3070 = list(filter(lambda u: u in ['Amortecedor', 'Amortecedor Traseiro',], itensLado))
            itens50 = list(filter(lambda v: v in ['Balança','Rolamento Roda'], itensLado))
            itensIndeterminados = list(filter(lambda x: x in ['Batente', 'Coxim Amortecedor', 'Catalisador', 'Porta', 'Porta Traseira', 'Mola', 'Mola Traseira', 'Rolamento Amortecedor', 'Roda', 'Vidro', 'Vidro Traseiro', 'Maçaneta', 'Maçaneta Traseira'], itensLado))
            if itemSelecionado in itens3070:
                self.destruirWidgets4()
                self.divisao4.config(text='Tempo de vida: de 30 mil a 70 mil km')
            elif itemSelecionado in itens50:
                self.destruirWidgets4()
                self.divisao4.config(text = 'Tempo de vida: 50 mil km')
            elif itemSelecionado in itensIndeterminados:
                self.destruirWidgets4()
                self.divisao4.config(text='Esse componente não possui \n tempo de vida útil determinado.\n Por favor, faça revisões e tome\n devidos cuidados')
            elif itemSelecionado == 'Pneu':
                self.destruirWidgets4()
                self.divisao4.config(text='Esse componente pode durar\n de 8 meses a 1 ano em boas condições de\n uso, sendo feitos os rodízios')  
        
        def selecionarItemtras(event):
            itemSelecionado = lista.get(lista.curselection())
            itensIndeterminados = list(filter(lambda x: x in ['Cano de Descarga', 'Faról', 'Lâmpada de Farol', 'Limpador de P. Brisas', 'Parachoque', 'Porta-Mala', 'Vidro', 'Luz de Freio'], itensTras))
            if itemSelecionado in itensIndeterminados:
                self.destruirWidgets4()
                self.divisao4.config(text='Esse componente não possui \n tempo de vida útil determinado.\n Por favor, faça revisões e tome\n devidos cuidados')

        def selecionarItemInterno (event):
            itemSelecionado = lista.get(lista.curselection())
            itensIndeterminados = list(filter(lambda x: x in ['Banco', 'Banco Traseiro', 'Câmbio', 'Maçaneta', 'Maçaneta Traseira', 'Pedal Acelerador', 'Pedal Embreagem', 'Pedal Freio', 'Volante'], itensInterno))
            if itemSelecionado in itensIndeterminados:
                self.destruirWidgets4()
                self.divisao4.config(text='Esse componente não possui \n tempo de vida útil determinado.\n Por favor, faça revisões e tome\n devidos cuidados')
                        
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
    
    # Função para exibir e armazenar a quilometragem digitada no Label da divisao1
    def exibirkm(self):
       
        quantQuilometro = Label(self.divisao1,font=1, fg="white", bg='#007CAD', text=self.km.get()+' KMs', bd=4, highlightbackground='white', highlightthickness=1)
        quantQuilometro.place(relx=0.06, rely=0.10, width= 165)
App()
