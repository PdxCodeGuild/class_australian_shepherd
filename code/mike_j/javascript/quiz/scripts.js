const app = Vue.createApp({
    data(){
        return{
            questionObject: [],
            allQuestions: [],
            correctAnswer: "",
            diff: "",
            cat: "",
            counter: 0
        }
    },
    methods:{
        getData(){
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
                let data = response.data
                questionObject = data["results"][0]
                correctAnswer = questionObject.correct_answer
                document.querySelector("#question").innerHTML = questionObject.question
                this.allQuestions[0] = questionObject.correct_answer
                this.allQuestions[1] = questionObject.incorrect_answers[0]
                this.allQuestions[2] = questionObject.incorrect_answers[1]
                this.allQuestions[3] = questionObject.incorrect_answers[2]
                this.allQuestions.sort(() => 0.5 - Math.random())    
                document.querySelectorAll(".btn").forEach(button => {
                    button.innerHTML = this.allQuestions[this.counter]
                    this.counter++
                })

                this.counter = 0
                document.querySelector("#result").innerHTML = ""

                document.querySelectorAll(".btn").forEach(button => {
                    button.addEventListener("click", () => {
                        console.log(button.innerHTML)
                        if (button.innerHTML === correctAnswer){
                            showAnswer("correct")
                        }
                        else{
                            showAnswer("incorrect")
                        }     
                    })
                })

                let showAnswer = function(result) {
                    if (result === "correct"){
                        document.querySelector("#result").innerHTML = "You got it! " + correctAnswer + "."
                        document.querySelector("#result").style.color = "green"
                    }
                    else{
                        document.querySelector("#result").innerHTML = "The correct answer was actually " + correctAnswer + "."
                        document.querySelector("#result").style.color = "red"       
                    }
                }
            }
            )},        
        }
    })