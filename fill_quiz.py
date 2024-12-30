import os
import json

# Définir les niveaux et thèmes
levels = {
    "Seconde": ["Analyse", "Calcul littéral", "Probabilités", "Statistiques", "Géométrie"],
    "Première Spé Maths": ["Analyse", "Calcul littéral", "Probabilités", "Statistiques", "Géométrie"],
    "Terminale Spé Maths": ["Analyse", "Calcul littéral", "Probabilités", "Statistiques", "Géométrie"]
}

# Définir les nouvelles questions pour tous les thèmes
default_questions = {
    "Analyse": [
        {"question": "Quelle est la dérivée de x² ?", "options": ["2x", "x", "x²", "2"], "answer": "2x"},
        {"question": "Calculez la limite de 1/x lorsque x tend vers 0.", "options": ["0", "+∞", "-∞", "1"], "answer": "+∞"},
        {"question": "Quelle est l'intégrale de 2x dx ?", "options": ["x²", "2x²", "x² + C", "2x + C"], "answer": "x² + C"}
    ],
    "Calcul littéral": [
        {"question": "Développez : (x + 1)(x - 1).", "options": ["x² - 1", "x² + 1", "x² - 2", "x² + 2"], "answer": "x² - 1"},
        {"question": "Factorisez : x² - 4.", "options": ["(x - 2)(x + 2)", "(x - 4)(x + 1)", "(x - 2)(x - 2)", "(x + 4)(x - 1)"], "answer": "(x - 2)(x + 2)"},
        {"question": "Simplifiez : 2x + 3x.", "options": ["2x", "3x", "5x", "6x"], "answer": "5x"}
    ],
    "Probabilités": [
        {"question": "Quelle est la probabilité d’obtenir un 6 avec un dé ?", "options": ["1/6", "1/2", "1/3", "1/4"], "answer": "1/6"},
        {"question": "Combien de résultats possibles avec une pièce ?", "options": ["1", "2", "3", "4"], "answer": "2"},
        {"question": "Quelle est la probabilité d’avoir au moins un 6 avec deux dés ?", "options": ["11/36", "1/6", "5/12", "7/36"], "answer": "11/36"}
    ],
    "Statistiques": [
        {"question": "Quelle est la moyenne de 2, 4, 6 ?", "options": ["3", "4", "5", "6"], "answer": "4"},
        {"question": "Quelle est la médiane de 3, 5, 7 ?", "options": ["3", "5", "7", "6"], "answer": "5"},
        {"question": "Quel est l’écart-type de 1, 3, 5 ?", "options": ["1", "2", "2.24", "1.5"], "answer": "2.24"}
    ],
    "Géométrie": [
        {"question": "Calculez la somme des angles d’un triangle.", "options": ["90°", "180°", "270°", "360°"], "answer": "180°"},
        {"question": "Combien d’angles droits dans un carré ?", "options": ["1", "2", "3", "4"], "answer": "4"},
        {"question": "Quelle est la formule de l’aire d’un cercle ?", "options": ["πr²", "2πr", "πd²", "πd"], "answer": "πr²"}
    ]
}

# Chemin des fichiers JSON
quiz_path = "quiz_structure"

# Ajouter ou compléter les questions dans les fichiers JSON
for level, themes in levels.items():
    level_path = os.path.join(quiz_path, level.replace(" ", "_"))
    os.makedirs(level_path, exist_ok=True)  # Crée les dossiers s'ils n'existent pas

    for theme in themes:
        theme_file = os.path.join(level_path, f"{theme.replace(' ', '_')}.json")
        
        # Charger les questions existantes
        if os.path.exists(theme_file):
            with open(theme_file, 'r') as file:
                existing_questions = json.load(file)
        else:
            existing_questions = []

        # Compléter avec des questions par défaut si le fichier est vide
        if len(existing_questions) == 0:
            updated_questions = default_questions.get(theme, [])
        else:
            updated_questions = existing_questions

        # Sauvegarder les mises à jour
        with open(theme_file, 'w') as file:
            json.dump(updated_questions, file, indent=4)

print("Tous les fichiers JSON ont été complétés avec des questions.")