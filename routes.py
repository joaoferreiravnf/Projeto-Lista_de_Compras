'''Contém todas as rotas da aplicação, mapeamento das URLs'''
from flask import Blueprint
from backend import update_item, insert_item, delete_item, show_list
from flask import jsonify

# Para evitar importações circulares, o Flask aconselha a utilização de Blueprints
main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def root():
    return "Hello World!"
    # return show_list()

@main.route('/lista', methods=['GET'])
def show_list():
    return "Olá Mundo!"