from flask import Flask, request, jsonify

app = Flask(__name__)
customers = {}

@app.route('/customers', methods=['POST'])
def add_customer():
    data = request.json
    customer_id = data['id']
    customers[customer_id] = data
    return jsonify({'message': 'Customer added'}), 201

@app.route('/customers/<customer_id>', methods=['GET'])
def get_customer(customer_id):
    customer = customers.get(customer_id)
    if customer:
        return jsonify(customer)
    return jsonify({'error': 'Customer not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)