

const app = Vue.createApp({
    data(){
        return{
            message: 'Hello World',
            questionArray: [
               
            ],
        }
    },
    methods:{
        getNewQuestion(){
            axios({
                method: 'get',
                url:  `https://opentdb.com/api.php?amount=10&type=multiple`
            }).then((response) => {
                questValue = response.data.results[0].question
                let QandA = {
                    questions: this.questValue,
                    // answer1: this.answer1Value,
                    // answer2: this.answer2Value,
                    // answer3: this.answer3Value,
                    // answer4: this.answer4Value,
                    
                }
                
                this.questionArray.push(QandA)
                console.log(questValue)
                console.log(QandA)
                console.log(QandA.questions)
            })
        }
    },
    setup(){
       
        
    }
})