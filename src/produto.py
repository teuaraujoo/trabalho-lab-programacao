import uuid

produtos = []

def listar_produtos():
    if len(produtos) == 0: 
        print("Nenhum produto cadastrado!")
    else :
        for produto in produtos :
            print(f"{produto['codigo']} - {produto['nome']} - R${produto['preço']:.2f }")
            if produto["descricao"] != "":
                print(f" {produto['descricao']}")

def cadastrar_produto():
    print("\n Cadastro de Produto")
    identificador = gerar_codigo()
    nome = input("Nome do produto: ")
    descricao = input("Descricao: ")
    preco = float(input("Preco: ").replace(",", "."))
    
    produto  = {
        "codigo": identificador,
        "nome": validar_nome(nome),
        "descricao": validar_descricao(descricao),
        "preco": validar_preco(preco)
    }
    
    if produto_existe(produto["nome"]):
        print("Produto já cadastrado.")
    else:
        produtos.append(produto)
        
    print("Novo produto cadastrado: ", produtos)
    return;

def gerar_codigo():
    return str(uuid.uuid4())

def validar_nome(nome):
    if nome.strip() == "":
        return False

    if len(nome) < 3:
        return False

    return nome

def validar_descricao(descricao):
    if descricao.strip() == "":
        return False

    if len(descricao) < 5:
        return False

    return descricao

def validar_preco(preco):
    if preco <= 0:
        return False

    return preco

def produto_existe(nome):
    for produto in produtos:
        if produto["nome"].lower() == nome:
            return True
    
    return False
        
cadastrar_produto()


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



