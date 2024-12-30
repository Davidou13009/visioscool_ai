import os
import json

# Définir les nouvelles questions pour Terminale Spé Maths (Analyse, Probabilités et Géométrie)
questions_terminale = {
    "Analyse": [
        {"question": "Calculez la dérivée de f(x) = x³ - 6x² + 9x - 5.",
         "options": ["3x² - 12x + 9", "3x² - 12x + 5", "3x² - 5", "6x² - 9x + 5"],
         "answer": "3x² - 12x + 9"},
        {"question": "Calculez la limite de f(x) = (x² - 1)/(x - 1) lorsque x tend vers 1.",
         "options": ["1", "2", "0", "∞"],
         "answer": "2"},
        {"question": "Calculez l'intégrale de f(x) = 4x² dx.",
         "options": ["x³ + C", "2x³ + C", "4x³ + C", "x² + C"],
         "answer": "4x³ + C"}
    ],
    "Probabilités": [
        {"question": "Dans une urne contenant 4 billes rouges et 6 billes bleues, une bille est tirée. Puis, la bille est remise dans l'urne. Quelle est la probabilité de tirer une bille rouge puis une bille bleue ?",
         "options": ["2/5", "4/25", "1/5", "2/5"],
         "answer": "4/25"},
        {"question": "Dans un échantillon de taille n = 1000, la moyenne observée est 50 et l'écart-type est 10. Quelle est la probabilité d'obtenir une valeur entre 45 et 55 ?",
         "options": ["0.6826", "0.50", "0.68", "0.68"],
         "answer": "0.6826"},
        {"question": "On tire un échantillon de taille 30. Quelle est l'estimation de la moyenne ?",
         "options": ["30", "15", "20", "25"],
         "answer": "15"}
    ],
    "Géométrie (Vecteurs)": [
        {"question": "Les vecteurs u(2, 4) et v(1, 2) sont-ils colinéaires ?",
         "options": ["Oui", "Non", "Impossible à dire", "Ils sont orthogonaux"],
         "answer": "Oui"},
        {"question": "Calculez le produit scalaire des vecteurs u(1, 2) et v(2, 3).",
         "options": ["8", "5", "6", "7"],
         "answer": "8"},
        {"question": "Soit u(1, 2) et v(3, 4), quelle est la norme du vecteur u + v ?",
         "options": ["5", "4", "3", "2"],
         "answer": "5"}
    ]
}

# Chemin du fichier JSON pour Terminale Spé Maths
quiz_path_terminale = './quiz_structure/Terminale_Spé_Maths'

# Mettre à jour le fichier JSON pour chaque thème de Terminale
for theme, questions in questions_terminale.items():
    theme_file = os.path.join(quiz_path_terminale, f"{theme.replace(' ', '_')}.json")
    
    # Remplacer le contenu avec les nouvelles questions
    with open(theme_file, 'w') as file:
        json.dump(questions, file, indent=4)

print("Les fichiers JSON pour Terminale Spé Maths ont été mis à jour avec les nouvelles questions adaptées.")