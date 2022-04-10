from main import BD


class Esto(object):

    def __init__(self, quantidade="", id="", nome=""):
        self.quantidade = quantidade
        self.id = id
        self.nome = nome

    def inserirEstoque(self):
        try:
            curso = BD.conexao.cursor()
            curso.execute("INSERT INTO bruno_verissimo.estoque (quantidade, nome) VALUES (%s, %s);",(self.quantidade, self.nome))
            BD.conexao.commit()
            curso.close()
            return "Estoque inserido!"
        except:
            return "Ocorreu um erro na inserção!"



    def attEstoque(self):
        try:
            curso = BD.conexao.cursor()
            curso.execute("UPDATE bruno_verissimo.estoque SET quantidade=%s, nome=%s WHERE id=%s;",(self.quantidade, self.nome, self.id))
            BD.conexao.commit()
            curso.close()
            return "Estoque atualizado!"
        except:
            return "Ocorreu um erro na atualização!"

    def deleteEstoque(self):
        curso = BD.conexao.cursor()
        curso.execute("DELETE FROM bruno_verissimo.estoque WHERE id=%s;",(self.id,))
        BD.conexao.commit()
        curso.close()

    def selectEstoque(self):
        curso = BD.conexao.cursor()
        curso.execute("select * from bruno_verissimo.estoque WHERE id=%s;", (self.id,))
        l = curso.fetchall()
        for local in l:
            self.quantidade = local[0]
            self.id = local[1]
            self.nome = local[1]
        curso.close()



