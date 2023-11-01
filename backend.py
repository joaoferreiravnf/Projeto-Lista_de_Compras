from flask import Flask
import sqlite3
from datetime import date

# Classe para criação\abertura de ligação à BD
class Database:
    # Inicialização da classe
    def __init__(self):
        try:
            # Conexão à BD
            self.conn = sqlite3.connect(r"C:\Users\João Ferreira\OneDrive\Documents\Formação\Github Repositorio\Projeto Lista_de_Compras\Lista de Compras.db")
            # Cria uma tabela se esta ainda não existir
            self.conn.execute('''CREATE TABLE IF NOT EXISTS ListaDeCompras,
                            id INT PRIMARY KEY AUTOINCREMENT,
                            item VARCHAR(64) NOT NULL UNIQUE,
                            date DATE NOT NULL,
                            qty TINYINT NOT NULL DEFAULT 1,
                            market VARCHAR(64),
                            buyed BOOLEAN DEFAULT FALSE''')
        except sqlite3.Error as error:
            return f"Não foi possível aceder à BD devido a: {error}"
    # Criação do apontador
    def cursor(self):
        return self.conn.cursor()
    # Commit da alteração feita
    def commit(self):
        return self.conn.commit()
    # Fecho da ligação à DB
    def close(self):
        return self.conn.close

# Lógica para adicionar um item à lista
def insert_item(item : str, qty : int, market : str):
    try:
        # Cração da instância de ligação à DB
        db = Database()
        # Criação de apontador
        c = db.cursor()
        # Execução da inserção pretendida
        c.execute('''INSERT INTO ListaDeCompras (item, date, qty, market) VALUES (?, ?, ?, ?)''', (item, date.today(), qty, market))
        db.commit()
        return f"O item {item} foi inserido com sucesso!"
    # Exposição de eventuais erros
    except sqlite3.Error as error:
        return f"Não foi possível adicionar o item {item} à lista devido a: {error}"
    # Fecho da ligação à BD
    finally:
        db.close()

# Lógica para remover um item da lista
def delete_item(item):
    try:
        # Cração da instância de ligação à DB
        db = Database()
        # Criação de apontador
        c = db.cursor()
        # Execução da remoção pretendida
        c.execute('''DELETE FROM ListaDeCompras WHERE item = ?''', (item))
        db.commit()
        return f"O item {item} foi removido com sucesso!"
    # Exposição de eventuais erros
    except sqlite3.Error as error:
        return f"Não foi possível remover o item {item} da lista devido a: {error}"
    # Fecho da ligação à BD
    finally:
        db.close()

# Lógica para alterar um item da lista
def update_item(item, item2):
    try:
        # Cração da instância de ligação à DB
        db = Database()
        # Criação de apontador
        c = db.cursor()
        # Execução da alteração pretendida
        c.execute('''UPDATE ListaDeCompras SET item = ? WHERE item = ?''', (item2, item))
        db.commit()
        return f"O item {item} foi alterado com sucesso!"
    # Exposição de eventuais erros
    except sqlite3.Error as error:
        return f"Não foi possível alterar o item {item} da lista devido a: {error}"
    # Fecho da ligação à BD
    finally:
        db.close()

# Lógica para mostrar a lista
def show_list(item, item2):
    try:
        # Cração da instância de ligação à DB
        db = Database()
        # Criação de apontador
        c = db.cursor()
        # Execução da alteração pretendida
        c.execute('''SELECT * FROM ListaDeCompras''')             
        return c.fetchall()        
    # Exposição de eventuais erros
    except sqlite3.Error as error:
        return f"Não foi possível alterar o item {item} da lista devido a: {error}"
    # Fecho da ligação à BD
    finally:
        db.close() 