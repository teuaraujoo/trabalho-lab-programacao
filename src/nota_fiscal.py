# receber dados dos cliente
# receber dados da operaca - preco e descricao
# colocar data da operacao Date now()
#  UUID aleatório
# **buscar** informações da empresa

from datetime import datetime
import uuid
from empresa import empresa

def gerarNotaFiscal(nome, telefone, cpf, preco, descricao):
    data = datetime.now()
    identificador = str(uuid.uuid4())

    dadosCliente = {
        "nome": nome,
        "telefone": telefone,
        "cpf": cpf
    }

    dadosCompra = {
        "identificador": identificador,
        "data": data.strftime("%d/%m/%Y %H:%M"),
        "preco": preco,
        "descricao": descricao,
    }

    return printarNotaFiscal(empresa, dadosCliente, dadosCompra)


def printarNotaFiscal(dadosEmpresa, dadosCliente, dadosCompra):
        print("======================================")
        print("              NOTA FISCAL             ")
        print("======================================")
        print("EMPRESA") 
        print()
        print("Nome: ", dadosEmpresa["Nome"]) 
        print("CNPJ: ", dadosEmpresa["CNPJ"]) 
        print("Telefone: ", dadosEmpresa["Telefone"]) 
        print("--------------------------------------")
        print("CLIENTE") 
        print()
        print("Nome: ", dadosCliente["nome"]) 
        print("CPF: ", dadosCliente["cpf"]) 
        print("Telefone: ", dadosCliente["telefone"]) 
        print("--------------------------------------")
        print("COMPRA") 
        print()
        print("Numero: ", dadosCompra["identificador"]) 
        print("Data: ", dadosCompra["data"]) 
        print("Descricao: ", dadosCompra["descricao"]) 
        print("--------------------------------------")
        print("TOTAL: R$", dadosCompra["preco"])
        print("======================================")
        print("      OBRIGADO PELA PREFERENCIA!      ")
        print("======================================")