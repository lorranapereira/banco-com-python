import psycopg2

con = psycopg2.connect(host='localhost', database='tiago', user='postgres', password='postgres')
cur = con.cursor()
#listar limit ofsset se tiver se tiver com id alterar, se não tiver criar 
#sql = "select *from alunos"
#cur.execute(sql)
#for linha in cur.fetchall():
    #print(linha)

#con.close() 
#inserir
#cur.execute("insert into alunos (aluno, id) values (%s,%s)",["guilherme",3])
#con.commit()

#alterar
#cur.execute("update alunos set aluno = %s  where id = (%s)",["lorrana",3])
#con.commit()

#deletar 
#cur.execute("delete from alunos where id = (%s)",[3])
#con.commit()
#buscar 

#buscar
cur.execute("select *from alunos where id = (%s)",[4])
con.commit()
print(cur.fetchone())


con.close() 
