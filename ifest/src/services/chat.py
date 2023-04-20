from services import produtoService

carrinho = {
  "nome": "",
  "cidade": "",
  "convidados": 0,
  "data": "",
  "carrinho": [],
  "total": 0
}

def respostas(recebido, contexto, n) -> tuple:
    recebido = recebido.lower()

    contextos = {
        "geral": geral,
        "decoracao": decoracao,
        "buffet": buffet,
        "local": local,
        "menu": menu
    }

    if recebido == "voltar" and contexto not in ("geral", "menu"):
        contexto = "menu"
    
    mensagem, contexto, n = contextos[contexto](recebido, n)

    if not mensagem:
        mensagem = "Desculpe, não entendi."

    return mensagem, contexto, n


def geral(recebido, n):
    mensagem = None
    contexto = "geral"

    if recebido in (
            "oi",
            "olá",
            "aoba",
            "manda",
            "bom dia",
            "boa tarde",
            "boa noite"):
        mensagem = "Bem vindo(a) ao iFest! Qual o seu nome?"
    
    if(n == 1):
        carrinho["nome"] = recebido
        mensagem = f"{recebido}, A festa é para quantos convidados?"

    if(n == 2):
        carrinho["convidados"] = recebido
        mensagem = "Em qual data será o evento?"
    
    if(n == 3):
        carrinho["data"] = recebido
        mensagem = "Em qual cidade será realizado o evento?"

    if(n == 4):
        carrinho["cidade"] = recebido
        mensagem = "Entre Decoração, Local e Buffet, qual você deseja escolher?"
        contexto = "menu"

    n += 1
    return mensagem, contexto, n

def menu(recebido, n):
    n = 0
    mensagem = None
    contexto = "menu"

    if any(item in ("decoração", "decoracao") for item in recebido.split(",")):
        mensagem = "Qual você deseja contratar: \nArco de balões(R$180,00)\nBolo fake(R$50,00)\nKit de móveis provençais(R$180,00)\nPainel de balões(R$130,00)\nPainel de tecido(R$100,00)\nVoltar"
        contexto = "decoracao"

    if any(item in ("buffet", "comida") for item in recebido.split(",")):
        mensagem = "Qual você deseja contratar: \nArroz e guarnição(R$300,00)\nBolo de corte(R$100,00)\nChurrasco(R$400,00)\nMassas(R$300,00)\nBebidas(R$500,00)\nVoltar"
        contexto = "buffet"

    if any(item in ("local", "lugar")for item in recebido.split(",")):
        mensagem = "Qual você deseja contratar: \nSalão(R$800,00)\nChacára(R$1.000,00)\nVoltar"
        contexto = "local"
        
    if recebido == "voltar":
        mensagem = "Para finalizar a compra digite FINALIZAR \nEntre Decoração, Local e Buffet, qual você deseja escolher?"

    if recebido == "finalizar":
        contexto = "finalizar"

    return mensagem, contexto, n


def decoracao(recebido, n):
    mensagem = None
    contexto = "decoracao"

    recebido = recebido.replace(', ', ',')

    if any(item in ("arco de balões", "arco") for item in recebido.split(",")):
        mensagem = "Item adicionado com sucesso! \nDigite VOLTAR para continuar comprando ou FINALIZAR a compra"
        carrinho["carrinho"].append({"item": "Arco de Balões", "preco": 180.00})
        carrinho["total"] += 180.00

    if any(item in ("bolo fake", "bolo") for item in recebido.split(",")):
        mensagem = "Item adicionado com sucesso! \nDigite VOLTAR para continuar comprando ou FINALIZAR a compra"
        carrinho["carrinho"].append({"item": "Bolo Fake", "preco": 50.00})
        carrinho["total"] += 50.00


    if any(item in ("kit de móveis provençais", "kit", "provençal", "móvel", "movel", "moveis", "móveis") for item in recebido.split(",")):
        mensagem = "Item adicionado com sucesso! \nDigite VOLTAR para continuar comprando ou FINALIZAR a compra"
        carrinho["carrinho"].append({"item": "Kit de Móveis Provençais", "preco": 180.00})
        carrinho["total"] += 180.00

    if any(item in ("painel de tecido", "tecido") for item in recebido.split(",")):
        mensagem = "Item adicionado com sucesso! \nDigite VOLTAR para continuar comprando ou FINALIZAR a compra"
        carrinho["carrinho"].append({"item": "Painel de Tecido", "preco": 100.00})
        carrinho["total"] += 100.00
    
    if any(item in ("painel de balões", "balões") for item in recebido.split(",")):
        mensagem = "Item adicionado com sucesso! \nDigite VOLTAR para continuar comprando ou FINALIZAR a compra"
        carrinho["carrinho"].append({"item": "Painel de Balões", "preco": 130.00})
        carrinho["total"] += 100.00

    if recebido == "finalizar":
        contexto = "finalizar"

    return mensagem, contexto, n


def buffet(recebido, n):
    mensagem = None
    contexto = "buffet"

    if recebido:
    
        recebido = recebido.replace(', ', ',')

        if any(item in ("arroz e guarnição", "guarnição", "arroz") for item in recebido.split(",")):
            carrinho["carrinho"].append({"item": "Arroz e Guranição", "preco": 300.00})
            carrinho["total"] += 300.00

        if any(item in ("bolo de corte", "bolo") for item in recebido.split(",")):
            carrinho["carrinho"].append({"item": "Bolo de Corte", "preco": 100.00})
            carrinho["total"] += 100.00
            
        if any(item in ("churrasco", "carne") for item in recebido.split(",")):
            carrinho["carrinho"].append({"item": "Churrasco", "preco": 400.00})
            carrinho["total"] += 400.00

        if any(item in ("massas", "massa") for item in recebido.split(",")):
            carrinho["carrinho"].append({"item": "Massas", "preco": 300.00})
            carrinho["total"] += 300.00

        if any(item in ("bebidas", "bebida") for item in recebido.split(",")):
            carrinho["carrinho"].append({"item": "Bebidas", "preco": 500.00})
            carrinho["total"] += 500.00

        if recebido == "finalizar":
            contexto = "finalizar"
    
        mensagem = "Item adicionado com sucesso! \nDigite VOLTAR para continuar comprando ou FINALIZAR a compra"

    return mensagem, contexto, n


def local(recebido, n):
    mensagem = None
    contexto = "local"

    recebido = recebido.replace(', ', ',')

    if recebido:

        if any(item in ("salão", "salao") for item in recebido.split(",")):
            carrinho["carrinho"].append({"item": "Salão", "preco": 800.00})
            carrinho["total"] += 800.00

        if any(item in ("chácara", "chacara") for item in recebido.split(",")):
            carrinho["carrinho"].append({"item": "Chácara", "preco": 1000.00})
            carrinho["total"] += 1000.00

        if recebido == "finalizar":
            contexto = "finalizar"

        mensagem = "Item adicionado com sucesso! \nDigite VOLTAR para continuar comprando ou FINALIZAR a compra"

    return mensagem, contexto, n

def finalizar():
    return produtoService.adicionarCarrinho(carrinho)