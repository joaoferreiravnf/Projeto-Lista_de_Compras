# python -m flask run

from flask import Flask, jsonify
from backend import update_item, insert_item, delete_item, show_list
from routes import routes

app = Flask(__name__)
app.config.from_object('config')