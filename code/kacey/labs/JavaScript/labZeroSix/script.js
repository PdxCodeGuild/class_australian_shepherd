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
            i: 0,
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
                    // let i = 0;
                    currentQuestionObject = {};
                    currentQuestionIndex = 0;
                    wrongAnswers = [];
                    allAnswers = [];
                    i = this.i;
                    this.dataArray = response.data.results;

                    console.log("this.dataArray", this.dataArray);
                    console.log(
                        "this.dataArray[0].question",
                        this.dataArray[0].question
                    );

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

                    console.log(
                        "this.currentQuestionObject.correct_answer",
                        this.currentQuestionObject.correct_answer
                    );
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
            console.log("choice", choice);
            if (choice === this.correctAnswer) {
                // console.log("correct");
                resultDisplay.innerHTML = this.decode(
                    `${this.correctAnswer} is Correct `
                );
                this.currentQuestionIndex++;
                this.score++;
                console.log(
                    "this.currentQuestionIndex",
                    this.currentQuestionIndex
                );
                console.log("this.score", this.score);
            } else {
                resultDisplay.innerHTML = this.decode(
                    `${choice} was Incorrect, ${this.correctAnswer} was the Correct Answer.`
                );
                this.currentQuestionIndex++;
            }
            this.getQuizData();
        },
        decode(str) {
            let txt = document.createElement("textarea");
            txt.innerHTML = str;
            return txt.value;
        },
        scoreKeeper() {},
    },
    mounted() {},
    setup() {
        // getQuizData();
    },
});
