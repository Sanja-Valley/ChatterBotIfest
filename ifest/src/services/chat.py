from services import produtoService, pixService, usuarioService
from datetime import datetime, date

carrinho = {
    "email": "",
    "nome": "",
    "cidade": "",
    "convidados": 0,
    "data": "",
    "carrinho": [],
    "total": 0
}


def respostas(recebido, contexto, n, email) -> tuple:
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

    if recebido.isspace() or not recebido:
        mensagem = "Por favor, digite uma mensagem"

    if not mensagem:
        mensagem = "Desculpe, não entendi."

    return mensagem, contexto, n


def geral(recebido, n):

    contexto = "geral"

    mensagem = "Você está no iFest! Qual o seu e-mail?"

    if (n == 1):
        carrinho["email"] = recebido

        usuario = usuarioService.buscarUsuario(recebido)

        if usuario == 0:
            mensagem = "Usuário não encontrado. Insira um e-mail válido."
            n = 0
        else:
            carrinho["nome"] = usuario
            mensagem = f"{usuario}, a festa é para quantos convidados?"

    if (n == 2):
        try:
            int(recebido)
            carrinho["convidados"] = recebido
            mensagem = "Em qual data será o evento?"
        except:
            mensagem = "Por favor, insira um número válido"
            n = 1

    if (n == 3):
        try:
            data = datetime.strptime(recebido, '%d/%m/%Y')
            if data.date() <= date.today():
                mensagem = "Por favor, insira uma data posterior a hoje"
                n = 2
            else:
                carrinho["data"] = recebido
                mensagem = "Em qual cidade será realizado o evento?"
        except ValueError:
            mensagem = "Por favor, insira uma data válida no formato dd/mm/aaaa"
            n = 2

    if (n == 4):
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
        mensagem = produtoService.recomendacao(str(carrinho['email'])) + "\nVoltar"
        contexto = "decoracao"

    if any(item in ("buffet", "comida") for item in recebido.split(",")):
        mensagem = "Qual você deseja contratar (valores por convidado): \nArroz e guarnição(R$8,00)\nBolo de corte(R$10,00)" \
                   "\nChurrasco(R$40,00)\nMassas(R$80,00)\nBebidas(R$15,00)\nVoltar"
        contexto = "buffet"

    if any(item in ("local", "lugar") for item in recebido.split(",")):
        mensagem = "Qual você deseja contratar: \n1.Chacára(R$1.000,00)\n2.Salão(R$800,00)\nVoltar|local"
        contexto = "local"

    if recebido == "voltar":
        mensagem = "Para finalizar a compra digite FINALIZAR " \
                   "\nEntre Decoração, Local e Buffet, qual você deseja escolher?"

    if recebido == "finalizar":
        contexto = "finalizar"

    return mensagem, contexto, n


def decoracao(recebido, n):
    mensagem = None
    contexto = "decoracao"

    recebido = recebido.replace(', ', ',')

    if recebido == "finalizar":
        contexto = "finalizar"
        return mensagem, contexto, n

    mensagem = "Item adicionado com sucesso! \nDigite VOLTAR para continuar comprando ou" \
               " FINALIZAR para encerrar a compra"
    carrinho["carrinho"].append({"item": str(produtoService.finalizar_carrinho(str(recebido))), "preco": 180.00})
    carrinho["total"] += 180.00

    return mensagem, contexto, n


def buffet(recebido, n):
    mensagem = None
    contexto = "buffet"
    qtd_convidados = int(carrinho["convidados"])

    if recebido:

        recebido = recebido.replace(', ', ',')

        if any(item in ("arroz e guarnição", "guarnição", "arroz") for item in recebido.split(",")):
            preco = 8 * qtd_convidados
            carrinho["carrinho"].append({"item": "Arroz e Guranição", "preco": preco})
            carrinho["total"] += preco

        if any(item in ("bolo de corte", "bolo") for item in recebido.split(",")):
            preco = 10 * qtd_convidados
            carrinho["carrinho"].append({"item": "Bolo de Corte", "preco": preco})
            carrinho["total"] += preco

        if any(item in ("churrasco", "carne") for item in recebido.split(",")):
            preco = 40 * qtd_convidados
            carrinho["carrinho"].append({"item": "Churrasco", "preco": preco})
            carrinho["total"] += preco

        if any(item in ("massas", "massa") for item in recebido.split(",")):
            preco = 80 * qtd_convidados
            carrinho["carrinho"].append({"item": "Massas", "preco": preco})
            carrinho["total"] += preco

        if any(item in ("bebidas", "bebida") for item in recebido.split(",")):
            preco = 15 * qtd_convidados
            carrinho["carrinho"].append({"item": "Bebidas", "preco": preco})
            carrinho["total"] += preco

        if recebido == "finalizar":
            contexto = "finalizar"

        mensagem = "Item adicionado com sucesso! \nDigite VOLTAR para continuar comprando ou" \
                   " FINALIZAR para encerrar a compra"

    return mensagem, contexto, n


def local(recebido, n):
    mensagem = None
    contexto = "local"

    recebido = recebido.replace(', ', ',')

    if recebido:

        if any(item in ("salão", "salao", "1") for item in recebido.split(",")):
            carrinho["carrinho"].append({"item": "Salão", "preco": 800.00})
            carrinho["total"] += 800.00

        if any(item in ("chácara", "chacara", "2") for item in recebido.split(",")):
            carrinho["carrinho"].append({"item": "Chácara", "preco": 1000.00})
            carrinho["total"] += 1000.00

        if recebido == "finalizar":
            contexto = "finalizar"

        mensagem = "Item adicionado com sucesso! \nDigite VOLTAR para continuar comprando ou" \
                   " FINALIZAR para encerrar a compra"

    return mensagem, contexto, n


def finalizar():
    c = produtoService.adicionarCarrinho(carrinho)
    if c:
        nome = c["nome"]
        convidados = c["convidados"]
        data = c["data"]
        cidade = c["cidade"]

        mensagem = f"{nome},\nDados da sua festa: \nQuantidade de Convidados: {convidados} \nData: {data} \nCidade: {cidade} \n\nProdutos Adquiridos:\n"
        for produto in c["carrinho"]:
            mensagem += f"{produto['item']} - R${produto['preco']}\n"

        mensagem += f"\nVALOR TOTAL:{c['total']} \nAgradecemos por realizar sua festa conosco!"
        pix = pixService.gerarPix()

        mensagem_pix = {
            'mensagem': mensagem,
            'pix': {
                'copia_cola': pix['payload'],
                'codigo_QR': pix['qr_code_image']

            }
        }

        return mensagem_pix

        return mensagem_pix

    else:
        return 'Não foi possível finalizar a compra.'


def termo_lgpd_chat(email: str):

    usuario = usuarioService.buscarUsuario(email)

    if usuario == 0:
        return False
    else:
        carrinho["nome"] = usuario
        return usuarioService.termo_lgpd(email=email)

