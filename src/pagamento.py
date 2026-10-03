# quantidade de produtos * valor do produto -> retornar resultado final
# validar tipo de pagamento com base no enum
# Importar Nota Fiscal depois

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
                c
            return valor
        except ValueError:
            print("Valor inválido, tente novamente.")


    def main():
    produtos = []
 
    quantidade_produtos = ler_numero("Quantos produtos deseja cadastrar? ", int)
 
    for _ in range(quantidade_produtos):
        nome = input("Nome do produto: ")
        quantidade = ler_numero("Quantidade: ", int)
        preco = ler_numero("Preço: ", float)
 
        produtos.append((nome, quantidade, preco))
 
    pagamento = ler_pagamento()
    print(f"Pagamento escolhido: {pagamento.value}")
    print("Pagamento válido!")
 
 
if __name__ == "__main__":
    main()

        metodo = input("Forma de pagamento (pix, cartao ou dinheiro): ")
        pagamento = validar_pagamento(metodo)
 
        if pagamento is not None:
            return pagamento
 
        print("Método de pagamento inválido, tente novamente.")





