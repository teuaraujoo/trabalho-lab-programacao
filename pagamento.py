from enum import Enum


class Metodos(Enum):
    Dinheiro = "dinheiro"
    Pix = "pix"
    Cartao = "cartao"


def ler_numero(mensagem, tipo=float):
    while True:
        try:
            valor = tipo(input(mensagem))

            if valor < 0:
                print("Digite um numero maior ou igual a 0.")
                continue

            return valor

        except ValueError:
            print("Valor inválido, tente novamente.")


def calcular_total(produtos):
    total = 0

    for produto in produtos:
        quantidade = produto[1]
        preco = produto[2]

        total += quantidade * preco

    return total


def validar_pagamento(metodo):
    metodo = metodo.strip().lower()

    if metodo == Metodos.Dinheiro.value:
        return Metodos.Dinheiro

    elif metodo == Metodos.Pix.value:
        return Metodos.Pix

    elif metodo == Metodos.Cartao.value:
        return Metodos.Cartao

    else:
        return None


def ler_pagamento():
    while True:
        metodo = input(
            "Forma de pagamento (pix, cartao ou dinheiro): "
        )

        pagamento = validar_pagamento(metodo)

        if pagamento is not None:
            return pagamento
        
        print("Método de pagamento inválido, tente novamente.")


def main():
    produtos = []

    quantidade_produtos = ler_numero(
        "Quantos produtos deseja cadastrar? ", int
    )

    for _ in range(quantidade_produtos):
        nome = input("Nome do produto: ")
        quantidade = ler_numero("Quantidade do produto: ", int)
        preco = ler_numero("Preço do produto: R$ ", float)

        produtos.append((nome, quantidade, preco))

    total = calcular_total(produtos)

    print(f"\nTotal da compra: R$ {total:.2f}")

    pagamento = ler_pagamento()

    print(f"Pagamento escolhido: {pagamento.value}")
    print("Pagamento válido!")


if __name__ == "__main__":
    main()