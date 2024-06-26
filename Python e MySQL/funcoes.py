import mysql.connector
from mysql.connector import Error
from tabulate import tabulate

# Função para conectar ao banco de dados
def conectar():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1a2b",
            database="pmysql"
        )
        if conn.is_connected():
            print("Conexão ao banco de dados MySQL foi bem-sucedida.")
            return conn
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None

# Função para desconectar do banco de dados
def desconectar(conn):
    if conn.is_connected():
        conn.close()
        print("Conexão ao MySQL foi encerrada.")

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

# Função para criar um novo produto
def criar_produto():
    conn = conectar()
    if conn:
        cursor = conn.cursor()
        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: "))
        estoque = int(input("Digite a quantidade do produto: "))
        try:
            cursor.execute("INSERT INTO produtos (nome, preco, estoque) VALUES (%s, %s, %s)", (nome, preco, estoque))
            conn.commit()
            print("Produto criado com sucesso!")
        except Error as e:
            print(f"Erro ao criar produto: {e}")
        finally:
            cursor.close()
            desconectar(conn)

# Função para ler produtos
def ler_produtos():
    conn = conectar()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM produtos")
            resultados = cursor.fetchall()
            print(tabulate(resultados, headers=["ID", "Nome", "Preço", "Estoque"], tablefmt="pretty"))
        except Error as e:
            print(f"Erro ao ler produtos: {e}")
        finally:
            cursor.close()
            desconectar(conn)

# Função para atualizar um produto
def atualizar_produto():
    conn = conectar()
    if conn:
        cursor = conn.cursor()
        id_produto = int(input("Digite o ID do produto a ser atualizado: "))
        nome = input("Digite o novo nome do produto: ")
        preco = float(input("Digite o novo preço do produto: "))
        estoque = int(input("Digite a nova quantidade do produto: "))
        try:
            cursor.execute("UPDATE produtos SET nome=%s, preco=%s, estoque=%s WHERE id=%s", (nome, preco, estoque, id_produto))
            conn.commit()
            print("Produto atualizado com sucesso!")
        except Error as e:
            print(f"Erro ao atualizar produto: {e}")
        finally:
            cursor.close()
            desconectar(conn)

# Função para deletar um produto
def deletar_produto():
    conn = conectar()
    if conn:
        cursor = conn.cursor()
        id_produto = int(input("Digite o ID do produto a ser deletado: "))
        try:
            cursor.execute("DELETE FROM produtos WHERE id=%s", (id_produto,))
            conn.commit()
            print("Produto deletado com sucesso!")
        except Error as e:
            print(f"Erro ao deletar produto: {e}")
        finally:
            cursor.close()
            desconectar(conn)
