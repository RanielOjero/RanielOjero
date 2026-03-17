from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to my Flask API!"

@app.route('/student')
def get_student():
    return jsonify({
        "name": "Raniel Guerra Ojero",
        "grade": 10,
        "section": "Zechariah"
    })

@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    return jsonify({
        "number1": a,
        "number2": b,
        "sum": a + b
    })

if __name__ == '__main__':
    app.run(debug=True)