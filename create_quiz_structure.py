import os
import json
import zipfile

# Définir la structure de répertoires et les questions
quiz_path = 'quiz_structure'
os.makedirs(quiz_path, exist_ok=True)

levels = {
    "Seconde": ["Analyse", "Calcul littéral", "Probabilités", "Statistiques", "Géométrie"],
    "Première Spé Maths": ["Analyse", "Calcul littéral", "Probabilités", "Statistiques", "Géométrie"],
    "Terminale Spé Maths": ["Analyse", "Calcul littéral", "Probabilités", "Statistiques", "Géométrie"]
}

questions = {
    "Seconde": {
        "Analyse": [
            {"question": "Déterminez l'image de 2 par la fonction f(x) = x².", "options": ["2", "4", "6", "8"], "answer": "4"},
            {"question": "Quelle est la valeur de f(3) pour f(x) = 2x + 1 ?", "options": ["5", "6", "7", "8"], "answer": "7"}
        ]
    },
    "Première Spé Maths": {
        "Analyse": [
            {"question": "Calculez la dérivée de f(x) = x² + 3x.", "options": ["2x + 3", "x + 3", "2x", "3x"], "answer": "2x + 3"}
        ]
    },
    "Terminale Spé Maths": {
        "Probabilités": [
            {"question": "Quelle est l’espérance de X si X suit une loi uniforme sur {1, 2, 3, 4, 5} ?", "options": ["3", "3.5", "4", "2.5"], "answer": "3"}
        ]
    }
}

# Enregistrer les questions par niveau et thème
for level, themes in levels.items():
    level_path = os.path.join(quiz_path, level.replace(" ", "_"))
    os.makedirs(level_path, exist_ok=True)
    for theme in themes:
        theme_file = os.path.join(level_path, f"{theme.replace(' ', '_')}.json")
        theme_questions = questions.get(level, {}).get(theme, [])
        with open(theme_file, 'w') as file:
            json.dump(theme_questions, file, indent=4)

# Créer le fichier ZIP
zip_path = 'quiz_structure.zip'
with zipfile.ZipFile(zip_path, 'w') as zipf:
    for root, dirs, files in os.walk(quiz_path):
        for file in files:
            zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), quiz_path))

print(f"Structure créée et compressée dans {zip_path}")