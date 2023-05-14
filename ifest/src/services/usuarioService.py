import psycopg2

def buscarUsuario(email):
    
    #Conectar ao banco de dados
    conn = psycopg2.connect(
        host = "localhost",
        database = "ifest",
        user = "admin",
        password = "ifest",
        options = "-c search_path=ifest"
        )

    #Criar um cursos
    cur = conn.cursor()

    #Executar um select
    cur.execute(f"SELECT * FROM usuario WHERE ds_email = '{email}' LIMIT 1")

    #Obter os resultados
    row = cur.fetchall()

    #Fechar o cursor e a conexão
    cur.close()
    conn.close()

    if not row:
        return 0
    else:
        return row[0][1]
    

