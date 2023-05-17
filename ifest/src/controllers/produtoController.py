from flask import request, jsonify
from services import produtoService

#Atualiza lista de produtos de um carrinho e o valor total
def atualizarProdutosCarrinho():
    carrinhoProduto = request.get_json()
    verificaCarrinho = 0
    if("_id" in carrinhoProduto):
        buscarCarrinho(carrinhoProduto['_id'])
        carrinhoAtualizado = produtoService.atualizarCarrinho(carrinhoProduto, carrinhoProduto["_id"])
        return carrinhoAtualizado
    else:
        carrinhoAdicionado = adicionarCarrinho(carrinhoProduto)
        return carrinhoAdicionado

#Adiciona o carrinho criando um novo ID
def adicionarCarrinho(carrinho):
    carrinhoAdicionado = produtoService.adicionarCarrinho(carrinho)
    return carrinhoAdicionado

#Busca o carrinho pelo ID
def buscarCarrinho(carrinhoId):
    verificaCarrinho = produtoService.buscarCarrinho(carrinhoId)
    if(verificaCarrinho == 0):
        return jsonify({'message': 'Carrinho não encontrado.'}), 404
    else:
        return verificaCarrinho

