from flask import Blueprint, request
from services.chat import respostas
from controllers.chatController import testeChat
from controllers.produtoController import atualizarProdutosCarrinho, buscarCarrinho


blueprint = Blueprint('blueprint', __name__)

@blueprint.route('/', methods=['POST'])
def receber():
    mensagem = request.json['mensagem']
    contexto = request.json['contexto']
    resposta, contexto = respostas(mensagem, contexto)
    return {'resposta': resposta, 'contexto': contexto}


blueprint.route('/teste', methods=['GET'])(testeChat)

# ProdutoController
blueprint.route('/update', methods=['POST'])(atualizarProdutosCarrinho)


@blueprint.route('/search/<string:id>', methods=['GET'])
def search(id):
    return buscarCarrinho(id)
