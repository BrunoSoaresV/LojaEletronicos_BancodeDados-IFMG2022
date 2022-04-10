import psycopg2
class BD():
   conexao=psycopg2.connect(database="aula", user="aula", password="aula", host="200.18.128.54", port="5432")
   curso=conexao.cursor()
