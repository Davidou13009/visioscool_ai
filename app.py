
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Base de données temporaire (JSON)
questions = [
    {
        "question": "Quelle est la dérivée de x^2 ?",
        "options": ["2x", "x^2", "x", "2"],
        "answer": "2x"
    },
    {
        "question": "Quel est le résultat de 3 + 5 ?",
        "options": ["5", "7", "8", "9"],
        "answer": "8"
    },
    {
        "question": "Combien y a-t-il de côtés dans un triangle ?",
        "options": ["3", "4", "5", "6"],
        "answer": "3"
    }
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/quiz', methods=['GET'])
def quiz():
    return jsonify(questions)

if __name__ == '__main__':
    app.run(debug=True)
