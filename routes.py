'''Contém todas as rotas da aplicação, mapeamento das URLs'''
from flask import Blueprint, request, render_template, flash, redirect, url_for, session, abort
from database import insert_item, delete_item, show_list
from autheticaton import register, login, login_required

# To avoid curcular imports, Flask recommends the use of Blueprints
main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
@main.route('/login', methods=['GET', 'POST'])
def root():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if login(username, password):
            session['username'] = username
            flash(f'Successfull login. Welcome!')
            return redirect(url_for('main.add_item'))
        else:
            flash('Invalid user or password, please try again.')
            return redirect(url_for('main.root'))
    if request.method == 'GET':
        return render_template('home.html')

@main.route('/register', methods=['GET', 'POST'])
def register_new_user():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        register(username, password)
        session['username'] = username
        flash(f'\"{username.title()}\" created successfully!')
        return redirect(url_for('main.root'))
    if request.method == 'GET':
        return render_template('register.html')

@main.route('/additem', methods=['GET', 'POST'])
def add_item():
    if session.get('username'):
        if request.method == 'POST':
            if 'addingitem' in request.form:
                item = request.form['item']
                type = request.form['type']
                quantity = request.form['quantity']
                market = request.form['market']
                insert_item(item, type, quantity, market)
                flash(f'\"{item.title()}\" added successfully!')
            if 'item_id' in request.form:
                item_id = request.form['item_id']
                item_item = request.form['item_item']
                delete_item(item_id)
                flash(f'\"{item_item.title()}\" removed successfully!')
            if 'logoff' in request.form:
                session.pop('username', None)
                return redirect(url_for('main.root'))
            return redirect(url_for('main.add_item'))
        if request.method == 'GET':
            items = show_list()
            types = ['Carne \ Peixe', 'Legumes \ Fruta', 'Bebidas', 'Frescos', 'Sobremesas', 'Embalados \ Enlatados', 'Limpeza', 'Outros']
            markets = ['Belita', 'Lidl', 'Eleclerc', 'Pingo Doce', 'Jumbo', 'Continente']
            return render_template('additem.html', items_formated=items, markets=markets, types=types)
    else:
        flash(f'Acess denied. Please log in.')
        return redirect(url_for('main.root'))
   
@main.route('/logoff', methods=['POST'])
def logoff():
    session.pop('username', None)
    return redirect(url_for('main.root')) 