from flask import Flask, jsonify, request
import os

app = Flask(__name__)

def create_frequency_table(input_list):
    frequency_table = {}
    for item in input_list:
        if item in frequency_table:
            frequency_table[item] += 1
        else:
            frequency_table[item] = 1
    return frequency_table

@app.route('/frequency', methods=['POST'])
def get_frequency():
    data = request.json
    if not data or 'list' not in data:
        return jsonify({'error': 'Invalid input. Please provide a list.'}), 400
    
    input_list = data['list']
    result = create_frequency_table(input_list)
    return jsonify(result)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)