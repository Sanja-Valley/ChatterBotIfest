from config import get_database, get_postgre
from bson import ObjectId
import json
from bson.json_util import dumps
from flask import jsonify
import pandas as pd

db = get_database()
carrinhodb = db["carrinho_compras"]


def buscarCarrinho(carrinhoId):
    id = {"_id": ObjectId(carrinhoId)}
    getCarrinho = carrinhodb.find_one(id)
    if (getCarrinho is not None):
        return json.loads(dumps(getCarrinho))
    else:
        return 0


def atualizarCarrinho(carrinho, id):
    result = carrinhodb.update_one(
        {"_id": ObjectId(id)},
        {"$set":
             {"carrinho": carrinho['carrinho'],
              "total": carrinho['total']
              }})
    # Verifica se a atualização foi bem sucedida
    if result.modified_count == 1:
        # Se a atualização foi bem-sucedida, retorna uma mensagem em JSON
        return jsonify({'message': 'Carrinho atualizado com sucesso.', 'id': id}), 200
    else:
        # Se a atualização falhou, retorna uma mensagem de erro em JSON
        return jsonify({'message': 'Não foi possível atualizar o carrinho.'}), 400


def adicionarCarrinho(carrinho):
    result = carrinhodb.insert_one(carrinho)
    if result.inserted_id:
        carrinho["_id"] = json.loads(dumps(result.inserted_id))
        return carrinho
    else:
        return jsonify({'message': 'Não foi possível adicionar o carrinho.'}), 400


def recomendacao():
    #Grupo Logado

    query = "select * from produto_review where id_user = 383"
    df = pd.read_sql(query, get_postgre())

    #df_user = df[df['id_user'] == '383']
    df_user_dpto = df.groupby('class_name').sum()
    df_user_dpto = df_user_dpto.sort_values(by='id_user', ascending=False)
    query = f"select distinct pd.nome_decoracao from ifest.ifest.produto_decoracao pd join public.produto_review pr on pd.id = pr.clothing_id where class_name = '{str(df_user_dpto.index[0])}' limit 5"
    df = pd.read_sql(query, get_postgre())

    # obter valores da coluna "nome_decoracao" como uma lista
    decoracoes = df['nome_decoracao'].to_list()

    # unir os valores da lista em uma única string, separando com vírgula e quebra de linha
    decoracoes_str = ",\n".join(decoracoes)

    return decoracoes_str
