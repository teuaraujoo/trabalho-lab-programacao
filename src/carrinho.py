# cliente selecionou produto -> adiciona no carrinho
#  selecionar metodo de pagaamento
# quando cliente parar de selecionar produto  
# jogar infos para pagamento
# retornar sucesso ou erro


from produto import produtos
from src.pagamento import Metodos, ler_numero, calcular_total, ler_pagamento




carrinho = []



def adicionar_ao_carrinho(produto, quantidade):
    for item in carrinho:
        if item["codigo"] == produto["codigo"]:
            item["quantidade"] += quantidade
            return

    item = {
        "codigo": produto["codigo"],
        "nome": produto["nome"],
        "preco": produto["preco"],
        "quantidade": quantidade
    }
    carrinho.append(item)


def carrinho_para_pagamento():
    
    lista = []
    for item in carrinho:
        lista.append((item["nome"], item["quantidade"], item["preco"]))
    return lista


def mostrar_carrinho():
    print("\n--- Carrinho ---")
    for item in carrinho:
        subtotal = item["preco"] * item["quantidade"]
        print(f"{item['quantidade']}x {item['nome']} - R$ {subtotal:.2f}")



def selecionar_produtos():
    while True:
        print("\nProdutos disponíveis:")
        numero = 1
        for produto in produtos:
            print(f"{numero} - {produto['nome']} - R$ {produto['preco']:.2f}")
            numero += 1

        escolha = ler_numero("Número do produto (0 para finalizar): ", int)
        if escolha == 0:
            break

        if escolha > len(produtos):
            print("Produto não encontrado!")
            continue

        quantidade = ler_numero("Quantidade: ", int)
        if quantidade == 0:
            print("Quantidade inválida!")
            continue

        produto = produtos[escolha - 1]
        adicionar_ao_carrinho(produto, quantidade)
        print(f"{quantidade}x {produto['nome']} adicionado!")


def pagar(total, metodo):
    """Recebe as infos do pagamento e retorna sucesso ou erro."""
    if metodo == Metodos.Dinheiro:
        recebido = ler_numero(f"Valor recebido (total R$ {total:.2f}): R$ ", float)

        if recebido < total:
            return {"sucesso": False, "mensagem": "Valor insuficiente."}

        troco = recebido - total
        return {"sucesso": True, "mensagem": f"Pago em dinheiro. Troco: R$ {troco:.2f}"}

    
    return {"sucesso": True, "mensagem": f"Pagamento aprovado via {metodo.value}."}



def finalizar_carrinho():
    if len(carrinho) == 0:
        return {"sucesso": False, "mensagem": "Carrinho vazio."}

    mostrar_carrinho()
    total = round(calcular_total(carrinho_para_pagamento()), 2)
    print(f"Total: R$ {total:.2f}")

    metodo = ler_pagamento()
    resultado = pagar(total, metodo)

    resultado["total"] = total
    resultado["metodo"] = metodo.value
    resultado["itens"] = list(carrinho)

    if resultado["sucesso"]:
        carrinho.clear()  

    return resultado