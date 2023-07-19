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
        # Botão Frente
        self.botaoFrente = Button(self.divisao1, text='Frente', command=lambda: self.botaoPress(self.destruirWidgets(), self.exibirImagem('C:/Users/flame/OneDrive/Área de Trabalho/Cursos/Meus Projetos/Meu Kwid/Projeto-MeuKwid/imagens/kwidfrente.png'), self.listas(frente=True, lado=False, tras=False, interno=False)))
        self.botaoFrente.place(relx=0.06, rely=0.03, relwidth=.9, relheight=.05)
        # Botão Lado
        self.botaoLado = Button(self.divisao1, text='Lateral', command=lambda: self.botaoPress(self.destruirWidgets(), self.exibirImagem('C:/Users/flame/OneDrive/Área de Trabalho/Cursos/Meus Projetos/Meu Kwid/Projeto-MeuKwid/imagens/kwidlado.png'), self.listas(frente=False, lado=True, tras=False, interno=False)))
        self.botaoLado.place(relx=0.06, rely=0.1, relwidth=.9, relheight=.05)
        # Botão Traseira
        self.botaTraseira = Button(self.divisao1, text='Traseira', command=lambda: self.botaoPress(self.destruirWidgets(), self.exibirImagem('C:/Users/flame/OneDrive/Área de Trabalho/Cursos/Meus Projetos/Meu Kwid/Projeto-MeuKwid/imagens/kwidtras.png'), self.listas(frente=False, lado=False, tras=True, interno=False)))
        self.botaTraseira.place(relx=0.06, rely=0.17, relwidth=.9, relheight=.05)
        # Botão Interno
        self.botaoInterno = Button(self.divisao1, text='Interior', command=lambda: self.botaoPress(self.destruirWidgets(), self.exibirImagem('C:/Users/flame/OneDrive/Área de Trabalho/Cursos/Meus Projetos/Meu Kwid/Projeto-MeuKwid/imagens/kwidinterno.png'), self.listas(frente=False, lado=False, tras=False, interno=True)))
        self.botaoInterno.place(relx=0.06, rely=0.24, relwidth=.9, relheight=.05)
    
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
        itensLado = ['Amortecedor', 'Amortecedor Traseiro', 'Balança', 'Batente', 'Coxim Amortecedor', 'Catalizador', 'Silencioso', 'Porta', 'Porta Traseira', 'Pneu', 'Mola', 'Mola Traseira', 'Rolamento Amortecedor', 'Rolamento Roda', 'Roda', 'Vidro', 'Vidro Traseiro', 'Maçaneta', 'Maçaneta Traseira']
        itensTras = [ 'Cano de Descarga', 'Faról', 'Lâmpada de Farol', 'Limpador de P. Brisas', 'Parachoque', 'Porta-Mala', 'Vidro', 'Luz de Freio']
        itensInterno = ['Banco', 'Banco Traseiro', 'Câmbio', 'Maçaneta', 'Maçaneta Traseira', 'Pedal Acelerador', 'Pedal Embreagem', 'Pedal Freio', 'Volante' ]
        if frente == True:
            for itens in itensFrente:
                lista.insert(END, itens)
            lista.pack()
        elif lado == True:
            for itens in itensLado:
                lista.insert(END, itens)
            lista.pack()
        elif tras == True:
            for itens in itensTras:
                lista.insert(END, itens)
            lista.pack()
        elif interno == True:
            for itens in itensInterno:
                lista.insert(END, itens)
            lista.pack()
        # Evento para atribuir informções ao item selecionado na lista
        def selecionarItem(event):
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
            
            
        lista.bind("<<ListboxSelect>>", selecionarItem)

App()
