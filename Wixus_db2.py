import mysql.connector
    
def create_db():
    create = '''CREATE DATABASE IF NOT EXISTS db_Wixus'''
    cursor_db.execute(create)
    use = '''USE db_Wixus'''
    cursor_db.execute(use)
    print("Data base criada")

class Conexão:
    def __init__(self, host='localhost', user='root',password='123456', database='db_Wixus'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

def conection_db():
    conection = mysql.connector.connect(
        user='root',
        host='localhost',
        database='db_Wixus',
        password='123456'
    )

    print("Conexão concluida")
    print("Conexão", conection)
    return conection


# -------------------------------------------JOGOS--------------------------------------------------------

def create_tb_jogos(cursor_db):
    create = '''CREATE TABLE IF NOT EXISTS tb_jogos(
            id_jogo INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            price DECIMAL(9,2),
            faixa_etaria INT,
            developer VARCHAR(30) NOT NULL,
            data_lanc DATE,
            plataformas VARCHAR(30),
            genre VARCHAR(50)
            )'''
    cursor_db.execute(create)
    print("Tabela Jogos criada")


def Insert_table_jogos(cursor_db, conex_db):
    sql = '''
    INSERT INTO tb_jogos (name, price, data_lanc, faixa_etaria, developer, plataformas, genre)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    '''
    dados_geral = input('Digite o nome do jogo: '), \
        float(input('Digite o preço do jogo: ')), \
        input('Digite a data de lançamento (YYYY-MM-DD): '), \
        int(input('Digite a faixa etária do jogo: ')), \
        input('Digite o nome do desenvolvedor: '), \
        input('Digite as plataformas do jogo: '), \
        input('Digite o gênero do jogo: ')
    dados_geral = tuple(dados_geral)
    cursor_db.execute(sql, dados_geral)
    conex_db.commit()
    print('Dados do jogo inseridos')


def Procurar_ID_Jogo():
    Escolha = input("Digite o ID do jogo: ")
    sql = f''' SELECT * FROM tb_jogos WHERE id_jogo = "{Escolha}" '''
    cursor_db.execute(sql)
    rows = cursor_db.fetchall()

    if len(rows) == 0:
        print("Nenhum jogo encontrado com o ID informado.")
    else:
        for row in rows:
            print(f'Id: {row[0]} | Nome: {row[1]} | Preço: {row[2]} | Faixa Etária: {row[3]} | Desenvolvedor: {row[4]} | Data de Lançamento: {row[5]} | Plataformas: {row[6]} | Gênero: {row[7]} |')


def Procurar_Nome_Jogo():
    Escolha = input("Digite o Nome do jogo: ")
    sql = f''' SELECT * FROM tb_jogos WHERE name = "{Escolha}" '''
    cursor_db.execute(sql)
    rows = cursor_db.fetchall()

    if len(rows) == 0:
        print("Nenhum jogo encontrado com o Nome informado.")
    else:
        for row in rows:
            print(f'Id: {row[0]} | Nome: {row[1]} | Preço: {row[2]} | Faixa Etária: {row[3]} | Desenvolvedor: {row[4]} | Data de Lançamento: {row[5]} | Plataformas: {row[6]} | Gênero: {row[7]} |')
            

def Procurar_Preco():
    Escolha = input("Digite o preço máximo do jogo: ")
    sql = f''' SELECT * FROM tb_jogos WHERE price <= "{Escolha}" '''
    cursor_db.execute(sql)
    rows = cursor_db.fetchall()

    if len(rows) == 0:
        print("Nenhum jogo encontrado com valor menor.")
    else:
        for row in rows:
            print(f'Id: {row[0]} | Nome: {row[1]} | Preço: {row[2]} | Faixa Etária: {row[3]} | Desenvolvedor: {row[4]} | Data de Lançamento: {row[5]} | Plataformas: {row[6]} | Gênero: {row[7]} |')
            

def Procurar_Idade():
    Escolha = input("Digite a faixa etária do jogo: ")
    sql = f''' SELECT * FROM tb_jogos WHERE faixa_etaria <= "{Escolha}" '''
    cursor_db.execute(sql)
    rows = cursor_db.fetchall()

    if len(rows) == 0:
        print("Nenhum jogo encontrado com a faixa etária informado.")
    else:
        for row in rows:
            print(f'Id: {row[0]} | Nome: {row[1]} | Preço: {row[2]} | Faixa Etária: {row[3]} | Desenvolvedor: {row[4]} | Data de Lançamento: {row[5]} | Plataformas: {row[6]} | Gênero: {row[7]} |')
            

def Procurar_developer():
    Escolha = input("Digite o produtor(a) do jogo: ")
    sql = f''' SELECT * FROM tb_jogos WHERE developer = "{Escolha}" '''
    cursor_db.execute(sql)
    rows = cursor_db.fetchall()

    if len(rows) == 0:
        print("Nenhum jogo encontrado com o Desenvolvedor informado.")
    else:
        for row in rows:
            print(f'Id: {row[0]} | Nome: {row[1]} | Preço: {row[2]} | Faixa Etária: {row[3]} | Desenvolvedor: {row[4]} | Data de Lançamento: {row[5]} | Plataformas: {row[6]} | Gênero: {row[7]} |')           


def Procurar_data_lanc():
    Escolha = input("Digite a data de lançamento do jogo: ")
    sql = f''' SELECT * FROM tb_jogos WHERE data_lanc  = "{Escolha}" '''
    cursor_db.execute(sql)
    rows = cursor_db.fetchall()

    if len(rows) == 0:
        print("Nenhum jogo publicado na data informada.")
    else:
        for row in rows:
            print(f'Id: {row[0]} | Nome: {row[1]} | Preço: {row[2]} | Faixa Etária: {row[3]} | Desenvolvedor: {row[4]} | Data de Lançamento: {row[5]} | Plataformas: {row[6]} | Gênero: {row[7]} |')
            

def Procurar_plataformas():
    Escolha = input("Digite o gênero do jogo: ")
    sql = f''' SELECT * FROM tb_jogos WHERE plataformas  = "{Escolha}" '''
    cursor_db.execute(sql)
    rows = cursor_db.fetchall()

    if len(rows) == 0:
        print("Nenhum jogo lançado na plataforma informada.")
    else:
        for row in rows:
            print(f'Id: {row[0]} | Nome: {row[1]} | Preço: {row[2]} | Faixa Etária: {row[3]} | Desenvolvedor: {row[4]} | Data de Lançamento: {row[5]} | Plataformas: {row[6]} | Gênero: {row[7]} |')
            

def Procurar_Genero():
    Escolha = input("Digite o gênero do jogo: ")
    sql = f''' SELECT * FROM tb_jogos WHERE genre  = "{Escolha}" '''
    cursor_db.execute(sql)
    rows = cursor_db.fetchall()

    if len(rows) == 0:
        print("Nenhum jogo encontrado com o Genero informado.")
    else:
        for row in rows:
            print(f'Id: {row[0]} | Nome: {row[1]} | Preço: {row[2]} | Faixa Etária: {row[3]} | Desenvolvedor: {row[4]} | Data de Lançamento: {row[5]} | Plataformas: {row[6]} | Gênero: {row[7]} |')
            

def Update_tb_jogos(cursor_db, conex_db):
    escolha = input("Digite o ID do jogo que deseja atualizar: ")
    escolha_coluna = input(
        "Digite a coluna que deseja atualizar (name, price, faixa_etaria, developer, data_lanc, plataformas, genre): ")
    novo_valor = input(f"Digite o novo valor para {escolha_coluna}: ")
    sql = f'''UPDATE tb_jogos SET {escolha_coluna} = %s WHERE id_jogo = %s'''
    dados = (novo_valor, escolha)
    cursor_db.execute(sql, dados)
    conex_db.commit()
    print(f'Dados do jogo com ID {escolha} atualizados')


def delete_tb_jogos(cursor_db, conex_db):
    escolha = input("Digite o ID do jogo que deseja deletar: ")
    sql = f'''DELETE FROM tb_jogos WHERE id_jogo = "{escolha}" '''
    cursor_db.execute(sql)
    conex_db.commit()
    print(f'Dados do jogo com ID {escolha} deletados')


# ---------------------------------------------USUARIO--------------------------------------------------------

def create_tb_user(cursor_db):
    # não coloquei a parametro 'jogos_criados' deve ser colocado na tabela tb_devs (Ricardo)
    create = '''CREATE TABLE IF NOT EXISTS tb_user(
            id_user INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(50) NOT NULL,
            idade INT NOT NULL,
            pais VARCHAR(50),
            status VARCHAR(50),
            developer bool DEFAULT FALSE
            )'''
    cursor_db.execute(create)
    print("Tabela User criada")


def Insert_table_user(cursor_db, conex_db):
    sql = '''
    INSERT INTO tb_user (nome, idade, pais, status, developer)
    VALUES (%s, %s, %s, %s, %s)
    '''
    dados = input('Digite o nome do usuário: '), \
        int(input('Digite a idade do usuário: ')), \
        input('Digite o país do usuário: '), \
        input('Digite o status do usuário: '), \
        int(input('O usuário é um desenvolvedor? (1/0): '))

    dados = tuple(dados)
    cursor_db.execute(sql, dados)
    conex_db.commit()
    print('Dados do usuario inseridos')


def Procurar_Nome_Usuario():
    Escolha = input("Digite o nome do usuário: ")
    sql = f''' SELECT * FROM tb_user WHERE nome = "{Escolha}" '''
    cursor_db.execute(sql)
    rows = cursor_db.fetchall()

    if len(rows) == 0:
        print("Nenhum usuário encontrado com o ID informado.")
    else:
        for row in rows:
            print(f'ID: {row[0]} | Nome: {row[1]} | Idade: {row[2]} | País: {row[3]} | Status: {row[4]} | Developer {row[5]} ')


def Procurar_ID_Usuario():
    Escolha = input("Digite o ID do usuário: ")
    sql = f''' SELECT * FROM tb_user WHERE id_user = "{Escolha}" '''
    cursor_db.execute(sql)
    rows = cursor_db.fetchall()

    if len(rows) == 0:
        print("Nenhum usuário encontrado com o ID informado.")
    else:
        for row in rows:
            print(f'ID: {row[0]} | Nome: {row[1]} | Idade: {row[2]} | País: {row[3]} | Status: {row[4]} | Developer {row[5]} ')


def Update_tb_user(cursor_db, conex_db):
    escolha = input("Digite o ID do usuario que deseja atualizar: ")
    escolha_coluna = input("Digite a coluna que deseja atualizar (nome, idade, pais, status, developer): ")
    novo_valor = input(f"Digite o novo valor para {escolha_coluna}: ")
    sql = f'''UPDATE tb_user SET {escolha_coluna} = %s WHERE id_user = %s'''
    dados = (novo_valor, escolha)
    cursor_db.execute(sql, dados)
    conex_db.commit()
    print(f'Dados do usuario com ID {escolha} atualizados')


def delete_tb_user(cursor_db, conex_db):
    escolha = input("Digite o ID do usuario que deseja deletar: ")
    sql = f'''DELETE FROM tb_user WHERE id_user = "{escolha}" '''
    cursor_db.execute(sql)
    conex_db.commit()
    print(f'Dados do usuario com ID {escolha} deletados')


# ---------------------------------------------GERAL---------------------------------------------------------

def Ver_tudo():
    print("Todas os jogos do banco de dados:")
    sql = f'''SELECT * FROM tb_jogos'''
    cursor_db.execute(sql)
    rows = cursor_db.fetchall()
    for row in rows:
        print(row)

def linha():
    print("="*90)

def Menu():
    while True:
        linha()
        try:
            escolha = int(input("""Escolha a funcionalidade desejada: 

[1] - Procure um jogo
[2] - Procure um usuário

[0] - Funcionalidades de desenvolvedor
"""))
            linha()
        except ValueError:
            print("Valor inválido")
        
        if escolha == 1:
            Info_Jogos()
            
        if escolha == 2:
            Info_Usuario()
        
        if escolha == 0:
            Funcoes_Dev()
            
def Info_Jogos():
    try:
        escolha = int(input("""Escolha uma das opções: 

[1] - ID
[2] - Nome
[3] - Preço
[4] - Faixa etária
[5] - Gênero
"""))
        
        linha()
        if escolha == 1:
            Procurar_ID_Jogo()
        elif escolha == 2:
            Procurar_Nome_Jogo()
        elif escolha == 3:
            Procurar_Preco()
        elif escolha == 4: 
            Procurar_Idade()
        elif escolha == 5:
            Procurar_Genero()
            
    except ValueError:
        print("Valor inválido")

def Info_Usuario():
    try:
        escolha = int(input("""Escolha uma das opções: 

[1] - ID
[2] - Nome         
"""))

        linha()
        if escolha == 1:
            Procurar_ID_Usuario()
        elif escolha == 2:
            Procurar_Nome_Usuario()

    except ValueError:
        print("Valor inválido")

def Funcoes_Dev():
    try:
        escolha = int(input("""Escolha uma das opções: 

[1] - Jogo
[2] - Usuário
"""))

        if escolha == 1:
            Funcoes_Jogo()
        elif escolha == 2:
            Funcoes_Usuario()
            
    except ValueError:
        print("Valor inválido")

def Funcoes_Jogo():
    try:
        escolha = int(input("""Escolha uma das opções: 

[1] - Inserir 
[2] - Remover      
[3] - Atualizar
"""))

        linha()
        if escolha == 1:
            Insert_table_jogos(cursor_db, conex_db)
        elif escolha == 2:
            delete_tb_jogos(cursor_db, conex_db)
        elif escolha == 3:
            Update_tb_jogos(cursor_db, conex_db)

    except ValueError:
        print("Valor inválido")
    
def Funcoes_Usuario():
    try:
        escolha = int(input("""Escolha uma das opções: 

[1] - Inserir 
[2] - Remover      
[3] - Atualizar
"""))

        linha()
        if escolha == 1:
            Insert_table_user(cursor_db, conex_db)
        elif escolha == 2:
            delete_tb_user(cursor_db, conex_db)
        elif escolha == 3:
            Update_tb_user(cursor_db, conex_db)

    except ValueError:
        print("Valor inválido")

# -----------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    conex_db = conection_db()
    cursor_db = conex_db.cursor()
    Menu()
