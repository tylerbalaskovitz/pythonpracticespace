from flask import Flask, jsonify

app = Flask(__name__)

# Sample data (could be replaced with a database or other source)
data = {
    'message': 'Hello, Evelyn!',
    'status': 'success'
}

# Define a GET endpoint
@app.route('/api/message', methods=['GET'])
def get_message():
    return jsonify(data)

@app.route('/')
def home():
    return "Hello, Evelyn I'm writing this in Python!"

@app.route('/secret')
def secret():
    return "I like to play RuneScape "

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
