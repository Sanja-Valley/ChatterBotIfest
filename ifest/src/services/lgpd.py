from config import get_postgre

def aceitar_termo_lgpd(email):
    db = get_postgre()
    cur = db.cursor()

    search = f"SELECT u.id FROM ifest.usuario_novo u WHERE u.email = '{email}' LIMIT 1;"
    cur.execute(search)
    user_id = cur.fetchone()[0]

    query = f"INSERT INTO ifest.user_termo(id_user, id_termo, data) VALUES ({user_id}, 1, CURRENT_TIMESTAMP);"
    cur.execute(query)

    db.commit()
    cur.close()
    db.close()

    return 'Modificação inserida com sucesso'


def verifica_aceite(email):
    db = get_postgre()
    query = f"SELECT id, texto FROM ifest.termo_lgpd ORDER  BY id DESC LIMIT 1;"

    cur = db.cursor()
    cur.execute(query)

    (termo_id, termo_texto) = cur.fetchone()

    query = f"SELECT COUNT(*) FROM ifest.user_termo ut LEFT JOIN ifest.usuario_novo u ON u.id = ut.id_user\
            WHERE u.email = %s AND ut.id_termo = %s;"
    params = (email, termo_id)

    cur.execute(query, params)

    retorno = None

    if cur.fetchone()[0] == 0:
        retorno = termo_texto

    cur.close()
    db.close()
    return retorno
