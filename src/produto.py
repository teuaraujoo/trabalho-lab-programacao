import uuid

produtos = []


def listar_produtos():
    if len(produtos) == 0:
        print("Nenhum produto cadastrado!")
    else:
        for produto in produtos:
            print(f"{produto['codigo']} - {produto['nome']} - R${produto['preco']:.2f}")
            if produto["descricao"] != "":
                print(f" {produto['descricao']}")


def cadastrar_produtos():
    print("\n Cadastro de Produto")

    nome = validar_nome(input("Nome do produto: "))
    while nome == False:
        print("Nome inválido! Mínimo de 3 letras.")
        nome = validar_nome(input("Nome do produto: "))

    if produto_existe(nome):
        print("Produto já cadastrado.")
        return

    descricao = validar_descricao(input("Descricao: "))
    while descricao == False:
        print("Descrição inválida! Mínimo de 5 letras.")
        descricao = validar_descricao(input("Descricao: "))

    preco = validar_preco(input("Preco: "))
    while preco == False:
        print("Preço inválido!")
        preco = validar_preco(input("Preco: "))

    produto = {
        "codigo": gerar_codigo(),
        "nome": nome,
        "descricao": descricao,
        "preco": preco
    }
    produtos.append(produto)
    print("Novo produto cadastrado:", produto["nome"])


def gerar_codigo():
    return str(uuid.uuid4())


def validar_nome(nome):
    nome = nome.strip()
    if len(nome) < 3:
        return False
    return nome


def validar_descricao(descricao):
    descricao = descricao.strip()
    if len(descricao) < 5:
        return False
    return descricao


def validar_preco(texto):
    texto = texto.replace(",", ".")
    try:
        preco = float(texto)
    except ValueError:
        return False
    if preco <= 0:
        return False
    return preco


def produto_existe(nome):
    for produto in produtos:
        if produto["nome"].lower() == nome.lower():
            return True
    return False


# def ler_preco():
    
#     while True:
#         texto = input("Preço: R$ ").replace(",", ".")
#         try:
#             preco = float(texto)
#         except ValueError:
#             print("Preço inválido! Ex.: 4.99 ou 4,99")
#             continue

#         if preco <= 0:
#             print("O preço precisa ser maior que zero!")
#             continue

#         return preco



