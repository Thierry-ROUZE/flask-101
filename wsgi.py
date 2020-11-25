# wsgi.py
# pylint: disable=missing-docstring

from flask import Flask
from flask import jsonify
from flask import request
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/api/v1/products')
def products():
    PRODUCTS = {
        1: { 'id': 1, 'name': 'Skello' },
        2: { 'id': 2, 'name': 'Socialive.tv' },
        3: { 'id': 3, 'name': 'Le Wagon'},
    }
    return jsonify(PRODUCTS)

@app.route('/api/v1/products/<int:product_id>', methods=['GET'])
def get_one_product(product_id):
    if request.method == 'GET':
        PRODUCTS = {
            1: { 'id': 1, 'name': 'Skello' },
            2: { 'id': 2, 'name': 'Socialive.tv' },
            3: { 'id': 3, 'name': 'Le Wagon'}
            }
        if product_id < len(PRODUCTS):
            return jsonify(PRODUCTS[product_id])
        else:
            return jsonify({'ERROR': 'product not found , try again'})
    else:
        abort(404)

@app.route('/api/v1/products/<int:product_id>', methods=['DELETE'])
def del_one_product(product_id):
    if request.method == 'DELETE':
        PRODUCTS = {
            1: { 'id': 1, 'name': 'Skello' },
            2: { 'id': 2, 'name': 'Socialive.tv' },
            3: { 'id': 3, 'name': 'Le Wagon'}
            }
        if product_id > len(PRODUCTS):
            return jsonify({'ERROR': 'product not found , try again'})
        else:
            PRODUCTS.pop(product_id)
#            PRODUCTS.remove(product_id)
#            PRODUCTS[product_id].del
#            del PRODUCTS(produc_id)
            return jsonify(PRODUCTS)
    else:
        abort(405)
