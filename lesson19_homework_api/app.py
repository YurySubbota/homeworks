from flask import Flask, request, jsonify
from database import add_product, delete_product, get_product

app = Flask(__name__)


@app.route('/products', methods=['GET', 'POST'])
def products():
    if request.method == 'GET':
        name = request.args.get('name')
        if name:
            product = get_product(name)
            if product:
                return jsonify(product), 200
            else:
                return jsonify({'message': 'Product not found'}), 404
        else:
            return jsonify({'message': 'Name parameter is required'}), 400
    elif request.method == 'POST':
        data = request.get_json()
        if data and 'name' in data:
            product = get_product(data['name'])
            if product:
                return jsonify({'message': 'Product already exists'}), 409
            else:
                add_product(data)
                return jsonify({'message': 'Product added successfully'}), 201
        else:
            return jsonify({'message': 'Invalid data'}), 400


@app.route('/products/<name>', methods=['DELETE'])
def delete(name):
    product = get_product(name)
    if product:
        delete_product(name)
        return jsonify({'message': 'Product deleted successfully'}), 200
    else:
        return jsonify({'message': 'Product not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
