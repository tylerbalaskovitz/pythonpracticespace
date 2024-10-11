from flask import Flask, jsonify

app = Flask(__name__)

# Sample data (could be replaced with a database or other source)
data = {
    'message': 'Hello, World!',
    'status': 'success'
}

# Define a GET endpoint
@app.route('/api/message', methods=['GET'])
def get_message():
    return jsonify(data)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
