from flask import Blueprint, request
from services.chat import respostas, finalizar
from controllers.chatController import testeChat
from controllers.produtoController import atualizarProdutosCarrinho, buscarCarrinho
from services.logService import inserirLog
from datetime import datetime
from pymongo import MongoClient


blueprint = Blueprint('blueprint', __name__)
log = {}

@blueprint.route('/', methods=['POST'])
def receber():
    mensagem = request.json['mensagem']
    contexto = request.json['contexto']

    n = request.json['n']
    
    inserirLog({'user': mensagem, 'date': str(datetime.now())})

    if contexto == "finalizar" or mensagem.lower() == "finalizar":
        resposta = finalizar()
        contexto = "finalizar"
    else:
        resposta, contexto, n = respostas(mensagem, contexto, n)

    inserirLog({'bot': resposta, 'date': str(datetime.now())})
    print('retorno',{'resposta': resposta, 'contexto': contexto, "n": n})
    return {'resposta': resposta, 'contexto': contexto, "n": n}


blueprint.route('/teste', methods=['GET'])(testeChat)

# ProdutoController
blueprint.route('/update', methods=['POST'])(atualizarProdutosCarrinho)


@blueprint.route('/search/<string:id>', methods=['GET'])
def search(id):
    return buscarCarrinho(id)


@blueprint.route('/salvar', methods=['POST'])
def salvar():
    client = MongoClient('localhost', 27017)
    db = client['iFestDB']
    collection = db['LGPD']

    data = request.get_json()
    nome = data['nome']
    email = data['email']
    estado = data['estado']
    data_hora = data['data']
    collection.insert_one({'nome': nome, 'email': email, 'data_hora': data_hora, 'estado': estado})
    return 'Usuário inserido com sucesso'
