import unicodedata

class Item:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Menu:
    def __init__(self, items: dict):
        self.items = items

    @staticmethod
    def normalizar(string: str):
        return unicodedata.normalize('NFKD', string).encode('ASCII', 'ignore').decode('utf-8').lower()

    def iniciar(self, carrinho: list):
        escolha: str = ''

        while escolha != 'voltar':
            for numero, item in self.items.items():
                print(f"{numero} - {item.nome}")

            escolha =self.normalizar(input("\nDigite os itens que deseja adicionar ao carrinho ou voltar: "))

            getEscolhas = escolha.split(", ")

            # Verificar se o produto existe no dicionário de produtos
            if escolha != 'voltar':
                for e in getEscolhas:
                    if e not in self.items:
                        print('\nProduto não encontrado.\n')
                        continue
                    else:
                        item_escolhido = self.items[e]
                        carrinho.append(item_escolhido)
                        print(f'Item: {item_escolhido.nome} adicionado ao carrinho.')
