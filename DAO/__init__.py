import psycopg2

# Estabelecendo a conexão com o Banco de dados
def conectardb():
    conexao = psycopg2.connect(database="minicursobd",
                               host="localhost",
                               user="postgres",
                               password="leonmelhorprof",
                               port="5432")
    print("Conexao realizada com sucesso")
    return conexao

# Chame a função para testar a conexão
conexao = conectardb()

def inserir_usuario(nome, email):
    conexao = conectardb()                  # Estabelece conexão com o banco de dados.
    cursor = conexao.cursor()             # Cria um cursor para executar comandos SQL.
    cursor.execute("INSERT INTO usuarios (nome, email) VALUES (%s, %s)", (nome, email))
                                         # Executa o comando INSERT para adicionar um novo usuário.
    conexao.commit()                      # Salva (confirma) a transação no banco de dados.
    cursor.close()                        # Fecha o cursor.
    conexao.close()                       # Fecha a conexão com o banco de dados.

    def buscar_usuarios(nome):
        conexao = conectardb()  # Conecta ao banco.
        cursor = conexao.cursor()  # Cria um cursor para consultas.
        cursor.execute(f"SELECT email,nome FROM usuarios where nome= '{nome}' ")

        # Executa o comando SELECT para obter todos os usuários.

        resultado = cursor.fetchall()  # Recupera todos os resultados da consulta em uma lista.
        cursor.close()  # Fecha o cursor.
        conexao.close()  # Fecha a conexão com o banco.
        return resultado  # Retorna a lista de usuários.