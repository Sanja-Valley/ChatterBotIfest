from flask import Blueprint, request
from services.chat import respostas, finalizar
from controllers.chatController import testeChat
from controllers.produtoController import atualizarProdutosCarrinho, buscarCarrinho
from services.logService import inserirLog
from datetime import datetime


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
    return {'resposta': resposta, 'contexto': contexto, "n": n}


blueprint.route('/teste', methods=['GET'])(testeChat)

# ProdutoController
blueprint.route('/update', methods=['POST'])(atualizarProdutosCarrinho)


@blueprint.route('/search/<string:id>', methods=['GET'])
def search(id):
    return buscarCarrinho(id)
