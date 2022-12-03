const app = Vue.createApp({
    data(){
        return{
            difficulty: '',
            selected: '',
            questionType: '',
            score: 0,
            questions: [],
            answers: [],
            counter: 0,
            correctAnswer: ''
        }
    },
    methods:{
        getData() {
            axios({
                method: "get",
                url: "https://opentdb.com/api.php?amount=10",
                params: {
                    difficulty: this.selected,
                    type: this.questionType
                },
            }).then((response) => {
                console.log(response.data.results)
                if (this.questionType === 'multiple'){
                    questionObject = response.data['results'][this.counter]
                    console.log(questionObject)
                    this.questions = questionObject.question
                    this.correctAnswer = questionObject.correct_answer
                    this.answers[0] = questionObject.incorrect_answers[0]
                    this.answers[1] = questionObject.incorrect_answers[1]
                    this.answers[2] = questionObject.incorrect_answers[2]
                    this.answers[3] = questionObject.correct_answer
                    this.answers.sort(() => Math.random() - 0.5)
                    console.log(this.answers)   
                } else {
                    questionObject = response.data['results'][this.counter]
                    console.log(questionObject)
                    this.questions = questionObject.question
                    this.correctAnswer = questionObject.correct_answer
                    this.answers[0] = questionObject.correct_answer
                    this.answers[1] = questionObject.incorrect_answers[0]
                } 
            })    

        }
    
    },
    mounted(){
    }
})

