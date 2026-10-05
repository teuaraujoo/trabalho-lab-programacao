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
    
if __package__:
    from ..cliente import cadastrar_clientes
    from ..produto import cadastrar_produtos, listar_produtos
else:
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from cliente import cadastrar_clientes
    from produto import cadastrar_produtos, listar_produtos


def menu_cliente():
    while True:
        print("\nMenu do cliente")
        print("1 - Listar produtos\n2 - Escolher produto\n3 - Pagar\n4 - Voltar")
        escolha = input("Escolha uma opção: ").strip()
        if escolha == "1":
            listar_produtos()
        elif escolha == "2":
            print("A escolha de produtos ainda será implementada.")
        elif escolha == "3":
            print("O pagamento ainda será implementado.")
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
