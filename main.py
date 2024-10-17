from conexao_db import abrir_conexao, fechar_conexao
def main():
   conexao = abrir_conexao()  
   if conexao is not None:
        try:
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM usuario")  # Consulta SQL
            resultados = cursor.fetchall()

            print("Lista de usuários:")
            for linha in resultados:
                print(linha)  # Aqui você pode formatar a saída como quiser
        except Exception as e:
            print(f"Erro ao executar o SELECT: {e}")
        finally:
            fechar_conexao(conexao)


if __name__ == "__main__":
    main()