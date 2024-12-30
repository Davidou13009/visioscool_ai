import os
import json

# Définir la structure des niveaux et thèmes
levels = {
    "Seconde": ["Analyse", "Calcul littéral", "Probabilités", "Statistiques", "Géométrie"],
    "Première_Spé_Maths": ["Analyse", "Calcul littéral", "Probabilités", "Statistiques", "Géométrie"],
    "Terminale_Spé_Maths": ["Analyse", "Calcul littéral", "Probabilités", "Statistiques", "Géométrie"]
}

# Définir les nouvelles questions pour chaque thème
questions = {
    "Analyse": [
        {"question": "Calculez 2 + 3.", "options": ["4", "5", "6", "7"], "answer": "5"},
        {"question": "Résolvez : 4x = 8.", "options": ["1", "2", "3", "4"], "answer": "2"},
        {"question": "Calculez 3².", "options": ["6", "9", "12", "15"], "answer": "9"}
    ],
    "Calcul littéral": [
        {"question": "Simplifiez : (x + 1)(x - 1).", "options": ["x² - 1", "x² + 1", "x² - 2", "x² + 2"], "answer": "x² - 1"},
        {"question": "Développez : (2x + 3)(x - 1).", "options": ["2x² - 2x + 3", "2x² + x - 3", "2x² - x - 3", "2x² + 3x - 3"], "answer": "2x² + x - 3"},
        {"question": "Factorisez : x² - 4.", "options": ["(x - 2)(x + 2)", "(x - 4)(x + 1)", "(x - 2)(x - 2)", "(x + 4)(x - 1)"], "answer": "(x - 2)(x + 2)"}
    ],
    "Probabilités": [
        {"question": "Quelle est la probabilité d’obtenir un 6 en lançant un dé ?", "options": ["1/6", "1/2", "1/3", "1/4"], "answer": "1/6"},
        {"question": "Combien de résultats possibles dans un lancer de pièce ?", "options": ["1", "2", "3", "4"], "answer": "2"},
        {"question": "Quelle est la probabilité d’obtenir un nombre pair en lançant un dé ?", "options": ["1/2", "1/3", "2/3", "1/6"], "answer": "1/2"}
    ]
}

# Chemin des fichiers JSON
quiz_path = "quiz_structure"

# Ajouter les questions dans les fichiers JSON
for level, themes in levels.items():
    level_path = os.path.join(quiz_path, level.replace(" ", "_"))
    os.makedirs(level_path, exist_ok=True)  # Crée le dossier s'il n'existe pas

    for theme in themes:
        theme_file = os.path.join(level_path, f"{theme.replace(' ', '_')}.json")
        
        # Charger les questions existantes
        if os.path.exists(theme_file):
            with open(theme_file, 'r') as file:
                existing_questions = json.load(file)
        else:
            existing_questions = []

        # Ajouter les nouvelles questions
        updated_questions = existing_questions + questions.get(theme, [])

        # Sauvegarder les mises à jour
        with open(theme_file, 'w') as file:
            json.dump(updated_questions, file, indent=4)

print("Les fichiers JSON ont été mis à jour avec des questions pour chaque niveau et thème.")