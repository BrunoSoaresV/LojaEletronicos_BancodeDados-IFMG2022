from User import User
from tkinter import *

if __name__ == "__main__":
   class Cliente:
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

           self.tenth = Frame(master)
           self.tenth["padx"] = 20
           self.tenth["pady"] = 20
           self.tenth.pack()

           self.ponto = Frame(master)
           self.ponto["pady"] = 20
           self.ponto.pack()

           self.titulo = Label(self.first, text="                Dados do cliente")
           self.titulo["font"] = ("Times New Roman", "12", "italic", "bold")
           self.titulo.pack()

           self.nome1 = Label(self.second, text="Nome      ", font=self.fonte)
           self.nome1.pack(side=LEFT)
           self.nome1 = Entry(self.second)
           self.nome1["width"] = 30
           self.nome1["font"] = self.fonte
           self.nome1.pack(side=LEFT)

           self.email1 = Label(self.third, text="Email       ", font=self.fonte)
           self.email1.pack(side=LEFT)
           self.email1 = Entry(self.third)
           self.email1["width"] = 30
           self.email1["font"] = self.fonte
           self.email1.pack(side=LEFT)


           self.telefone1 = Label(self.fifth, text="Telefone  ", font=self.fonte)
           self.telefone1.pack(side=LEFT)
           self.telefone1 = Entry(self.fifth)
           self.telefone1["width"] = 30
           self.telefone1["font"] = self.fonte
           self.telefone1.pack(side=LEFT)

           self.cpf1 = Label(self.sixth, text="CPF        ", font=self.fonte)
           self.cpf1.pack(side=LEFT)
           self.cpf1 = Entry(self.sixth)
           self.cpf1["width"] = 30
           self.cpf1["font"] = self.fonte
           self.cpf1.pack(side=LEFT)

           self.endereco1 = Label(self.seventh, text="Endereço", font=self.fonte)
           self.endereco1.pack(side=LEFT)
           self.endereco1 = Entry(self.seventh)
           self.endereco1["width"] = 30
           self.endereco1["font"] = self.fonte
           self.endereco1.pack(side=LEFT)


           self.buscar = Button(self.tenth)
           self.buscar["text"] = "Buscar"
           self.buscar["font"] = ("Times New Roman", "12")
           self.buscar["width"] = 30
           self.buscar["command"] = self.buscarUsuario
           self.buscar.pack()

           self.inserir = Button(self.tenth)
           self.inserir["text"] = "Inserir"
           self.inserir["font"] = ("Times New Roman", "12")
           self.inserir["width"] = 30
           self.inserir["command"] = self.ibcd
           self.inserir.pack()

           self.atualizar = Button(self.tenth)
           self.atualizar["text"] = "Atualizar"
           self.atualizar["font"] = ("Times New Roman", "12")
           self.atualizar["width"] = 30
           self.atualizar["command"] = self.alterarUsuario
           self.atualizar.pack()

           self.excluir = Button(self.tenth)
           self.excluir["text"] = "Excluir"
           self.excluir["font"] = ("Times New Roman", "12")
           self.excluir["width"] = 30
           self.excluir["command"] = self.excluirUsuario
           self.excluir.pack()

           self.sair = Button(self.tenth)
           self.sair["text"] = "Sair"
           self.sair["font"] = ("Times New Roman", "12")
           self.sair["width"] = 30
           self.sair["command"] = self.tenth.quit
           self.sair.pack()

           self.testar = Label(self.ponto, text="")
           self.testar.pack()


       def ibcd(self):
           use = User()
           use.nome = self.nome1.get()
           use.email = self.email1.get()
           use.telefone = self.telefone1.get()
           use.cpf = self.cpf1.get()
           use.endereco = self.endereco1.get()
           self.testar["text"] = use.inserirCliente()
           self.cpf1.delete(0, END)
           self.nome1.delete(0, END)
           self.telefone1.delete(0, END)
           self.email1.delete(0, END)
           self.endereco1.delete(0, END)


       def alterarUsuario(self):
           use = User()
           use.nome = self.nome1.get()
           use.email = self.email1.get()
           use.telefone = self.telefone1.get()
           use.cpf = self.cpf1.get()
           use.endereco = self.endereco1.get()
           self.testar["text"] = use.attCliente()
           self.cpf1.delete(0, END)
           self.nome1.delete(0, END)
           self.telefone1.delete(0, END)
           self.email1.delete(0, END)
           self.endereco1.delete(0, END)



       def excluirUsuario(self):
           use = User()
           use.cpf = self.cpf1.get()
           self.testar["text"] = use.deleteCliente()
           self.cpf1.delete(0, END)
           self.nome1.delete(0, END)
           self.telefone1.delete(0, END)
           self.email1.delete(0, END)
           self.endereco1.delete(0, END)



       def buscarUsuario(self):
           use = User()
           use.cpf = self.cpf1.get()
           self.testar["text"] = use.selectCliente(use.cpf)
           self.cpf1.delete(0, END)
           self.cpf1.insert(INSERT, use.cpf)
           self.endereco1.delete(0, END)
           self.endereco1.insert(INSERT, use.endereco)
           self.nome1.delete(0, END)
           self.nome1.insert(INSERT, use.nome)
           self.telefone1.delete(0, END)
           self.telefone1.insert(INSERT, use.telefone)
           self.email1.delete(0, END)
           self.email1.insert(INSERT, use.email)

   janela = Tk()
   janela.wm_title("Dados do Cliente")
   Cliente(janela)
   janela.mainloop()
