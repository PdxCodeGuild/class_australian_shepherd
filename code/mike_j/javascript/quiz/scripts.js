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
            let amount = 20
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
            },
        )},
        nextQuestion: function() {
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
            console.log(this.data[this.questionCounter].correct_answer)
            this.questionCounter += 1
        },
        showAnswer: function(result) {
            if (result === "correct"){
                document.querySelector("#result").innerHTML = "You got it! " + this.correctAnswer + "."
                document.querySelector("#result").style.color = "green"
                console.log(this.correctAnswer)
            }
            else{
                document.querySelector("#result").innerHTML = "The correct answer was actually " + this.correctAnswer + "."
                document.querySelector("#result").style.color = "red"       
            }    
        }},
        mounted() {
            document.querySelector("#result").innerHTML = ""
            document.querySelectorAll(".btn").forEach(button => {
            button.addEventListener("click", () => {
            if (button.innerHTML === this.correctAnswer){
                showAnswer("correct")
                this.correct += 1
                document.querySelector("#correct").innerHTML = this.correct
                document.querySelector("#correct").style.color = "green"
            }
            else{
                showAnswer("incorrect")
                this.incorrect += 1
                document.querySelector("#incorrect").innerHTML = this.incorrect
                document.querySelector("#incorrect").style.color = "red"
            }   
        })
    })
})