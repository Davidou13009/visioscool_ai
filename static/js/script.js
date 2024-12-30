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

            questions.forEach((q, index) => {
                const questionElement = document.createElement('div');
                questionElement.classList.add('question');
                questionElement.innerHTML = `
                    <p><strong>${index + 1}. ${q.question}</strong></p>
                    <ul>
                        ${q.options.map(option => `<li><button class="answer">${option}</button></li>`).join('')}
                    </ul>
                `;
                quizContainer.appendChild(questionElement);
            });
        })
        .catch(err => {
            console.error(err);
            quizContainer.innerHTML = "<p>Erreur lors du chargement des questions.</p>";
        });
    });
});
