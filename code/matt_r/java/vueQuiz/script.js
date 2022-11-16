

const app = Vue.createApp({
    data(){
        return{
            message: 'Hello World',
            questionArray: [],
            questionArrayIndex : 0,
            currentQuestion: {},
            allQuestions: [],
            answerResults: [],

            currentScore: 0,

            correctAnswer: '',
            incorrectAnswer: '',

            catagory: '',

            userAmount: 10,
            userType: 'multiple',
            userDifficulty: 'easy',
            userCategory: 9,

            inGame: false,
            
        }
        
    },
    methods:{
        getNewQuestion(){
            // this.hideContent()
            axios({
                method: 'get',
                url:  `https://opentdb.com/api.php`,
                params: {
                    amount: this.userAmount,
                    type: this.userType,
                    difficulty: this.userDifficulty,
                    category: this.userCategory,
                    
                }
            }).then((response)=> {
                this.questionArray = response.data.results
                
                this.checkAnswers()
                
                // console.log(this.currentQuestion.incorrect_answers[0])
                // this.revealContent()
                this.inGame = true
            })
        },
        
        checkAnswers(index){
            // console.log(this.allQuestions[index])
            if (this.allQuestions[index] === this.currentQuestion.correct_answer && this.allQuestions[index] !== undefined){
                console.log(this.allQuestions[index])
                this.correctAnswer = 'correct'
                this.currentScore++
            }
            else{
                
                this.correctAnswer = this.currentQuestion.correct_answer
                this.incorrectAnswer = this.allQuestions[index]
                // console.log('INCORRECT')
                // this.answerResult.push('incorrect')
            }
            this.setAnswers()
        },
        
        setAnswers(){
            if (this.questionArrayIndex === 10){

                this.currentScore = 0
                this.getNewQuestion()
                this.questionArrayIndex = 0
                this.incorrectAnswer = ''
                this.correctAnswer = ''
                // console.log('test is it working')
            }
            else{
                
                this.currentQuestion = this.questionArray[this.questionArrayIndex]
                
                this.allQuestions = []
                
                this.allQuestions.push(this.currentQuestion.correct_answer)
                this.allQuestions.push(this.currentQuestion.incorrect_answers[0])
                this.allQuestions.push(this.currentQuestion.incorrect_answers[1])
                this.allQuestions.push(this.currentQuestion.incorrect_answers[2])
                
                // this.shuffleAnswers()
                this.allQuestions.sort(() => Math.random() -0.5)
                this.questionArrayIndex++
                console.log(this.currentQuestion.correct_answer)
                
                // console.log(this.currentQuestion.correct_answer)
            }

        },
        getMoreQuestions(){
            if (this.questionArrayIndex === 9){
                this.getNewQuestion()
                this.questionArrayIndex = 0
                // console.log('test is it working')
            }

        },
        decode(str) {
            let txt = document.createElement("textarea");
            txt.innerHTML = str;
            return txt.value;
        },


        // revealContent(){
        //     let buttondiv = document.querySelector('#choices')
        //     buttondiv.style.display='block'
        // },
        // hideContent(){
        //     let buttondiv = document.querySelector('#choices')
        //     buttondiv.style.display='none'
        // },

        

        
    },
    setup(){
        
    }
})
