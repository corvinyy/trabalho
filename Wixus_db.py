import mysql.connector

def create_db ():
    create = '''CREATE DATABASE IF NOT EXISTS db_Wixus'''
    cursor_db.execute(create)
    use = '''USE db_Wixus'''
    cursor_db.execute(use)
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
    #não coloquei a parametro 'jogos_criados' deve ser colocado na tabela tb_devs
    create = '''CREATE TABLE IF NOT EXISTS tb_user(
            id_user INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(50) NOT NULL,
            idade INT NOT NULL,
            pais VARCHAR(50),
            status VARCHAR(50)
            )'''
    cursor_db.execute(create)
    print("Tabela User criada")


def create_tb_cart():
    create = '''CREATE TABLE IF NOT EXISTS tb_cart(
            id_user INT NOT NULL AUTO_INCREMENT,
            preco_total INT NOT NULL,
            forma_pagamento VARCHAR(30),
            PRIMARY KEY (id_user),
            FOREIGN KEY (id_user) REFERENCES tb_user(id_user)
            )'''
    cursor_db.execute(create)
    print("Tabela Cart criada")

def create_tb_developer():
    create = '''CREATE TABLE IF NOT EXISTS tb_developer(
            id_dev INT NOT NULL AUTO_INCREMENT,
            nome VARCHAR(45),
            idade INT NOT NULL,
            pais VARCHAR(45),
            status VARCHAR(50),
            jogos_criados VARCHAR(50),
            PRIMARY KEY (id_dev)
            )'''
    cursor_db.execute(create)
    print("Tabela Developer criada")

if __name__ == '__main__':
    conex_db = conection_db()
    cursor_db = conex_db.cursor()
    create_db()
    create_tb_jogos()
    create_tb_user()
    create_tb_cart()
    create_tb_developer()