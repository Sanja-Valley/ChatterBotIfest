from flask import Blueprint, request
from services.chat import respostas, finalizar
from controllers.chatController import testeChat
from controllers.produtoController import atualizarProdutosCarrinho, buscarCarrinho


blueprint = Blueprint('blueprint', __name__)

@blueprint.route('/', methods=['POST'])
def receber():
    mensagem = request.json['mensagem']
    contexto = request.json['contexto']
    n =  request.json['n']
    imagens_url = []
    
    images_path = [
        'C:\Projects\Faculdade\ChatterBotIfest\ifest\images\chacara.jpeg',
        'C:\Projects\Faculdade\ChatterBotIfest\ifest\images\salao.jpeg'
    ]
    imagens_url = [f'http://localhost:5000/{p}' for p in images_path]

    if contexto == "finalizar" or mensagem.lower() == "finalizar":
        return finalizar()
    else:
        resposta, contexto, n = respostas(mensagem, contexto, n)
        return {'resposta': resposta, 'contexto': contexto, "n": n, "imagem":imagens_url}


blueprint.route('/teste', methods=['GET'])(testeChat)

# ProdutoController
blueprint.route('/update', methods=['POST'])(atualizarProdutosCarrinho)


@blueprint.route('/search/<string:id>', methods=['GET'])
def search(id):
    return buscarCarrinho(id)
