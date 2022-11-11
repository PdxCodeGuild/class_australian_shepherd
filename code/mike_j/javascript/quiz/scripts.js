const app = Vue.createApp({
    data(){
        return{
            dataArray: [],
            diff: "",
            cat: "",
            question: document.querySelector("#question"),
            btn1: document.querySelector("#btn1"),
            btn2: document.querySelector("#btn2"),
            btn3: document.querySelector("#btn3"),
            btn4: document.querySelector("#btn4")
        }
    },
    methods:{
        getData(){
            let amount = 10
            let category = this.cat
            difficulty = this.diff
            let type = "multiple"
            axios({
                method: 'get',
                url: `https://opentdb.com/api.php?`,
                params: {
                    amount: amount,
                    category: category,
                    difficulty: difficulty,
                    type: type
                }
            }).then((response) => {
                let dataArray = response.data
                console.log(dataArray)
                question.innerHTML = dataArray.results[0].question
                btn1.innerHTML = dataArray.results[0].correct_answer
                btn2.innerHTML = dataArray.results[0].incorrect_answers[0]
                btn3.innerHTML = dataArray.results[0].incorrect_answers[1]
                btn4.innerHTML = dataArray.results[0].incorrect_answers[2]
            })
        }
    }
})