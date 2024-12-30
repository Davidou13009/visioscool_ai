import os
import json

# Définir les nouvelles questions avancées pour Première Spé Maths (Analyse et Probabilités)
questions_premiere_advanced = {
    "Analyse": [
        {"question": "Calculez la dérivée de f(x) = 4x³ - 2x² + 5x - 3.", 
         "options": ["12x² - 4x + 5", "12x² - 4x + 3", "12x² + 4x - 3", "12x² - 2x + 5"], 
         "answer": "12x² - 4x + 5"},
        {"question": "La vitesse d’un objet est donnée par v(t) = 3t² - 4t + 2. Quelle est l'accélération à t = 2 ?", 
         "options": ["4", "6", "7", "8"], 
         "answer": "6"},
        {"question": "Une fonction affine f(x) = ax + b passe par les points (1, 3) et (4, 8). Déterminez la valeur de a.", 
         "options": ["2", "5/3", "1", "3/2"], 
         "answer": "5/3"}
    ],
    "Probabilités": [
        {"question": "Dans un tirage de deux cartes dans un jeu de 52 cartes, quelle est la probabilité d'obtenir une carte rouge puis une carte noire ?", 
         "options": ["1/26", "1/52", "1/4", "1/17"], 
         "answer": "1/26"},
        {"question": "Dans un tirage répété de 1000 fois d’un dé équilibré, quelle est la probabilité approximative d’obtenir un 6 au moins 200 fois ?", 
         "options": ["0.2", "0.6", "0.17", "0.5"], 
         "answer": "0.2"},
        {"question": "Dans un sac contenant 5 billes rouges et 7 billes bleues, une bille est tirée au hasard. Après cette action, la bille est remise dans le sac et une nouvelle bille est tirée. Quelle est la probabilité d'obtenir une bille rouge au second tirage, sachant que la première bille tirée était bleue ?", 
         "options": ["5/12", "5/7", "7/12", "1/2"], 
         "answer": "5/12"}
    ]
}

# Définir le chemin de votre dossier de projet Flask local
quiz_path_premiere = './quiz_structure/Première_Spé_Maths'

# Mettre à jour le fichier JSON pour Analyse et Probabilités
for theme, questions in questions_premiere_advanced.items():
    theme_file = os.path.join(quiz_path_premiere, f"{theme.replace(' ', '_')}.json")
    
    # Remplacer le contenu avec les nouvelles questions
    with open(theme_file, 'w') as file:
        json.dump(questions, file, indent=4)

print("Les fichiers JSON pour Première Spé Maths ont été mis à jour avec les nouvelles questions adaptées.")