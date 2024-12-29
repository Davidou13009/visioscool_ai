
document.addEventListener('DOMContentLoaded', function () {
    const quizContainer = document.getElementById('quiz-container');
    let currentQuestionIndex = 0;
    let score = 0;
    let questions = [];

    fetch('/quiz')
        .then(response => response.json())
        .then(data => {
            questions = data;
            loadQuestion();
        });

    function loadQuestion() {
        const questionObj = questions[currentQuestionIndex];
        quizContainer.innerHTML = `
            <div class="question">${questionObj.question}</div>
            <ul class="options">
                ${questionObj.options.map(option => `<li><button onclick="checkAnswer('${option}')">${option}</button></li>`).join('')}
            </ul>
        `;
    }

    window.checkAnswer = function (selected) {
        const correctAnswer = questions[currentQuestionIndex].answer;
        if (selected === correctAnswer) {
            score++;
        }
        currentQuestionIndex++;
        if (currentQuestionIndex < questions.length) {
            loadQuestion();
        } else {
            quizContainer.innerHTML = `<h2>Score final : ${score} / ${questions.length}</h2>`;
        }
    };
});
