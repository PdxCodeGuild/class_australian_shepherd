const app = Vue.createApp({
    data(){
        return{
            questionsArray: [],
            questionTitle: '',
            incorrectAnswersArray: [],
            correctAnswer: '',
            incorrectAnswerOne: '',
            incorrectAnswerTwo: '',
            incorrectAnswerThree: '',
            allAnswers: [],
            score: 0,
            currentQuestionObj: {},
            currentQuestionIndex: 0,
            inGame: false,
            difficultyChoice: '',
            categoryChoice: '',
            difficultyChosen: false,
            categoryChosen: false,
            choicesMade: false,
            difficultyLevels: [],
            catMenu: false,
            currentQuestionCat: '',
            wrongAnswer: false,
        }
    },
    methods:{
        chooseDifficulty(diff){
            console.log(diff)
            this.difficultyChoice = diff
            console.log(this.difficultyChoice)
            this.catMenu = true
        },
        chooseCategory(cat){
            console.log(cat)
            this.categoryChoice = cat
            console.log(this.categoryChoice)
            this.catMenu = false
            this.choicesMade = true
            // startGame()
        },
        startGame(){
            this.getInfo()
            let startBtn = document.querySelector('#startBtn')
            startBtn.style.display = 'none'
        },

        decode(str) {
            let txt = document.createElement("textarea")
            txt.innerHTML = str
            return txt.value
            },

        getInfo(){
            axios({
                method: 'get',
                url: `https://opentdb.com/api.php`,
                params: {
                    amount: 50,
                    type: 'multiple',
                    category: this.categoryChoice,
                    difficulty: this.difficultyChoice,
                }
            }).then((response) => {
                // console.log(this.difficultyChoice)
                // console.log(this.categoryChoice)
                this.inGame = true

                this.questionsArray = response.data.results
                // console.log(this.questionsArray.length)
                // console.log(this.questionsArray)

                this.currentQuestionObj = this.questionsArray[0]
                // console.log(this.currentQuestionObj)

                this.nextQuestion()
                this.makeButtonArray()
            })
        },
        makeButtonArray(){
            this.allAnswers[0] = this.correctAnswer.toUpperCase()
            this.allAnswers[1] = this.incorrectAnswersArray[0].toUpperCase()
            this.allAnswers[2] = this.incorrectAnswersArray[1].toUpperCase()
            this.allAnswers[3] = this.incorrectAnswersArray[2].toUpperCase()
            this.allAnswers.sort(() => Math.random() - 0.5)
        },
        selectAnswer(btn){
            if (btn === this.correctAnswer){
                this.increaseScore()
                this.nextQuestion()
                console.log('correct')
            }
            else{
                this.wrongAnswer = true
                this.inGame = false
                this.decreaseScore()
                console.log('incorrect')
            }

            // this.nextQuestion()
        },
        // revealAnswer(){
        //     this.wrongAnswer = true
        //     let questionsContainer = document.querySelector('#questionsContainer')
        //     questionsContainer.style.display = 'none'
        // },
        // hidePopup(){
        //     this.wrongAnswer = false
        //     let questionsContainer = document.querySelector('#questionsContainer')
        //     questionsContainer.style.display = 'flex'
        // },
        nextQuestion(){
            this.wrongAnswer = false
            this.inGame = true
            this.currentQuestionIndex++ // counter that goes through questions array into new currentQuestionObj
            this.currentQuestionObj = this.questionsArray[this.currentQuestionIndex]

            this.questionTitle = this.currentQuestionObj.question // extracts question title

            this.correctAnswer = this.currentQuestionObj.correct_answer // extracts correct answer

            this.incorrectAnswersArray = this.currentQuestionObj.incorrect_answers // extracts incorrect answer array

            this.makeButtonArray()

        },
        increaseScore(){
            this.score++
        },
        decreaseScore(){
            this.score--
        },
        resetScore(){ // use this when playAgain function is made
            this.score = 0
        },
    },
    mounted(){

    }
})

// how to handle if the end of the questions array is reached?
// make startBtn reappear with play again?? flip inGame bool??
// reset score
