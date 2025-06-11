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
        print("Nenhum usuário encontrado com o Nome informado.")
    else:
        for row in rows:
            print(f'Id: {row[0]} | Nome: {row[1]} | Preço: {row[2]} | Faixa Etária: {row[3]} | Desenvolvedor: {row[4]} | Data de Lançamento: {row[5]} | Plataformas: {row[6]} | Gênero: {row[7]} |')


def Procurar_ID_Usuario():
    Escolha = input("Digite o ID do usuário: ")
    sql = f''' SELECT * FROM tb_user WHERE id_user = "{Escolha}" '''
    cursor_db.execute(sql)
    rows = cursor_db.fetchall()

    if len(rows) == 0:
        print("Nenhum usuário encontrado com o ID informado.")
    else:
        for row in rows:
            print(f'Id: {row[0]} | Nome: {row[1]} | Preço: {row[2]} | Faixa Etária: {row[3]} | Desenvolvedor: {row[4]} | Data de Lançamento: {row[5]} | Plataformas: {row[6]} | Gênero: {row[7]} |')


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


# --------------------------------------------CARRINHO--------------------------------------------------------

def create_tb_cart(cursor_db):
    create = '''CREATE TABLE IF NOT EXISTS tb_cart(
            id_cart INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            id_jogos INT NOT NULL,
            id_user INT NOT NULL,
            preco_uni DECIMAL(9,2),
            forma_pagamento VARCHAR(30),
            FOREIGN KEY (id_jogos) REFERENCES tb_jogos(id_jogo),
            FOREIGN KEY (id_user) REFERENCES tb_user(id_user)
            )'''
    cursor_db.execute(create)
    print("Tabela Cart criada")


def Insert_table_cart(cursor_db, conex_db):

    forma_pagamento = input("Digite a forma de pagamento: ")
    id_jogos = int(input('Digite o ID jogo que deseja adicionar ao carrinho: '))
    id_user = int(input("Digite o id do usuario: "))
    cursor_db.execute("SELECT price, name FROM tb_jogos WHERE id_jogo = %s", (id_jogos,))
    linha = cursor_db.fetchone()

    if linha:
        preco = linha

        insert_query = '''
        INSERT INTO tb_cart (id_jogos, id_user, preco_uni, forma_pagamento)
        VALUES (%s, %s, %s, %s)
        '''
        cursor_db.execute(insert_query, (id_jogos, id_user, preco, forma_pagamento))
        conex_db.commit()
        print("Jogo adicionado ao carrinho com sucesso")
    else:
        print("Não foi possivel encontrar um jogo com esse ID.")


def Procurar_Produtos():
    Escolha = input("Digite o ID do usuário: ")
    sql = f''' SELECT * FROM tb_carrinho_compras WHERE id_cart = "{Escolha}" '''
    cursor_db.execute(sql)
    rows = cursor_db.fetchall()

    if len(rows) == 0:
        print("Nenhum carrinho encontrado com o ID informado.")
    else:
        for row in rows:
            print(f'Id: {row[0]} | Nome: {row[1]} | Preço: {row[2]} | Faixa Etária: {row[3]} | Desenvolvedor: {row[4]} | Data de Lançamento: {row[5]} | Plataformas: {row[6]} | Gênero: {row[7]} |')           


def Update_tb_cart(cursor_db, conex_db):
    escolha = input("Digite o ID do carrinho que deseja atualizar: ")
    escolha_coluna = input("Digite a coluna que deseja atualizar (preco_total, forma_pagamento): ")
    novo_valor = input(f"Digite o novo valor para {escolha_coluna}: ")
    sql = f'''UPDATE tb_cart SET {escolha_coluna} = %s WHERE id_cart = %s'''
    dados = (novo_valor, escolha)
    cursor_db.execute(sql, dados)
    conex_db.commit()
    print(f'Dados do carrinho com ID {escolha} atualizados')


def delete_tb_cart(cursor_db, conex_db):
    escolha = input("Digite o ID do jogo que deseja deletar: ")
    sql = f'''DELETE FROM tb_cart WHERE id_cart = "{escolha}" '''
    cursor_db.execute(sql)
    conex_db.commit()
    print(f'Dados do carrinho com ID {escolha} deletados')


def preco_total():
    id_user = int(input("Digite o ID do usuário: "))

    sql = '''SELECT SUM(preco_uni) AS total
        FROM tb_cart
        WHERE id_user = %s
        '''
    cursor_db.execute(sql, (id_user,))
    resultado = cursor_db.fetchone()

    if resultado[0] is not None:
        print(f"Total do usuário {id_user}: R$ {resultado[0]}")
    else:
        print(f"Usuário {id_user} não encontrado ou carrinho vazio.")
    

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
[3] - Carrinho

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

    # Criando as tabelas (Ricardo)
    #create_db()
    #create_tb_jogos(cursor_db)
    #create_tb_user(cursor_db)
    #create_tb_cart(cursor_db)

    # Insertando dados nas tabelas (Rafael)
    #Insert_table_jogos(cursor_db, conex_db)
    #Insert_table_user(cursor_db, conex_db)
    #Insert_table_cart(cursor_db, conex_db)

    # Atualizando os dados nas tabelas (Rafael)
    #Update_tb_jogos(cursor_db, conex_db)
    #Update_tb_user(cursor_db, conex_db)
    #Update_tb_cart(cursor_db, conex_db)

    # Removendo os dados das tabelas (Rafael)
    #delete_tb_jogos(cursor_db, conex_db)
    #delete_tb_cart(cursor_db, conex_db)
    #delete_tb_user(cursor_db, conex_db)

    # Procurando por informações nos jogos (Mateus)
    #Procurar_ID_Jogo()
    #Procurar_Nome_Jogo()
    #Procurar_Preco()
    #Procurar_Idade()
    #Procurar_developer()
    #Procurar_data_lanc()
    #Procurar_plataformas()
    #Procurar_Genero()

    # Procurar informações dos usuários (Mateus)
    #Procurar_ID_Usuario()
    #Procurar_Nome()

    # Procurar informações no carrinho (Mateus)
    #Procurar_Produtos()
    
    #Retorna o valor total dos jogos no carrinho (Ricardo)
    #preco_total()

    # Ver tudo (Mateus)
    #Ver_tudo()

    # Instruções para trouxas (Rafael)

    # Para criar o banco de dados no seu pc, baixe o mysql-connector-python e o mysql-server NA MESMA VERSÂO DO SEU PYTHON
    # Instale o mysql-connector-python com o comando: pip install mysql-connector-python
    # Instale o mysql-server com o comando: sudo apt install mysql-server
    # Para coferir a versao use o comando: get-command python
    # Então crie uma database no mysql com o nome db_Wixus (ou oq achar melhor) e a senha q tu quiser mas caso as mesmas sejam diferentes, mude no código

    # A primeira vez que você for rodar o código, descomente as linhas de create e COMENTE a database no início do código
    # Depois disso comente os create e descomente a database no início do código
    # A inserção da data de lançamento está no formato YYYY-MM-DD, year, month e day
    # Deixei todas as funções prontas para serem usadas entao caso queira testar alguma coisa, basta comente as paradas que tu não vai usar
    # O update das tabelas foi feito com escolhas de colunas, se isso dificultar no tkinter, tu q se lasque (me fala q eu faço o de cada um)
    # Todos os comandos funcionais entam após o main então tudo que quiser usar vai estar lá, se nn tiver, é pq eu não tem

    # Ja avisando que se tiver faltando algum select ou table é td culpa do Ricardo (do Mateus tbm mas isso é de menos), que não fez as paradas direito
    # Se tiver faltando algum insert, update ou delete é culpa do Rafael que tambem não faz as paradas direito