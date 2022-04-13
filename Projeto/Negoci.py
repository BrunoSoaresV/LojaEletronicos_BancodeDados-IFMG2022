from main import BD

class Negoci(object):

    def __init__(self, nome="", email="", telefone="", ctps="",endereco=""):
        self.nome = nome
        self.email= email
        self.telefone=telefone
        self.ctps = ctps
        self.endereco=endereco
    def inserirNegociante(self):
        try:
            curso = BD.conexao.cursor()
            curso.execute("INSERT INTO bruno_verissimo.vendedor (nome, email, telefone, ctps, endereco) VALUES (%s, %s, %s,%s, %s );",(self.nome, self.email, self.telefone, self.ctps, self.endereco))
            BD.conexao.commit()
            curso.close()
            return "Negociante inserido!"
        except:
            return "Ocorreu um erro na inserção!"



    def attNegociante(self):
        try:
            curso = BD.conexao.cursor() 
            curso.execute("UPDATE bruno_verissimo.vendedor SET nome=%s, email=%s, telefone=%s, endereco=%s WHERE ctps=%s;",(self.nome, self.email, self.telefone, self.endereco, self.ctps))
            BD.conexao.commit()
            curso.close()
            return "Negociante atualizado!"
        except:
            return "Ocorreu um erro na atualização!"

    def deleteNegociante(self):
        try:
            curso = BD.conexao.cursor()
            curso.execute("DELETE FROM bruno_verissimo.vendedor WHERE ctps=%s;", (self.ctps,))
            BD.conexao.commit()
            curso.close()
            return "Negociante deletado!"
        except:
            return "Ocorreu algum erro!"

    def selectNegociante(self):
        try:
            curso = BD.conexao.cursor()
            curso.execute("select * from bruno_verissimo.vendedor WHERE ctps=%s;", (self.ctps,))
            l = curso.fetchall()
            for local in l:
                self.nome = local[0]
                self.email = local[1]
                self.telefone = local[2]
                self.ctps = local[3]
                self.endereco = local[4]
            curso.close()
            return "Busca realizada com sucesso!"
        except:
            return "Ocorreu algum erro!"


