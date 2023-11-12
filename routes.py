'''Contém todas as rotas da aplicação, mapeamento das URLs'''
from flask import Blueprint, request, render_template
from database import update_item, insert_item, delete_item, show_list
from flask import jsonify

# To avoid curcular imports, Flask recommends the use of Blueprints
main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def root():
    return "Hello World1!"
    # return show_list()

@main.route('/lista', methods=['GET'])
def show_list():
    return "Olá Mundo!"

@main.route('/additem', methods=['GET, POST'])
def add_item():
    if request.method == 'POST':
        item = request.form['item']
        quantity = request.form['quantity']
        market = request.form['market']
        insert_item(item, quantity, market)
        return 'Item adicionado!'
    if request.method == 'GET':
        render_template('additem.html')
