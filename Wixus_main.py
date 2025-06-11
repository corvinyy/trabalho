from Wixus_db2 import * 

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

if __name__ == "__main__":
    conex_db = conection_db()
    cursor_db = conex_db.cursor()
    Menu()   