# wsgi.py
# pylint: disable=missing-docstring

from flask import Flask
from flask import jsonify
from flask import request
app = Flask(__name__)

PRODUCTS = {
    1: { 'id': 1, 'name': 'Skello' },
    2: { 'id': 2, 'name': 'Socialive.tv' },
    3: { 'id': 3, 'name': 'Le Wagon'}
    }

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/api/v1/products')
def products():
    PRODUCTS1 = {
        1: { 'id': 1, 'name': 'Skello' },
        2: { 'id': 2, 'name': 'Socialive.tv' },
        3: { 'id': 3, 'name': 'Le Wagon'},
    }
    return jsonify(PRODUCTS1)

@app.route('/api/v1/products/<int:product_id>', methods=['GET'])
def get_one_product(product_id):
    if request.method == 'GET':
        # PRODUCTS2 = {
        #     1: { 'id': 1, 'name': 'Skello' },
        #     2: { 'id': 2, 'name': 'Socialive.tv' },
        #     3: { 'id': 3, 'name': 'Le Wagon'}
        #     }
        if product_id < len(PRODUCTS2):
            return jsonify(PRODUCTS2[product_id])
        else:
            return jsonify({'ERROR': 'product not found , try again'})
    else:
        abort(404)

@app.route('/api/v1/products/<int:product_id>', methods=['DELETE'])
def del_one_product(product_id):
    if request.method == 'DELETE':
        PRODUCTS1 = {
            1: { 'id': 1, 'name': 'Skello' },
            2: { 'id': 2, 'name': 'Socialive.tv' },
            3: { 'id': 3, 'name': 'Le Wagon'}
            }
        if product_id > len(PRODUCTS1):
            return jsonify({'ERROR': 'product not found , try again'})
        else:
            PRODUCTS1.pop(product_id)
#            PRODUCTS.remove(product_id)
#            PRODUCTS[product_id].del
#            del PRODUCTS(produc_id)
            return jsonify(PRODUCTS1)
    else:
        abort(405)

# http://localhost:5000/api/v1/products/add/?id=6&name='waouh'
@app.route('/api/v1/products/add/', methods=['POST'])
def create_one_product():
    if request.method == 'POST':
        product_id=int(request.args.get('id'))
        product_name=request.args.get('name')
        new_product={ 4 :{'id' : product_id, 'name': product_name }}
        PRODUCTS.update(new_product)
        return jsonify(PRODUCTS)
    else:
        abort(405)
