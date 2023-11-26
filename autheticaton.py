from database import Database
import hashlib
import sqlite3
from flask import session

def hash_password(password : str):
    password_bytes = password.encode('utf-8')
    hash_object = hashlib.sha256(password_bytes)
    return hash_object.hexdigest()

def register(username, password):
    # Creating the hash for the password
    hash_pass = hash_password(password)
    # Cração da instância de ligação à DB
    try:
        db = Database()
        # Criação de apontador
        c = db.cursor()
        # Execução da alteração pretendida
        c.execute('''INSERT INTO Users (username, password_hash) VALUES (?, ?)''', (username, hash_pass))
        db.commit()
        return f"O user {username} foi criado com sucesso!"
    # Exposição de eventuais erros
    except sqlite3.Error as error:
        print(f"Não foi possível adicionar o user {username} à lista devido a: {error}")
        raise
    # Fecho da ligação à BD
    finally:
        db.close()

def login(username, password):
    hash_pass = hash_password(password)
    # Cração da instância de ligação à DB
    try:
        db = Database()
        # Criação de apontador
        c = db.cursor()
        # Execução da alteração pretendida
        c.execute('''SELECT password_hash FROM Users WHERE username = ?''', (username,))
        result = c.fetchone()
        if result and result[0] == hash_pass:
            return True
        else:
            return False
    # Exposição de eventuais erros
    except sqlite3.Error as error:
        print(error)
        raise
    # Fecho da ligação à BD
    finally:
        db.close()

def logoff(username, password):
    hash_pass = hash_password(password)
    # Cração da instância de ligação à DB
    try:
        db = Database()
        # Criação de apontador
        c = db.cursor()
        # Execução da alteração pretendida
        c.execute('''SELECT password_hash FROM Users WHERE username = ?''', (username,))
        result = c.fetchone()
        if result and result[0] == hash_pass:
            return True
        else:
            return False
    # Exposição de eventuais erros
    except sqlite3.Error as error:
        print(error)
        raise
    # Fecho da ligação à BD
    finally:
        db.close()

def login_required():
    if username not in session:
        return False
    else:
        return True