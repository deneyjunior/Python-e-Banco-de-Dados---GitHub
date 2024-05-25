from funcoes import *

# Programa
if __name__ == "__main__":
    while True:
        escolha = menu()
        if escolha == 1:
            criar_produto()
        elif escolha == 2:
            ler_produtos()
        elif escolha == 3:
            atualizar_produto()
        elif escolha == 4:
            deletar_produto()
        elif escolha == 5:
            print("Saindo do programa...")
            break