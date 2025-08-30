import mysql.connector, prettytable
from mysql.connector import Error
from prettytable import PrettyTable

try:
    # Tenta estabelecer uma conexão com o banco de dados MySQL
    connection = mysql.connector.connect(
        host='localhost',  # Nome do host (localhost = máquina local)
        database='projeto',  # Nome do banco de dados
        user='root',  # Usuário do banco de dados
        password=''  # Senha (em branco nesse caso)
    )


    def insert():
        nome = input("Insira o nome do local acessível: ")
        endereco = input("Insira o endereço do local acessível: ")
        tipo = input("Insira o tipo do local acessível: ")

        mySql_insert_query = f"""
            INSERT INTO locais (nome, endereco, tipo)
            VALUES ('{nome}','{endereco}','{tipo}')
        """
        cursor = connection.cursor()
        cursor.execute(mySql_insert_query)  # Executa o comando SQL
        connection.commit()  # Confirma as mudanças no banco de dados

        # Mostra o número de registros inseridos
        print(cursor.rowcount, "Inserido com sucesso")
        cursor.close()  # Fecha o cursor


    def selectall():
        mySql_select_query = """
            SELECT * FROM locais
        """
        cursor = connection.cursor()
        cursor.execute(mySql_select_query)  # Confirma as mudanças no banco de dados

        records = cursor.fetchall()
        print("Total de registros: ", cursor.rowcount)
        grid = PrettyTable(['ID', 'Nome', 'Endereço', 'Tipo de acessibilidade'])
        for row in records:
            grid.add_row([row[0], row[1], row[2], row[3]])
        print(grid)


    def selectbytipo():
        tipo = input("insira o tipo do local que deseja buscar: ")
        mySql_select_query = f"""
            SELECT * FROM locais WHERE tipo= '{tipo}'
        """
        cursor = connection.cursor()
        cursor.execute(mySql_select_query)  # Executa o comando SQL
        records = cursor.fetchall()
        print("Total de registros: ", cursor.rowcount)
        grid = PrettyTable(['ID', 'Nome', 'Endereço', 'Tipo de acessibilidade'])
        for row in records:
            grid.add_row([row[0], row[1], row[2], row[3]])
        print(grid)
        # Mostra o número de registros inseridos
        print(cursor.rowcount, "Selecionado(s) com sucesso")
        cursor.close()  # Fecha o cursor


    def opcao(opc):
        if opc == 1:
            insert()
        elif opc == 2:
            selectall()
        elif opc == 3:
            selectbytipo()
        elif opc == 4:
            return False
        else:
            print('Opção inválida!')
        return True

    print ('Administração de Locais Acessíveis')
    x = input('''Deseja iniciar o programa e visualizar suas opções?
    Digite 1 para SIM ou qualquer tecla para sair: ''')
    print ('-'*35)
    if x == '1':
        selectall()
        while True:
            opc = int(input("""Ecolha uma opção: 
            1 - Cadastrar novo local
            2 - Listar locais
            3 - Buscar por tipo de acessibilidade
            4 - Sair
            
            Digite aqui a opção: """))
            if (opcao(opc) == False):
                break
    else:
        print('O usuário não quis executar o programa')


except Error as e:
    # Caso ocorra um erro na conexão ou execução do SQL
    print("Erro no MySQL", e)
finally:
    # Garante que a conexão será encerrada corretamente
    if connection.is_connected():
        connection.close()
        print("MySQL conexão fechada")
