# validador de CPF
# limpar telefone e validar
# limpar nome
# verificar se o cliente ja esta cadastro ***

# 1. Formato e Tamanho
# • O CPF deve possuir exatamente 11 dígitos numéricos.
# • Se houver máscara (como ###.###.###-##), os pontos e o traço devem ser removidos para considerar apenas os números.

# 2. Dígitos Iguais (Sequências Inválidas)
# • CPFs com todos os números iguais (como 000.000.000-00, 111.111.111-11, etc.) são considerados inválidos, embora matematicamente passem no cálculo.

# 3. Cálculo do 1º Dígito Verificador
# • Pega-se os 9 primeiros dígitos do CPF.
# • Multiplica-se cada dígito, da esquerda para a direita, por pesos decrescentes de 10 a 2.
# • Soma-se todos os resultados das multiplicações.
# • Multiplica-se a soma por 10 e divide-se por 11 para obter o resto da divisão (ou faz-se soma % 11).
# • Se o resto for menor que 2 (0 ou 1), o primeiro dígito verificador deve ser 0.
# • Se o resto for 2 ou mais, o dígito será 11 menos o resto.
# • O resultado deve ser igual ao 10º dígito do CPF.

# 4. Cálculo do 2º Dígito Verificador
# • Pega-se os 10 primeiros dígitos do CPF (os 9 iniciais mais o 1º dígito verificador já validado).
# • Multiplica-se cada dígito, da esquerda para a direita, por pesos decrescentes de 11 a 2.
# • Soma-se os produtos, multiplica-se por 10 e tira-se o resto da divisão por 11.
# • Aplica-se a mesma regra: se o resto for menor que 2, o dígito é 0; caso contrário, é 11 menos o resto.

# def limpar_cpf(cpf) # parametro de uma funcao
# cpfLimpo = limpar_cpf("065.265.075-90") # argumento de uma funcao

clientes = [] 

def limpar_nome(nome):
    palavras = nome.split()
    nome_limpo = " ".join(palavras)
    return nome_limpo.title()

def validar_telefone(telefone):
    telefone = limpar_telefone(telefone)

    if len(telefone) != 10 and len(telefone) !=11:
        return False

    if telefone[0] == "0":
        return False

    if len(telefone) == 11 and telefone[2] != "9":
        return False

def limpar_telefone(telefone):
    numeros = ""

    for caractere in telefone:
        if caractere.isdigit():
            numeros += caractere

    return numeros

def validar_cpf(cpf):
    cpf = cpf.replace(".","").replace("-","").strip()

    if not cpf.isdigit():
        return False

    if len(cpf) !=11:
        return False

    if cpf == cpf[0]*11:
        return False

    if int(cpf[9]) != calcular_primeiro_digito(cpf):
        return False

    if int(cpf[10]) != calcular_segundo_digito(cpf):
        return False

    return True

def calcular_primeiro_digito(cpf):
    nove_primeiros = cpf[:9]
    soma = 0 
    peso = 10 

    for digito in nove_primeiros:
        soma += int(digito) * peso
        peso -= 1

    resto = soma % 11

    if resto < 2:
        return 0 
    else:
        return 11 - resto 

def calcular_segundo_digito(cpf):
    dez_primeiros = cpf[:10]
    soma = 0
    peso = 11

    for digito in dez_primeiros:
        soma += int(digito) * peso
        peso -= 1

    resto = soma % 11

    if resto <2:
        return 0
    else:
        return 11 - resto
        
def cadastrar_clientes():
# verificar se ja exsite cliente no arrayu
# se exister retorna o encontrado
# se nao exister cadastra o novo cliente e retorna o novo cliente cadastrado
    cpf = input("CPF: ")
    while not validar_cpf(cpf):
        print("CPF inválido!")
        cpf = input("CPF: ")
    cpf = cpf.replace(".", "").replace("-", "").strip()

    for cliente in clientes:
        if cliente["cpf"] == cpf:
            print("Cliente já cadastrado:", cliente["nome"])
            return cliente

    nome = limpar_nome(input("Nome: "))
    while nome == "":
        print("Nome não pode ficar vazio!")
        nome = limpar_nome(input("Nome: "))

    telefone = input("Telefone: ")
    while not validar_telefone(telefone):
        print("Telefone inválido!")
        telefone = input("Telefone: ")
    telefone = limpar_telefone(telefone)


    cliente = {
        "nome": nome,
        "telefone": telefone,
        "cpf": cpf
    }

    clientes.append(cliente)
    print("Cliente cadastrado com sucesso! ", clientes)
    return