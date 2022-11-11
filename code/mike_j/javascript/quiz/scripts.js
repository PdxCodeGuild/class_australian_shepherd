const app = Vue.createApp({
    data(){
        return{
            dataArray: [],
        }
    },
    methods:{
        getData(){
            let amount = 10
            let category = 15
            let difficulty = "easy"
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
            })
        }
    },
})