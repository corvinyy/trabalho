import mysql.connector

def create_db ():
    cursor_db.execute('''CREATE DATABASE IF NOT EXISTS db_Wixus''')
    print("Data base criada")

def conection_db ():
    conection = mysql.connector.connect(
                    user = 'root',
                    host = 'localhost',
                    database = 'db_Wixus',
                    password = '123456'
                    )
    
    print("Conexão concluida")
    print("Conexão", conection)
    return conection

def create_tb_jogos():
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

def create_tb_user():
    #depois eu faço, relaxa
    pass

def create_tb_cart():
    #depois eu faço, relaxa
    pass

def create_tb_developer():
    #depois eu faço, relaxa
    pass


if __name__ == '__main__':
    conex_db = conection_db()
    cursor_db = conex_db.cursor()
    create_db()
    create_tb_jogos()
