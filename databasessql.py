from config import db_portatil, db_fixo
import sqlite3

conn = sqlite3.connect(db_portatil, timeout=5)
# Cria uma tabela se esta ainda não existir
conn.execute('''CREATE TABLE IF NOT EXISTS Users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL UNIQUE,
                        password_hash TEXT NOT NULL)''')

conn = sqlite3.connect(db_portatil, timeout=5)
# Cria uma tabela se esta ainda não existir
conn.execute('''CREATE TABLE IF NOT EXISTS ListaDeCompras (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    item VARCHAR(64) NOT NULL UNIQUE,
                                    type VARCHAR(64) NOT NULL,
                                    date DATE NOT NULL,
                                    qty TINYINT NOT NULL DEFAULT 1,
                                    market VARCHAR(64),
                                    buyed BOOLEAN DEFAULT FALSE)''')