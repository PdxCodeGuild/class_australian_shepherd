const app = Vue.createApp({
    data() {
        return {
            question: "what",
            answers: "",
            amount: 10,
            category: 18,
            difficulty: "easy",
            type: "multiple",
            score: 0,
            dataArray: [],
            correctAnswer: "",

            currentQuestionObject: {},
            currentQuestionIndex: 0,
            wrongAnswers: [],
            allAnswers: [],
        };
    },
    methods: {
        getQuizData() {
            axios({
                method: "get",
                url: `https://opentdb.com/api.php`,
                params: {
                    amount: this.amount,
                    category: this.category,
                    difficulty: this.difficulty,
                    type: this.type,
                },
            })
                .then((response) => {
                    let i = 0;
                    this.dataArray = response.data.results;
                    console.log(this.dataArray);
                    console.log(this.dataArray[0].question);

                    this.correctAnswer = this.dataArray[i].correct_answer;
                    questionBox.innerHTML = this.dataArray[i].question;

                    this.currentQuestionObject =
                        this.dataArray[this.currentQuestionIndex];
                    this.wrongAnswers =
                        this.dataArray[
                            this.currentQuestionIndex
                        ].incorrect_answers;
                    this.allAnswers = this.wrongAnswers;
                    this.allAnswers.push(
                        this.currentQuestionObject.correct_answer
                    );
                    this.correctAnswer =
                        this.currentQuestionObject.correct_answer;
                    this.shuffleOrder();

                    console.log(this.currentQuestionObject.correct_answer);
                    // answer1.innerHTML = this.dataArray[i].correct_answer;
                    // answer2.innerHTML = this.dataArray[i].incorrect_answers[0];
                    // answer3.innerHTML = this.dataArray[i].incorrect_answers[1];
                    // answer4.innerHTML = this.dataArray[i].incorrect_answers[2];
                    if (this.type === "multiple") {
                        answer3.style.display = "block";
                        answer4.style.display = "block";
                    } else {
                        answer3.style.display = "none";
                        answer4.style.display = "none";
                    }
                    this.question = this.dataArray[i].question;
                    this.i++;
                })
                .catch((error) => {
                    console.log(error);
                });
        },
        gameCreator() {
            this.getQuizData();
        },
        shuffleOrder() {
            this.allAnswers.sort(() => Math.random() - 0.5);
            console.log(this.allAnswers);
        },
        wrongOrRight(choice) {
            console.log(choice);
            if (choice === this.correctAnswer) {
                console.log("correct");
            }
        },
    },
    mounted() {},
    setup() {
        // getQuizData();
    },
});
