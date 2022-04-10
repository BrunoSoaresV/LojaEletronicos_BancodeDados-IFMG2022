from main import BD
class User(object):
    def __init__(self, nome="", telefone="", email="", cpf="", endereco=""):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.cpf = cpf
        self.endereco = endereco
    def inserirCliente(self):
        try:
            curso = BD.conexao.cursor()
            curso.execute("INSERT INTO bruno_verissimo.cliente (nome, email, telefone, pfpj, endereco) VALUES (%s, %s, %s,%s, %s );", (self.nome, self.email, self.telefone, self.cpf, self.endereco))
            BD.conexao.commit()
            curso.close()
            return "Cliente cadastrado!"
        except:
            return "Ocorreu um erro no cadastro!"

    def attCliente(self):
        try:
            curso = BD.conexao.cursor()
            curso.execute("UPDATE bruno_verissimo.cliente SET nome=%s, email=%s, telefone=%s, endereco=%s WHERE pfpj=%s;", (self.nome, self.email, self.telefone, self.endereco, self.cpf))
            BD.conexao.commit()
            curso.close()
            return "Cliente atualizado!"
        except:
            return "Ocorreu um erro na atualização!"



    def deleteCliente(self):
        try:
            curso = BD.conexao.cursor()
            curso.execute ("DELETE FROM bruno_verissimo.cliente WHERE pfpj=%s;", (self.cpf,))
            BD.conexao.commit()
            curso.close()
            return "Cliente deletado!"
        except:
            return "Ocorreu algum erro!"

    def selectCliente(self, cpf):
        try:
            curso = BD.conexao.cursor()
            curso.execute("select * from bruno_verissimo.cliente WHERE pfpj=%s;", (self.cpf,))
            l=curso.fetchall()
            for local in l:
                self.nome = local[0]
                self.email = local[1]
                self.telefone = local[2]
                self.cpf = local[3]
                self.endereco = local[4]
            curso.close()
            return "Busca realizada com sucesso!"
        except:
            return "Ocorreu algum erro!"

