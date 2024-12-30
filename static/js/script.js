document.addEventListener('DOMContentLoaded', function () {
    const startQuizButton = document.getElementById('startQuiz');
    const quizContainer = document.getElementById('quiz-container');

    startQuizButton.addEventListener('click', () => {
        const level = document.getElementById('level').value;
        const theme = document.getElementById('theme').value;

        fetch('/quiz', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ level: level, theme: theme })
        })
        .then(response => response.json())
        .then(questions => {
            quizContainer.innerHTML = "";
            if (questions.length === 0) {
                quizContainer.innerHTML = "<p>Aucune question disponible pour ce thème.</p>";
                return;
            }

            let score = 0; // Initialisation du score

            questions.forEach((q, index) => {
                const questionElement = document.createElement('div');
                questionElement.classList.add('question');
                questionElement.innerHTML = `
                    <p><strong>${index + 1}. ${q.question}</strong></p>
                    <ul>
                        ${q.options.map(option => `<li><button class="answer">${option}</button></li>`).join('')}
                    </ul>
                    <p class="feedback" style="color: green; display: none;"></p>
                `;
                quizContainer.appendChild(questionElement);

                // Gestion des clics sur les réponses
                const buttons = questionElement.querySelectorAll('.answer');
                buttons.forEach(button => {
                    button.addEventListener('click', () => {
                        const feedback = questionElement.querySelector('.feedback');
                        if (button.textContent === q.answer) {
                            feedback.textContent = "Correct !";
                            feedback.style.color = "green";
                            score++; // Incrémenter le score
                        } else {
                            feedback.textContent = `Incorrect ! La bonne réponse était : ${q.answer}`;
                            feedback.style.color = "red";
                        }
                        feedback.style.display = "block";

                        // Désactiver les autres boutons après réponse
                        buttons.forEach(btn => btn.disabled = true);
                    });
                });
            });

            // Affichage du score final après les réponses
            const scoreElement = document.createElement('p');
            scoreElement.id = "final-score";
            quizContainer.appendChild(scoreElement);

          // Ajout du score final après toutes les réponses
const showFinalScore = () => {
    const totalQuestions = questions.length;
    const feedbackCount = quizContainer.querySelectorAll('.feedback[style*="display: block"]').length;

    if (feedbackCount === totalQuestions) {
        scoreElement.textContent = `Score final : ${score} / ${totalQuestions}`;
        scoreElement.style.fontWeight = "bold";
        scoreElement.style.marginTop = "20px";
    }
};

// Surveiller chaque réponse pour mettre à jour le score
quizContainer.addEventListener('click', () => {
    showFinalScore();
});  
        })
        .catch(err => {
            console.error(err);
            quizContainer.innerHTML = "<p>Erreur lors du chargement des questions.</p>";
        });
    });
});
