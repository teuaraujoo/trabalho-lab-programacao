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


