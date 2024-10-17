import mysql.connector
from mysql.connector import Error

def abrir_conexao():
    print('conexão aberta')
    """Cria e retorna uma conexão com o banco de dados MariaDB."""
    try:
        conexao = mysql.connector.connect(
            host='localhost',      # Altere para o host do seu banco
            database='db_tarantino',  # Altere para o nome do seu banco
            user='root',        # Altere para o seu usuário
            password='405713#mds!',       # Altere para a senha do seu banco
            collation='utf8mb4_unicode_ci'
        )
        if conexao.is_connected():
            print("Conexão com o banco de dados estabelecida!")
            return conexao
    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None


def fechar_conexao(conexao):
    print('conexão fechado')
    """Fecha a conexão com o banco de dados."""
    if conexao.is_connected():
        conexao.close()
        print("Conexão com o banco de dados fechada.")