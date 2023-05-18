#import psycopg2
from config import get_postgre
def buscarUsuario(email):
    
    #Conectar ao banco de dados
    conn = get_postgre()

    #Criar um cursos
    cur = conn.cursor()

    #Executar um select
    cur.execute(f"SELECT * FROM usuario_novo WHERE email = '{email}' LIMIT 1")

    #Obter os resultados
    row = cur.fetchall()

    #Fechar o cursor e a conexão
    cur.close()
    conn.close()

    if not row:
        return 0
    else:
        return row[0][1]
    

def termo_lgpd(email: str):
    conn = get_postgre()
    # Criar um cursos
    cur = conn.cursor()
    # Executar um select
    cur.execute(f"SELECT max(data) FROM termo_lgpd")

    # Obter os resultados
    row = cur.fetchall()
    print(row[0])

    cur.execute(f"select count(*) >= 1 from user_termo ut \
        join usuario_novo un on un.id = ut.id_user \
        where un.email = {email} \
        and ut.'data' >= {row[0]}")

    # Fechar o cursor e a conexão
    cur.close()
    conn.close()

    if not row:
        return 0
    else:
        return row[0][1]
