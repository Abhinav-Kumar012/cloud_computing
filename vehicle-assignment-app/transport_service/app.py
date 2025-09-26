from flask import Flask, request, jsonify

app = Flask(__name__)
vehicles = {
    "V1": {"type": "Truck", "available": True},
    "V2": {"type": "Van", "available": True}
}
assignments = {}

@app.route('/assign', methods=['POST'])
def assign_vehicle():
    data = request.json
    customer_id = data['customer_id']
    for vid, vinfo in vehicles.items():
        if vinfo['available']:
            vinfo['available'] = False
            assignments[customer_id] = vid
            return jsonify({'vehicle_id': vid}), 200
    return jsonify({'error': 'No vehicles available'}), 503

@app.route('/release', methods=['POST'])
def release_vehicle():
    data = request.json
    customer_id = data['customer_id']
    vid = assignments.pop(customer_id, None)
    if vid:
        vehicles[vid]['available'] = True
        return jsonify({'message': f'Vehicle {vid} released'}), 200
    return jsonify({'error': 'No vehicle assigned'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)