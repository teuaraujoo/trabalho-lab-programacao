# TODO:
    # carrinho
    # init py
    # verificar se tem poroduto cadastrado, caso nao tenha bloquear compra
    # fazer fluxo de compra -> array do carrinho
    # testes
        # caso der tempo (feat):
            # validacao de CNPJ caso cliente selecione CNPJ + cadastro de cliente CNPJ
            # cupons de desconto e/ou desconto de produtos (flag se produto esta em desconto + procentaem de desconto -> fazer calculo em pagamento)
            # vencimento de produto -> impedir venda + dar desconto
            # exclusao e edicao de clientes e produtos (CRUD COMPLETO)
            # permitir pagamento internacional (conversao de moedas)
            # possibilidade de gerar qr code com alguma lib python (para pagamento PIX)    
            # codigo de barras -> identificacao do produto pelo codigo de barras dele (digitado)
            # simulacao de pesagem de produto
    
import sys
from pathlib import Path

# Garante que os módulos de src/ se importem entre si (python src/main.py ou python -m src.main)
sys.path.insert(0, str(Path(__file__).resolve().parent))

from carrinho import selecionar_produtos, finalizar_carrinho, mostrar_carrinho, carrinho
from cliente import cadastrar_clientes
from produto import cadastrar_produtos, listar_produtos, produtos

def escolher_produto():
    if len(produtos) == 0:
        print("Nenhum produto cadastrado! Compra bloqueada.")
        return
    selecionar_produtos()
    if len(carrinho) > 0:
        mostrar_carrinho()

def pagar_carrinho():
    resultado = finalizar_carrinho()
    if resultado["sucesso"]:
        print(f"\n{resultado['mensagem']}")
        print(f"Total pago: R$ {resultado['total']:.2f} ({resultado['metodo']})")
        if "comprovante" in resultado:
            print(f"Comprovante PIX: {resultado['comprovante']}")
    else:
        print(f"\nPagamento não realizado: {resultado['mensagem']}")

def menu_cliente():
    while True:
        print("\nMenu do cliente")
        print("1 - Listar produtos\n2 - Escolher produto\n3 - Pagar\n4 - Voltar")
        escolha = input("Escolha uma opção: ").strip()
        if escolha == "1":
            listar_produtos()
        elif escolha == "2":
            escolher_produto()
        elif escolha == "3":
            pagar_carrinho()
        elif escolha == "4":
            return
        else:
            print("Opção inválida!")

def menu_administrador():
    while True:
        print("\nMenu do administrador")
        print("1 - Cadastrar cliente\n2 - Cadastrar produto\n3 - Voltar")
        escolha = input("Escolha uma opção: ").strip()
        if escolha == "1":
          cadastrar_clientes()
        elif escolha == "2":
            cadastrar_produtos()
        elif escolha == "3":
            return
        else:
            print("Opção inválida!")

def menu():
    while True:
        print("\nSistema de Supermercado")
        print("1 - Cliente\n2 - Administrador\n3 - Sair")
        escolha = input("Escolha seu perfil: ").strip()
        if escolha == "1":
            menu_cliente()
        elif escolha == "2":
            menu_administrador()
        elif escolha == "3":
            print("Sistema encerrado")
            return
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu()
