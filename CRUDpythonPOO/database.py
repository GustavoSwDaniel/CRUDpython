import sqlite3

def criar():
    conn = sqlite3.connect('banco_de_dados.db')

    c = conn.cursor()

    #Create table
    c.execute('''CREATE TABLE stocks
                 (nome, cpf, data_nacimento, endereco) ''')

criar()