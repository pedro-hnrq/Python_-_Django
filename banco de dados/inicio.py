# import pymysql.cursors



# con = pymysql.connect(
#     host="localhost",
#     user="root",
#     password="",
#     port=3306,
#     db="pythonfull",
#     charset="utf8mb4",
#     cursorclass= pymysql.cursors.DictCursor)

# def criaTabela(nomeTabela): 
      
#     try:
#         with con.cursor() as cursor:
#             cursor.execute(f"create table {nomeTabela} (nome varchar(50))")
#         print("tabela criada com sucesso")
#     except Exception as e:
#         print(f'Ocorreu um erro {e}')

# criaTabela("teste")


# nome = input('Digite seu nome ')    
# try:
#     with con.cursor() as cursor:
#         cursor.execute(f"INSERT INTO teste values ('{nome}')")
#     print("Valor inserido com sucesso")
# except Exception as e:
#     print(f'Ocorreu um erro {e}')


# def selectTabela():
#     try:
#         with con.cursor() as cursor:
#             cursor.execute("SELECT * FROM teste")
#             resultado = cursor.fetchall() #fetchall() = trás todas as linha do banco de dados e #fetchone() = trás só uma linha do banco de dados.
#             for i in resultado:
#                 print(i)
#     except Exception as e:
#         print(f'Ocorreu um erro {e}')

# def updateTabela():
#     try:
#         with con.cursor() as cursor:
#             cursor.execute("UPDATE teste SET nome = 'Pedro' WHERE nome = 'henrique'")
#         print("Atualização com sucesso")
#     except Exception as e:
#         print(f'Ocorreu um erro {e}')

# try:
#     with con.cursor() as cursor:
#         cursor.execute("DELETE FROM teste WHERE nome = 'Feitosa'")
#     print("remoção efetuada com sucesso")
# except Exception as e:
#     print(f'Ocorreu um erro {e}')



# con.close()