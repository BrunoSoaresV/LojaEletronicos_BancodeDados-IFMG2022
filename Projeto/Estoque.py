from tkinter import *
from Esto import Esto

if __name__ == "__main__":
    class Estoque1:
            def __init__(self, master=None):
                self.fonte = ("Times New Roman", "12")
                self.first = Frame(master)
                self.first["pady"] = 10
                self.first.pack()

                self.second = Frame(master)
                self.second["padx"] = 20
                self.second.pack()

                self.g = Frame(master)
                self.g["padx"] = 20
                self.g.pack()

                self.third = Frame(master)
                self.third["padx"] = 20
                self.third.pack()


                self.fourth= Frame(master)
                self.fourth["padx"] = 20
                self.fourth["pady"] = 20
                self.fourth.pack()

                self.ponto = Frame(master)
                self.ponto["pady"] = 20
                self.ponto.pack()


                self.titulo = Label(self.first, text="          Informações do estoque")
                self.titulo["font"] = ("Times New Roman", "12", "italic", "bold")
                self.titulo.pack()

                self.quantidade1 = Label(self.second, text="Quantidade", font=self.fonte)
                self.quantidade1.pack(side=LEFT)
                self.quantidade1 = Entry(self.second)
                self.quantidade1["width"] = 30
                self.quantidade1["font"] = self.fonte
                self.quantidade1.pack(side=LEFT)

                self.ID= Label(self.g, text="ID              ", font=self.fonte)
                self.ID.pack(side=LEFT)
                self.ID = Entry(self.g)
                self.ID["width"] = 30
                self.ID["font"] = self.fonte
                self.ID.pack(side=LEFT)

                self.n1 = Label(self.third, text="Nome        ", font=self.fonte)
                self.n1.pack(side=LEFT)
                self.n1 = Entry(self.third)
                self.n1["width"] = 30
                self.n1["font"] = self.fonte
                self.n1.pack(side=LEFT)

                self.buscar = Button(self.fourth)
                self.buscar["text"] = "Buscar"
                self.buscar["font"] = ("Times New Roman", "12")
                self.buscar["width"] = 30
                self.buscar["command"] = self.buscarEsto
                self.buscar.pack()

                self.inserir = Button(self.fourth)
                self.inserir["text"] = "Inserir"
                self.inserir["font"] = ("Times New Roman", "12")
                self.inserir["width"] = 30
                self.inserir["command"] = self.InserEs
                self.inserir.pack()

                self.atualizar = Button(self.fourth)
                self.atualizar["text"] = "Atualizar"
                self.atualizar["font"] = ("Times New Roman", "12")
                self.atualizar["width"] = 30
                self.atualizar["command"] = self.altEstoque
                self.atualizar.pack()

                self.excluir= Button(self.fourth)
                self.excluir["text"] = "Excluir"
                self.excluir["font"] = ("Times New Roman", "12")
                self.excluir["width"] = 30
                self.excluir["command"] = self.excluirEsto
                self.excluir.pack()

                self.sair = Button(self.fourth)
                self.sair["text"] = "Sair"
                self.sair["font"] = ("Times New Roman", "12")
                self.sair["width"] = 30
                self.sair["command"] = self.fourth.quit
                self.sair.pack()

                self.testar = Label(self.ponto, text="")
                self.testar.pack()

            def InserEs(self):
                use = Esto()
                use.quantidade = self.quantidade1.get()
                self.quantidade1.delete(0, END)
                use.nome = self.n1.get()
                self.testar["text"] = use.inserirEstoque()
                self.n1.delete(0, END)
                use.id=self.ID.get()
                self.ID.delete(0, END)
            def altEstoque(self):
                use = Esto()
                use.quantidade = self.quantidade1.get()
                use.nome = self.n1.get()
                self.testar["text"] = use.attEstoque()
                self.n1.delete(0, END)
                self.quantidade1.delete(0, END)
                use.id = self.ID.get()
                self.ID.delete(0, END)
            def excluirEsto(self):
                use = Esto()
                use.nome = self.n1.get()
                self.testar["text"] = use.deleteEstoque()
                self.n1.delete(0, END)
                self.quantidade1.delete(0, END)
                self.ID.delete(0, END)

            def buscarEsto(self):
                use = Esto()
                use.id = self.ID.get()
                self.testar["text"] = use.selectEstoque()
                self.ID.delete(0, END)
                self.ID.insert(INSERT, use.id)
                self.quantidade1.delete(0, END)
                self.quantidade1.insert(INSERT, use.quantidade)
                self.n1.delete(0, END)
                self.n1.insert(INSERT, use.nome)
                self.ID.delete(0, END)
                self.ID.insert(INSERT, use.id)
    janela = Tk()
    janela.wm_title("Dados do Estoque")
    Estoque1(janela)
    janela.mainloop()