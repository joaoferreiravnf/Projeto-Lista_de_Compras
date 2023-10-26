from backend import update_item, insert_item, delete_item, show_list
from flask import jsonify

@app.route('/', methods=['GET'])
def root():
    return show_list()