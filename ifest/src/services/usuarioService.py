from config import get_postgre


def buscarUsuario(email):
    # Conectar ao banco de dados
    conn = get_postgre()

    # Criar um cursos
    cur = conn.cursor()

    # Executar um select
    cur.execute(f"SELECT * FROM ifest.ifest.usuario_novo WHERE email = '{email}' LIMIT 1")

    # Obter os resultados
    row = cur.fetchall()

    # Fechar o cursor e a conexão
    cur.close()
    conn.close()

    if not row:
        return 0
    else:

        return row[0][1].split("@")[0]
    

def termo_lgpd(email: str):
    conn = get_postgre()
    cur = conn.cursor()

    cur.execute(f"SELECT max(data) FROM ifest.ifest.termo_lgpd")

    row = cur.fetchall()
    date_obj = row[0][0]

    cur.execute(f"select count(*) >= 1 from ifest.ifest.user_termo ut \
        join ifest.ifest.usuario_novo un on un.id = ut.id_user \
        where un.email = '{email}'  \
        and ut.data >= '{date_obj.strftime('%Y-%m-%d %H:%M:%S')}'")

    row = cur.fetchall()
    # Fechar o cursor e a conexão
    cur.close()
    conn.close()

    return {'lgpd': row[0][0]}
