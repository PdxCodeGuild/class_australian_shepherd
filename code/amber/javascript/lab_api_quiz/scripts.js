// Tell the users the correct answer when they are wrong.
// maybe add a class to all buttons and queryselect all to hide them while displaying correct answer.
// maybe use green sock to do a delay while displaying answer before moving on to next

// Have the user select the questions category. Either general or specified.

// Have the user select the quiz difficulty.

// Remove encoding from html text
// function decode(str) {
// let txt = document.createElement("textarea");
// txt.innerHTML = str;
// return txt.value;
// }

// how to handle if the end of the questions array is reached?
// make startBtn reappear with play again?? flip inGame bool??
// reset score

// make large answers fit in buttons


const app = Vue.createApp({
    data(){ // global scope/variables
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

        }
    },
    methods:{
        startGame(){ // @click function call in html to start game
            this.getInfo() // WOULD NEED TO CHANGE THIS TO BE AFTER DROPDOWN SELECTIONS ARE ADDED

            let startBtn = document.querySelector('#startBtn')
            startBtn.style.display = 'none' // hide start button after game begins
        },

        // decode(str) {
        //     let txt = document.createElement("textarea")
        //     txt.innerHTML = str
        //     return txt.value
        //     },

        getInfo(){ // generate API request
            axios({
                method: 'get',
                url: `https://opentdb.com/api.php`,
                params: {
                    amount: 50,
                    type: 'multiple', // MAKE AN ARRAY OF OPTIONS?
                    difficulty: 'easy', // MAKE AN ARRAY OF OPTIONS?
                    // MAKE AN ARRAY CATEGORY?
                    // DO DROPDOWNS FOR EACH?
                }
            }).then((response) => { // assign global variables to response data in local scope
                this.inGame = true // connects to v-if in html #questions-container to render after start button is clicked

                this.questionsArray = response.data.results // all the question objects in the response
                console.log(this.questionsArray.length)

                this.currentQuestionObj = this.questionsArray[0] // current question object (question, correct, incorrect array). starts at [0] here since this is the first iteration but will be [currentQuestionIndex] later, which acts as a counter
                // console.log(this.currentQuestionObj)

                this.nextQuestion()
                this.makeButtonArray()
            })
        },

        makeButtonArray(){ // assigns correct and incorrect answers to single array and then randomizes them
            this.allAnswers[0] = this.correctAnswer.toUpperCase()
            this.allAnswers[1] = this.incorrectAnswersArray[0].toUpperCase()
            this.allAnswers[2] = this.incorrectAnswersArray[1].toUpperCase()
            this.allAnswers[3] = this.incorrectAnswersArray[2].toUpperCase()

            this.allAnswers.sort(() => Math.random() - 0.5)
        },

        selectAnswer(btn){
            let answerPopUp = document.querySelector('#answerPopUp')
            let questionsContainer = document.querySelector('#questionsContainer')


            if (btn === this.correctAnswer){

                this.increaseScore()
                console.log('correct')

            }
            else{
                questionsContainer.style.display = 'none'
                answerPopUp.style.display = 'flex'

                this.decreaseScore()
                console.log('incorrect')
            }

            this.nextQuestion()
        },

        nextQuestion(){
            this.currentQuestionIndex++ // counter that goes through questions array into new currentQuestionObj
            this.currentQuestionObj = this.questionsArray[this.currentQuestionIndex]

            this.questionTitle = this.currentQuestionObj.question // extracts question title

            this.correctAnswer = this.currentQuestionObj.correct_answer // extracts correct answer

            this.incorrectAnswersArray = this.currentQuestionObj.incorrect_answers // extracts incorrect answer array

            this.makeButtonArray()

        },
        // revealAnswer(){
        //     let answerPopUp = document.querySelector('#answerPopUp')
        //     if

        // },

        increaseScore(){
            this.score++
        },
        decreaseScore(){
            this.score--
        },
        resetScore(){ // use this when playAgain function is made
            this.score = 0
        },
        // playAgain(){
        //     if (this.currentQuestionIndex === this.questionsArray.length){}
        // }

    },

    mounted(){

    }
})

        // hideIntroScreen(){
        //     let startBtn = document.querySelector('#startBtn')
        //     startBtn.style.display = 'none'
        //     let questionScreen = document.querySelector("#questions-container")
        //     questionScreen.style.display = 'flex'
        //     let nextBtn = document.querySelector('#nextBtn')
        //     nextBtn.style.display = 'block'
        //     // console.log(startBtn)
        // },
