from tkinter import *
from Merc import Merc

if __name__ == "__main__":
    class Mercadoria:

        def __init__(self, master=None):
            self.fonte = ("Times New Roman", "12")
            self.first = Frame(master)
            self.first["pady"] = 10
            self.first.pack()

            self.secondt1 = Frame(master)
            self.secondt1["padx"] = 20
            self.secondt1.pack()

            self.fourth = Frame(master)
            self.fourth["padx"] = 20
            self.fourth.pack()

            self.fifth = Frame(master)
            self.fifth["padx"] = 20
            self.fifth.pack()

            self.sixth = Frame(master)
            self.sixth["padx"] = 20
            self.sixth.pack()


            self.seventh = Frame(master)
            self.seventh["padx"] = 20
            self.seventh.pack()

            self.g = Frame(master)
            self.g["padx"] = 20
            self.g.pack()

            self.s = Frame(master)
            self.s["padx"] = 20
            self.s.pack()

            self.t = Frame(master)
            self.t["padx"] = 20
            self.t.pack()

            self.eighth = Frame(master)
            self.eighth["padx"] = 20
            self.eighth["pady"] = 20
            self.eighth.pack()


            self.ponto = Frame(master)
            self.ponto["pady"] = 20
            self.ponto.pack()

            self.titulo = Label(self.first, text="                          Dados da mercadoria ")
            self.titulo["font"] = ("Times New Roman", "12", "italic", "bold")
            self.titulo.pack()

            self.nome1 = Label(self.secondt1, text="Nome                           ", font=self.fonte)
            self.nome1.pack(side=LEFT)
            self.nome1 = Entry(self.secondt1)
            self.nome1["width"] = 30
            self.nome1["font"] = self.fonte
            self.nome1.pack(side=LEFT)

            self.nota1 = Label(self.fourth, text="Nota fiscal                    ", font=self.fonte)
            self.nota1.pack(side=LEFT)
            self.nota1 = Entry(self.fourth)
            self.nota1["width"] = 30
            self.nota1["font"] = self.fonte
            self.nota1.pack(side=LEFT)

            self.ID = Label(self.fifth, text="ID                                ", font=self.fonte)
            self.ID.pack(side=LEFT)
            self.ID = Entry(self.fifth)
            self.ID["width"] = 30
            self.ID["font"] = self.fonte
            self.ID.pack(side=LEFT)

            self.garantia1 = Label(self.sixth, text="Garantia                       ", font=self.fonte)
            self.garantia1.pack(side=LEFT)
            self.garantia1 = Entry(self.sixth)
            self.garantia1["width"] = 30
            self.garantia1["font"] = self.fonte
            self.garantia1.pack(side=LEFT)

            self.quantidade1 = Label(self.g, text="Quantidade                  ", font=self.fonte)
            self.quantidade1.pack(side=LEFT)
            self.quantidade1 = Entry(self.g)
            self.quantidade1["width"] = 30
            self.quantidade1["font"] = self.fonte
            self.quantidade1.pack(side=LEFT)

            self.compra = Label(self.seventh, text="Data da compra           ", font=self.fonte)
            self.compra.pack(side=LEFT)
            self.compra = Entry(self.seventh)
            self.compra["width"] = 30
            self.compra["font"] = self.fonte
            self.compra.pack(side=LEFT)

            self.ctps1 = Label(self.t, text="CTPS de quem vendeu", font=self.fonte)
            self.ctps1.pack(side=LEFT)
            self.ctps1 = Entry(self.t)
            self.ctps1["width"] = 30
            self.ctps1["font"] = self.fonte
            self.ctps1.pack(side=LEFT)

            self.cpf1 = Label(self.s, text="CPF de quem comprou", font=self.fonte)
            self.cpf1.pack(side=LEFT)
            self.cpf1 = Entry(self.s)
            self.cpf1["width"] = 30
            self.cpf1["font"] = self.fonte
            self.cpf1.pack(side=LEFT)

            self.buscar = Button(self.eighth)
            self.buscar["text"] = "Buscar"
            self.buscar["font"] = ("Times New Roman", "12")
            self.buscar["width"] = 30
            self.buscar["command"] = self.buscarMercadoria
            self.buscar.pack()

            self.inserir = Button(self.eighth)
            self.inserir["text"] = "Inserir"
            self.inserir["font"] = ("Times New Roman", "12")
            self.inserir["width"] = 30
            self.inserir["command"] = self.insertMercadoria
            self.inserir.pack()

            self.atualizar = Button(self.eighth)
            self.atualizar["text"] = "Atualizar"
            self.atualizar["font"] = ("Times New Roman", "12")
            self.atualizar["width"] = 30
            self.atualizar["command"] = self.altMercadoria
            self.atualizar.pack()

            self.excluir = Button(self.eighth)
            self.excluir["text"] = "Excluir"
            self.excluir["font"] = ("Times New Roman", "12")
            self.excluir["width"] = 30
            self.excluir["command"] = self.excluirMercadoria
            self.excluir.pack()

            self.sair = Button(self.eighth)
            self.sair["text"] = "Sair"
            self.sair["font"] = ("Times New Roman", "12")
            self.sair["width"] = 30
            self.sair["command"] = self.eighth.quit
            self.sair.pack()
            self.testar = Label(self.ponto, text="")
            self.testar.pack()

        def insertMercadoria(self):
            use = Merc()
            use.nome = self.nome1.get()
            use.nota = self.nota1.get()
            use.id = self.ID.get()
            use.garantia = self.garantia1.get()
            use.data = self.compra.get()
            use.quantidade = self.quantidade1.get()
            use.cpf = self.cpf1.get()
            use.ctps = self.ctps1.get()
            self.nome1.delete(0, END)
            self.nota1.delete(0, END)
            self.ID.delete(0, END)
            self.garantia1.delete(0, END)
            self.compra.delete(0, END)
            self.quantidade1.delete(0, END)
            self.cpf1.delete(0, END)
            self.ctps1.delete(0, END)
            self.testar["text"] = use.inserirMercadoria()



        def altMercadoria(self):
            use = Merc()
            use.nome = self.nome1.get()
            self.nome1.delete(0, END)
            use.nota = self.nota1.get()
            self.nota1.delete(0, END)
            use.id = self.ID.get()
            self.ID.delete(0, END)
            use.garantia = self.garantia1.get()
            self.garantia1.delete(0, END)
            use.data = self.compra.get()
            self.compra.delete(0, END)
            use.quantidade = self.quantidade1.get()
            self.quantidade1.delete(0, END)
            use.cpf = self.cpf1.get()
            self.cpf1.delete(0, END)
            use.ctps = self.ctps1.get()
            self.ctps1.delete(0, END)
            self.testar["text"] = use.attMercadoria()

        def excluirMercadoria(self):
            use = Merc()
            use.id = self.ID.get()
            self.testar["text"] = use.deleteMercadoria()
            self.nome1.delete(0, END)
            self.ID.delete(0, END)
            self.nota1.delete(0, END)
            self.garantia1.delete(0, END)
            self.compra.delete(0, END)
            self.ctps1.delete(0, END)
            self.cpf1.delete(0, END)
            self.quantidade1.delete(0, END)

        def buscarMercadoria(self):
            use = Merc()
            use.id = self.ID.get()
            self.testar["text"] = use.selectMercadoria()
            self.ID.delete(0, END)
            self.ID.insert(INSERT, use.id)
            self.nome1.delete(0, END)
            self.nome1.insert(INSERT, use.nome)
            self.nota1.delete(0, END)
            self.nota1.insert(INSERT, use.nota)
            self.garantia1.delete(0, END)
            self.garantia1.insert(INSERT, use.garantia)
            self.compra.delete(0, END)
            self.compra.insert(INSERT, use.data)
            self.ctps1.delete(0, END)
            self.ctps1.insert(INSERT, use.ctps)
            self.cpf1.delete(0, END)
            self.cpf1.insert(INSERT, use.cpf)
            self.quantidade1.delete(0, END)
            self.quantidade1.insert(INSERT, use.quantidade)


    janela = Tk()
    janela.wm_title("Dados da Mercadoria")
    Mercadoria(janela)
    janela.mainloop()
