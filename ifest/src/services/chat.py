def respostas(recebido, contexto) -> tuple:
    recebido = recebido.lower()

    contextos = {
        "geral": geral,
        "decoracao": decoracao,
        "buffet": buffet,
        "local": local,
        "menu": menu
    }

    if recebido == "voltar" and contexto not in ("geral", "menu") in recebido:
        contexto = "menu"

    mensagem, contexto = contextos[contexto](recebido)

    if not mensagem:
        mensagem = "Desculpe, não entendi."

    return mensagem, contexto


def geral(recebido):
    mensagem = None
    contexto = "geral"

    if recebido in ("oi", "olá", "aoba", "manda"):
        mensagem = "Olá, a festa é para 50, 100, 150 ou 200 convidados?"

    if recebido in ("50", "100", "150", "200"):
        mensagem = "Em qual mês deseja realizar o evento?"

    if recebido in ("janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"):
        mensagem = "O evento será em São José dos Campos ou Jacareí?"

    if recebido in ("são josé dos campos", "jacareí", "jacarei", "sao jose dos campos", "sjc", "sanja", "jacacity"):
        mensagem = "Entre Decoração, Local e Buffet, qual você deseja escolher?"
        contexto = "menu"

    return mensagem, contexto

def menu(recebido):
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
    return mensagem, contexto


def decoracao(recebido):
    mensagem = None
    contexto = "decoracao"

    if any(item in ("arco de balões", "arco") for item in recebido.split(",")):
        mensagem = "Item adicionado com sucesso! \nDigite VOLTAR para continuar comprando ou FINALIZAR a compra"

    if any(item in ("bolo fake", "bolo") for item in recebido.split(",")):
        mensagem = "Item adicionado com sucesso! \nDigite VOLTAR para continuar comprando ou FINALIZAR a compra"

    if any(item in ("kit de móveis provençais", "kit", "provençal", "móvel", "movel", "moveis", "móveis") for item in recebido.split(",")):
        mensagem = "Item adicionado com sucesso! \nDigite VOLTAR para continuar comprando ou FINALIZAR a compra"

    if any(item in ("painel de tecido", "tecido", "painel") for item in recebido.split(",")):
        mensagem = "Item adicionado com sucesso! \nDigite VOLTAR para continuar comprando ou FINALIZAR a compra"

    if recebido == "finalizar":
        contexto = "geral"

    return mensagem, contexto


def buffet(recebido):
    mensagem = None
    contexto = "buffet"

    if any(item in ("arroz e guarnição", "guarnição", "arroz") for item in recebido.split(",")):
        mensagem = "Item adicionado com sucesso! \nDigite VOLTAR para continuar comprando ou FINALIZAR para compra"
        
    if any(item in ("bolo de corte", "bolo") for item in recebido.split(",")):
        mensagem = "Item adicionado com sucesso! \nDigite VOLTAR para continuar comprando ou FINALIZAR a compra"
        
    if any(item in ("churrasco", "carne") for item in recebido.split(",")):
        mensagem = "Item adicionado com sucesso! \nDigite VOLTAR para continuar comprando ou FINALIZAR a compra"
        
    if ("massas",) in recebido:
        mensagem = "Item adicionado com sucesso! \nDigite VOLTAR para continuar comprando ou FINALIZAR a compra"

    if ("bebidas",) in recebido:
        mensagem = "Item adicionado com sucesso! \nDigite VOLTAR para continuar comprando ou FINALIZAR a compra"

    if recebido == "finalizar":
        contexto = "geral"

    return mensagem, contexto


def local(recebido):
    mensagem = None
    contexto = "local"

    if ("salão") in recebido:
        mensagem = "Item adicionado com sucesso! \nDigite VOLTAR para continuar comprando ou FINALIZAR a compra"

    if ("chacara", "chácara") in recebido:
        mensagem = "Item adicionado com sucesso! \nDigite VOLTAR para continuar comprando ou FINALIZAR a compra"

    if recebido == "finalizar":
        contexto = "geral"

    return mensagem, contexto
