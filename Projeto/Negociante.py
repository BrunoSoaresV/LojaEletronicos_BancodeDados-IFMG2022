from tkinter import *
from Negoci import Negoci
if __name__ == "__main__":
    class Negociante:
        def __init__(self, master=None):
            self.fonte = ("Times New Roman", "12")
            self.first = Frame(master)
            self.first["pady"] = 10
            self.first.pack()

            self.second = Frame(master)
            self.second["padx"] = 20
            self.second.pack()

            self.third = Frame(master)
            self.third["padx"] = 20
            self.third.pack()


            self.fifth = Frame(master)
            self.fifth["padx"] = 20
            self.fifth.pack()

            self.sixth = Frame(master)
            self.sixth["padx"] = 20
            self.sixth.pack()

            self.seventh = Frame(master)
            self.seventh["padx"] = 20
            self.seventh.pack()

            self.twelfth = Frame(master)
            self.twelfth["padx"] = 20
            self.twelfth["pady"] = 20
            self.twelfth.pack()

            self.ponto = Frame(master)
            self.ponto["pady"] = 20
            self.ponto.pack()



            self.titulo = Label(self.first, text="                              Dados do negociante")
            self.titulo["font"] = ("Times New Roman", "12", "italic", "bold")
            self.titulo.pack()

            self.nome1= Label(self.second, text=" Nome                           ", font=self.fonte)
            self.nome1.pack(side=LEFT)
            self.nome1 = Entry(self.second)
            self.nome1["width"] = 30
            self.nome1["font"] = self.fonte
            self.nome1.pack(side=LEFT)

            self.email1 = Label(self.third, text=" Email                            ", font=self.fonte)
            self.email1.pack(side=LEFT)
            self.email1 = Entry(self.third)
            self.email1["width"] = 30
            self.email1["font"] = self.fonte
            self.email1.pack(side=LEFT)

            self.telefone1 = Label(self.fifth, text=" Telefone                       ", font=self.fonte)
            self.telefone1.pack(side=LEFT)
            self.telefone1 = Entry(self.fifth)
            self.telefone1["width"] = 30
            self.telefone1["font"] = self.fonte
            self.telefone1.pack(side=LEFT)

            self.ctps1= Label(self.sixth, text=" CTPS                           ", font=self.fonte)
            self.ctps1.pack(side=LEFT)
            self.ctps1 = Entry(self.sixth)
            self.ctps1["width"] = 30
            self.ctps1["font"] = self.fonte
            self.ctps1.pack(side=LEFT)

            self.endereco1 = Label(self.seventh, text=" Endereço                     ", font=self.fonte)
            self.endereco1.pack(side=LEFT)
            self.endereco1 = Entry(self.seventh)
            self.endereco1["width"] = 30
            self.endereco1["font"] = self.fonte
            self.endereco1.pack(side=LEFT)



            self.buscar = Button(self.twelfth)
            self.buscar["text"] = "Buscar"
            self.buscar["font"] = ("Times New Roman", "12")
            self.buscar["width"] = 30
            self.buscar["command"] = self.buscarNegoci
            self.buscar.pack()

            self.inserir = Button(self.twelfth)
            self.inserir["text"] = "Inserir"
            self.inserir["font"] = ("Times New Roman", "12")
            self.inserir["width"] = 30
            self.inserir["command"] = self.inserirNegoci
            self.inserir.pack()

            self.atualizar = Button(self.twelfth)
            self.atualizar["text"] = "Atualizar"
            self.atualizar["font"] = ("Times New Roman", "12")
            self.atualizar["width"] = 30
            self.atualizar["command"] = self.alterarNegoci
            self.atualizar.pack()

            self.excluir= Button(self.twelfth)
            self.excluir["text"] = "Excluir"
            self.excluir["font"] = ("Times New Roman", "12")
            self.excluir["width"] = 30
            self.excluir["command"] = self.excluirNegoci
            self.excluir.pack()

            self.sair = Button(self.twelfth)
            self.sair["text"] = "Sair"
            self.sair["font"] = ("Times New Roman", "12")
            self.sair["width"] = 30
            self.sair["command"] = self.twelfth.quit
            self.sair.pack()

            self.testar = Label(self.ponto, text="")
            self.testar.pack()

        def inserirNegoci (self):
            use = Negoci()
            use.nome = self.nome1.get()
            use.email = self.email1.get()
            use.telefone = self.telefone1.get()
            use.ctps = self.ctps1.get()
            use.endereco = self.endereco1.get()
            self.testar["text"] = use.inserirNegociante()
            self.ctps1.delete(0, END)
            self.nome1.delete(0, END)
            self.telefone1.delete(0, END)
            self.email1.delete(0, END)
            self.endereco1.delete(0, END)


        def alterarNegoci(self):
            use = Negoci()
            use.nome = self.nome1.get()
            use.email = self.email1.get()
            use.telefone = self.telefone1.get()
            use.ctps = self.ctps1.get()
            use.endereco = self.endereco1.get()
            self.testar["text"] = use.attNegociante()
            self.ctps1.delete(0, END)
            self.nome1.delete(0, END)
            self.telefone1.delete(0, END)
            self.email1.delete(0, END)
            self.endereco1.delete(0, END)


        def excluirNegoci(self):
            use = Negoci()
            use.ctps = self.ctps1.get()
            self.testar["text"] = use.deleteNegociante()
            self.ctps1.delete(0, END)
            self.nome1.delete(0, END)
            self.telefone1.delete(0, END)
            self.email1.delete(0, END)
            self.endereco1.delete(0, END)

        def buscarNegoci(self):
            use = Negoci()
            use.ctps = self.ctps1.get()
            self.testar["text"] = use.selectNegociante()
            self.ctps1.delete(0, END)
            self.ctps1.insert(INSERT, use.ctps)
            self.endereco1.delete(0, END)
            self.endereco1.insert(INSERT, use.endereco)
            self.nome1.delete(0, END)
            self.nome1.insert(INSERT, use.nome)
            self.telefone1.delete(0, END)
            self.telefone1.insert(INSERT, use.telefone)
            self.email1.delete(0, END)
            self.email1.insert(INSERT, use.email)

    janela = Tk()
    janela.wm_title("Dados do Negociante")
    Negociante(janela)
    janela.mainloop()