from tkinter import *

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Inserir números")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.nomeLabel = Label(self.segundoContainer,text="Número 01", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)

        self.numero01 = Entry(self.segundoContainer)
        self.numero01["width"] = 30
        self.numero01["font"] = self.fontePadrao
        self.numero01.pack(side=LEFT)

        self.numero01Label = Label(self.terceiroContainer, text="Número 02", font=self.fontePadrao)
        self.numero01Label.pack(side=LEFT)

        self.numero02 = Entry(self.terceiroContainer)
        self.numero02["width"] = 30
        self.numero02["font"] = self.fontePadrao        
        self.numero02.pack(side=LEFT)

        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Imprimir"
        self.autenticar["font"] = ("Calibri", "12")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.validacaonumeros
        self.autenticar.pack()

        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

    #Método verificar numeros
    def validacaonumeros(self):
        numero01 = self.numero01.get()
        numero02 = self.numero02.get()
        if numero01 > numero02:
            resultado = "O número 1 é  maior que o número 2 ==> " + str(numero01)
        elif numero01 == numero02:
            resultado = "Os números são iguais"            
        else:
            resultado = "O número 1 é  menor que o numero 2 ==> " + str(numero02)            
        self.mensagem["text"] = resultado


root = Tk()
Application(root)
root.mainloop()
