# cliente selecionou produto -> adiciona no carrinho
#  selecionar metodo de pagaamento
# quando cliente parar de selecionar produto  
# jogar infos para pagamento
# retornar sucesso ou erro


from produto import produtos
from cliente import identificar_cliente
from empresa import empresa
from gerar_qrcode import gerarQrCodePixCobranca, gerarQrCodeComprovante
from pagamento import Metodos, ler_numero, calcular_total, ler_pagamento

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

        produto = produtos[int(escolha) - 1]
        adicionar_ao_carrinho(produto, quantidade)
        print(f"{quantidade}x {produto['nome']} adicionado!")


def descricao_da_compra():
    return ", ".join(f"{item['quantidade']}x {item['nome']}" for item in carrinho)


def montar_dados_pix(total, descricao, status, cliente=None):
    dados = (
        f"chave_pix_empresa={empresa['Chave PIX']};"
        f"valor={total:.2f};descricao={descricao};status={status}"
    )
    if cliente is not None:
        dados += f";chave_pix_cliente={cliente['cpf']};cliente={cliente['nome']}"
    return dados


def pagar_pix(total):
    cliente = identificar_cliente()
    if cliente is None:
        return {"sucesso": False, "mensagem": "Cliente não identificado."}

    descricao = descricao_da_compra()
    cobranca = gerarQrCodePixCobranca(
        cliente, montar_dados_pix(total, descricao, "PENDENTE")
    )

    confirmacao = input("Pagamento realizado? (s/n): ").strip().lower()
    if confirmacao != "s":
        return {"sucesso": False, "mensagem": "Pagamento PIX não confirmado.", "cobranca": str(cobranca)}

    comprovante = gerarQrCodeComprovante(
        cliente, montar_dados_pix(total, descricao, "PAGO", cliente)
    )
    return {
        "sucesso": True,
        "mensagem": "Pagamento aprovado via pix.",
        "cliente": cliente,
        "cobranca": str(cobranca),
        "comprovante": str(comprovante),
    }


def pagar(total, metodo):
    """Recebe as infos do pagamento e retorna sucesso ou erro."""
    if metodo == Metodos.Dinheiro:
        recebido = ler_numero(f"Valor recebido (total R$ {total:.2f}): R$ ", float)

        if recebido < total:
            return {"sucesso": False, "mensagem": "Valor insuficiente."}

        troco = recebido - total
        return {"sucesso": True, "mensagem": f"Pago em dinheiro. Troco: R$ {troco:.2f}"}

    if metodo == Metodos.Pix:
        return pagar_pix(total)

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