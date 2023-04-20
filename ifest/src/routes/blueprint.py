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
    
    images_path = [
        #Aqui pode retornar qualquer coisa
        #To retorando o nome da imagem que a gente setou
        #Depois vou faze a logica para gerar esses nomes
        'chacara.jpeg',
        'salao.jpeg'
    ]    

    if contexto == "finalizar" or mensagem.lower() == "finalizar":
        return finalizar()
    else:
        resposta, contexto, n = respostas(mensagem, contexto, n)
        return {'resposta': resposta, 'contexto': contexto, "n": n, "imagem":images_path}


blueprint.route('/teste', methods=['GET'])(testeChat)

# ProdutoController
blueprint.route('/update', methods=['POST'])(atualizarProdutosCarrinho)


@blueprint.route('/search/<string:id>', methods=['GET'])
def search(id):
    return buscarCarrinho(id)
