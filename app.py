from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return jsonify({"message": "Hello from GitHub Actions CI!"})


@app.route('/sum/<int:a>/<int:b>')
def add_numbers(a, b):
    return jsonify({"sum": a + b})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
