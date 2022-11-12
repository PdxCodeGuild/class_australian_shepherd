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
            // allAnswers: [],
            score: 0,

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
                this.hideIntroScreen()

                this.questionsArray = response.data.results
                // console.log(this.questionsArray)

                this.incorrectAnswersArray = this.questionsArray[0].incorrect_answers
                // console.log(this.incorrectAnswersArray)

                this.questionTitle = this.questionsArray[0].question
                // console.log(this.questionTitle)

                this.correctAnswer = this.questionsArray[0].correct_answer
                // console.log(this.correctAnswer)

                this.incorrectAnswerOne = this.questionsArray[0].incorrect_answers[0]
                // console.log(this.incorrectAnswersArray[0])

                this.incorrectAnswerTwo = this.questionsArray[0].incorrect_answers[1]
                // console.log(this.incorrectAnswersArray[1])

                this.incorrectAnswerThree = this.questionsArray[0].incorrect_answers[2]
                // console.log(this.incorrectAnswersArray[2])

                this.allAnswers = []

                this.allAnswers[0] = this.correctAnswer
                this.allAnswers[1] = this.incorrectAnswerOne
                this.allAnswers[2] = this.incorrectAnswerTwo
                this.allAnswers[3] = this.incorrectAnswerThree

                // console.log(this.allAnswers)
                this.allAnswers.sort(() => Math.random() - 0.5)
                // console.log(this.allAnswers)

                let btn1 = document.querySelector('#btn1')
                let btn2 = document.querySelector('#btn2')
                let btn3 = document.querySelector('#btn3')
                let btn4 = document.querySelector('#btn4')

                btn1.innerHTML = this.allAnswers[0]
                btn2.innerHTML = this.allAnswers[1]
                btn3.innerHTML = this.allAnswers[2]
                btn4.innerHTML = this.allAnswers[3]






                // then, selectanswer onclick, if whatever question === correctanswer
                // and clear out everythign and show correct
                // and add point to score
                // else same but show incorrect and take away point
                // console.log(allAnswers)
            })

        },
        selectAnswer(btn){

            console.log(btn)
            console.log(btn.innerHTML)


            // if (btn.innerHTML === this.correctAnswer){
            //     console.log(btn.innerHTML)

            // }
            //
            // if whatever === correctanswer
            // remove other buttons and display it was right
            // else show something that clears em out and shows it was wrong and what the correct answer was
            // maybe change innerhtml of start button to say next question or something?
            // something that adds or subtracts score

            // this.score =

        },
        hideIntroScreen(){
            let startBtn = document.querySelector('#startBtn')
            startBtn.style.display = 'none'
            let questionScreen = document.querySelector("#questions-container")
            questionScreen.style.display = 'flex'
            let nextBtn = document.querySelector('#nextBtn')
            nextBtn.style.display = 'block'
            // console.log(startBtn)
        },
        // updateScore(){
        //     if
        // }
        // i guess make another method that does blahblahblah then calls it in blah
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
