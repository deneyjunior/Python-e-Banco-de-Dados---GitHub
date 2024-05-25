

def menu():
    while True:
        print("\n===== Gerenciador de Produtos =====")
        print("1. Criar novo produto")
        print("2. Ler produtos")
        print("3. Atualizar produto")
        print("4. Deletar produto")
        print("5. Sair")
        try:
            opcao = int(input("Escolha uma opção: "))
            if opcao in [1, 2, 3, 4, 5]:
                return opcao
            else:
                print("Opção inválida! Por favor, escolha uma opção de 1 a 5.")
        except ValueError:
            print("Entrada inválida! Por favor, insira um número.")

# Funções CRUD para o Gerenciador de Produtos
def criar_produto():
    # Implementar lógica para criar um novo produto
    print("Função de criar novo produto chamada.")

def ler_produtos():
    # Implementar lógica para ler produtos
    print("Função de ler produtos chamada.")

def atualizar_produto():
    # Implementar lógica para atualizar um produto
    print("Função de atualizar produto chamada.")

def deletar_produto():
    # Implementar lógica para deletar um produto
    print("Função de deletar produto chamada.")

