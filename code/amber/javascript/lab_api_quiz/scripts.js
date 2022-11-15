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

        }
    },
    methods:{
        getInfo(){
            axios({
                method: 'get',
                url: `https://opentdb.com/api.php`,
                params: {
                    amount: 10,
                    type: 'multiple',
                    difficulty: 'easy'
                }
            }).then((response) => {
                 // this.hideIntroScreen()
                this.inGame = true

                this.questionsArray = response.data.results

                this.currentQuestionObj = this.questionsArray[0]

                this.nextQuestion()
                this.makeButtonArray()

            })

        },

        startGame(){
            this.getInfo()
        },

        makeButtonArray(){
            this.allAnswers[0] = this.correctAnswer
            this.allAnswers[1] = this.incorrectAnswersArray[0]
            this.allAnswers[2] = this.incorrectAnswersArray[1]
            this.allAnswers[3] = this.incorrectAnswersArray[2]

            this.allAnswers.sort(() => Math.random() - 0.5)

        },


        selectAnswer(btn){
            if (btn === this.correctAnswer){
                // MAKE THESE DO POPUPS -------------------
                console.log('correct')
            }
            else{
                console.log('incorrect')
            }

            this.nextQuestion()
        },

        nextQuestion(){
            this.currentQuestionIndex++
            this.currentQuestionObj = this.questionsArray[this.currentQuestionIndex]

            this.questionTitle = this.currentQuestionObj.question

            this.correctAnswer = this.currentQuestionObj.correct_answer

            this.incorrectAnswersArray = this.currentQuestionObj.incorrect_answers

            this.makeButtonArray()

        },

        // hideIntroScreen(){
        //     let startBtn = document.querySelector('#startBtn')
        //     startBtn.style.display = 'none'
        //     let questionScreen = document.querySelector("#questions-container")
        //     questionScreen.style.display = 'flex'
        //     let nextBtn = document.querySelector('#nextBtn')
        //     nextBtn.style.display = 'block'
        //     // console.log(startBtn)
        // },
        // MAKE UPDATESCORE FUNCTION -----------------
    },
    mounted(){

    }
})

// let startBtn = document.querySelector('#start')

// let questionObject = []
// const allQuestions = []
// let correctAnswer = ''


// async function getQuestion() {
//     const response = await fetch('https://opentdb.com/api.php?amount=10&type=multiple')
//     data = await response.json()
//     questionObject = data['results'][0]
//     correctAnswer = questionObject.correct_answer

//     allQuestions[0] = questionObject.correct_answer
//     allQuestions[1] = questionObject.incorrect_answers[0]
//     allQuestions[2] = questionObject.incorrect_answers[1]
//     allQuestions[3] = questionObject.incorrect_answers[2]

//     // console.log(allQuestions)
//     allQuestions.sort(() => Math.random() - 0.5)
//     // console.log(allQuestions)

//     document.querySelector('#question').innerHTML = questionObject.question
//     // console.log(correctAnswer)

//     document.querySelectorAll('.btn').forEach(button => {
//         button.innerHTML = allQuestions[counter]
//         counter++
//     })
//     counter = 0
// }

// getQuestion()

// let counter = 0


// document.querySelectorAll('.btn').forEach(button => {
//     button.addEventListener('click', () => {
//         console.log(button.innerHTML)
//         if (button.innerHTML === correctAnswer)
//         {
//             getQuestion()
//             showAnswer('correct')
//             disableClicking()
//             // allQuestions.pop()

//             console.log(allQuestions)
//         }
//         else{
//             getQuestion()
//             showAnswer('incorrect')
//             disableClicking()
//         }

//     })
// })

// let showAnswer = function(result) {
//     if (result === 'correct'){
//         document.querySelector('#annoying-popup').innerHTML = 'You got it! ' + correctAnswer
//         document.querySelector('#annoying-popup').style.color = 'green'
//     }
//     else{
//         document.querySelector('#annoying-popup').innerHTML = 'The correct answer was actually ' + correctAnswer
//         document.querySelector('#annoying-popup').style.color = 'red'

//     }
//     document.querySelector('#annoying-popup').style.display = 'block'
// }


// let disableClicking = function() {
//     document.querySelector('#questions-container').style.pointerEvents  = "none"
//     setTimeout(enableClicking, 1500)
// }

// let enableClicking = function() {
//     document.querySelector('#questions-container').style.pointerEvents  = "auto"
// }



// // // need to clear out answer when new page loads
