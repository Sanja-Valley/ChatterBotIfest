from config import get_database
from bson import ObjectId
import json
from bson.json_util import dumps
from flask import jsonify

db = get_database()
carrinhodb = db["carrinho_compras"]

def buscarCarrinho(carrinhoId):
    id = {"_id": ObjectId(carrinhoId)}
    getCarrinho = carrinhodb.find_one(id)
    if(getCarrinho is not None):
        return json.loads(dumps(getCarrinho))
    else:
        return 0
    
def atualizarCarrinho(carrinho, id):
    result  = carrinhodb.update_one(
        {"_id": ObjectId(id)}, 
        { "$set": 
            { "carrinho": carrinho['carrinho'], 
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
        return jsonify({'message': 'Carrinho adicionado com sucesso.', 'carrinho': carrinho}), 200
    else:
        return jsonify({'message': 'Não foi possível adicionar o carrinho.'}), 400