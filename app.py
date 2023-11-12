'''Este é o ficheiro considerado como ponto de entrada da aplicação. Contem configurações básicas e a criação do objeto da aplicação'''

from flask import Flask, jsonify
from database import update_item, insert_item, delete_item, show_list
from routes import main

app = Flask(__name__)
app.register_blueprint(main)
app.config.from_object('config')