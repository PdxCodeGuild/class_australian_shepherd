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
                this.questionsArray = response.data.results
                console.log(this.questionsArray)

                this.incorrectAnswersArray = this.questionsArray[0].incorrect_answers
                console.log(this.incorrectAnswersArray)

                this.questionTitle = this.questionsArray[0].question
                console.log(this.questionTitle)

                this.correctAnswer = this.questionsArray[0].correct_answer
                console.log(this.correctAnswer)

                this.incorrectAnswerOne = this.questionsArray[0].incorrect_answers[0]
                console.log(this.incorrectAnswersArray[0])

                this.incorrectAnswerTwo = this.questionsArray[0].incorrect_answers[1]
                console.log(this.incorrectAnswersArray[1])

                this.incorrectAnswerThree = this.questionsArray[0].incorrect_answers[2]
                console.log(this.incorrectAnswersArray[2])


            })
        }
    },
    setup(){

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
