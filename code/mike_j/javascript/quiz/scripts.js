const app = Vue.createApp({
    data(){
        return{
            data: [],
            questionObject: [],
            questionCounter: 0,
            correctAnswer: "",
            diff: "",
            cat: "",
            counter: 0,
            correct: 0,
            incorrect: 0
        }
    },
    methods:{
        getData(){
            this.correct = 0
            this.incorrect = 0
            this.questionCounter = 0
            document.querySelector("#next").style.pointerEvents = "auto"
            document.querySelector("#question").innerHTML = ""
            document.querySelector("#correct").innerHTML = ""
            document.querySelector("#incorrect").innerHTML = ""
            document.querySelector("#result").innerHTML = ""
            document.querySelector("#result").style.color = "black"
            document.querySelectorAll(".btn").forEach(button => {
                button.innerHTML = ""
            })
            let amount = 10
            let category = this.cat
            difficulty = this.diff
            let type = "multiple"
            axios({
                method: "get",
                url: `https://opentdb.com/api.php?`,
                params: {
                    amount: amount,
                    category: category,
                    difficulty: difficulty,
                    type: type
                }
            }).then((response) => {
                this.data = response.data.results
                document.querySelector("#result").innerHTML = "Questions loaded. Press 'Next Question' to begin."
            }
        )},
        nextQuestion: function() {
            if (this.questionCounter < 10) {
                document.querySelector("#result").innerHTML = ""
                this.correctAnswer = this.data[this.questionCounter].correct_answer
                document.querySelector("#question").innerHTML = this.data[this.questionCounter].question
                this.questionObject[0] = this.data[this.questionCounter].correct_answer
                this.questionObject[1] = this.data[this.questionCounter].incorrect_answers[0]
                this.questionObject[2] = this.data[this.questionCounter].incorrect_answers[1]
                this.questionObject[3] = this.data[this.questionCounter].incorrect_answers[2]
                this.questionObject.sort(() => 0.5 - Math.random()) 
                document.querySelectorAll(".btn").forEach(button => {
                    button.innerHTML = this.questionObject[this.counter]
                    this.counter++
                })
                this.counter = 0
                this.questionCounter += 1
            }
            else {
                document.querySelector("#next").style.pointerEvents  = "none"
                document.querySelector("#result").innerHTML = "All questions answered. Choose category and difficulty then press 'Submit' to play again."
                document.querySelector("#result").style.color = "black"
                this.questionCounter = 0
                this.correct = 0
                this.incorrect = 0
                document.querySelector("#question").innerHTML = ""
                document.querySelectorAll(".btn").forEach(button => {
                    button.innerHTML = ""
                })
            }
        }
    },
    mounted() {
        document.querySelectorAll('.btn').forEach(button => {
            button.addEventListener('click', () => {
                if (button.innerHTML === this.correctAnswer){
                    this.correct += 1
                    document.querySelector("#correct").innerHTML = this.correct
                    document.querySelector("#correct").style.color = "green"
                    document.querySelector("#result").innerHTML = "You got it! " + this.correctAnswer + "."
                    document.querySelector("#result").style.color = "green"
                }
                else{
                    this.incorrect += 1
                    document.querySelector("#incorrect").innerHTML = this.incorrect
                    document.querySelector("#incorrect").style.color = "red"
                    document.querySelector("#result").innerHTML = "The correct answer was actually " + this.correctAnswer + "."
                    document.querySelector("#result").style.color = "red"
                }   
            })
        })
    }
})        