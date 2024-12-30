from flask import Flask, render_template, request, jsonify
import os
import json

app = Flask(__name__)

# Charger les quiz dynamiquement depuis les fichiers JSON
def load_quiz(level, theme):
    try:
        filepath = os.path.join(app.root_path, 'quiz_structure', level.replace(" ", "_"), f"{theme.replace(' ', '_')}.json")
        with open(filepath, 'r') as file:
            questions = json.load(file)
        return questions
    except FileNotFoundError:
        return []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/quiz', methods=['POST'])
def quiz():
    data = request.json
    level = data.get('level')
    theme = data.get('theme')
    questions = load_quiz(level, theme)
    return jsonify(questions)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
