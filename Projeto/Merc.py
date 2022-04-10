from main import BD


class Merc(object):

    def __init__(self, nome="",nota="", id="", garantia="", data="",quantidade="", ctps="", cpf=""):
        self.nome = nome
        self.nota = nota
        self.id = id
        self.garantia = garantia
        self.data = data
        self.quantidade = quantidade
        self.ctps= ctps
        self.cpf= cpf
    def inserirMercadoria(self):
        curso = BD.conexao.cursor()
        curso.execute("INSERT INTO bruno_verissimo.mercadoria (nome, nota, id, garantia, dtcompra, quantidade, pfpj, ctps) VALUES (%s, %s, %s,%s, %s, %s, %s, %s);",(self.nome, self.nota, self.id, self.garantia, self.data, self.cpf, self.ctps))
        BD.conexao.commit()
        curso.close()


    def attMercadoria(self):
        curso = BD.conexao.cursor()
        curso.execute("UPDATE bruno_verissimo.mercadoria SET nome=%s, nota=%s, Garantia=%s, dtcompra=%s, Quantidade=%s, pfpj=%s, CTPS=%s WHERE id=%s;",(self.nome, self.nota,self.garantia, self.data,self.ctps,self.cpf, self.id ))
        BD.conexao.commit()
        curso.close()


    def deleteMercadoria(self):
        try:
            curso = BD.conexao.cursor()
            curso.execute("DELETE FROM bruno_verissimo.mercadoria WHERE id=%s;", (self.id,))
            BD.conexao.commit()
            curso.close()
            return "Mercadoria deletada!"
        except:
            return "Ocorreu algum erro!"




    def selectMercadoria(self):
        try:
            curso = BD.conexao.cursor()
            curso.execute("select * from bruno_verissimo.mercadoria WHERE id=%s;", (self.id,))
            l = curso.fetchall()
            for local in l:
                self.nome= local[0]
                self.nota= local[1]
                self.id= local[2]
                self.garantia= local[3]
                self.data= local[4]
                self.quantidade= local[5]
                self.cpf= local[6]
                self.ctps= local[7]
            curso.close()
            return "Busca realizada com sucesso!"
        except:
            return "Ocorreu algum erro!"


