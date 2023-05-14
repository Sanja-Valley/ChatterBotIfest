#import psycopg2
from config import get_postgre
def buscarUsuario(email):
    
    #Conectar ao banco de dados
    conn = get_postgre()

    #Criar um cursos
    cur = conn.cursor()

    #Executar um select
    cur.execute(f"SELECT * FROM usuario WHERE nome = '{email}' LIMIT 1")

    #Obter os resultados
    row = cur.fetchall()

    #Fechar o cursor e a conexão
    cur.close()
    conn.close()

    if not row:
        return 0
    else:
        return row[0][1]
    

