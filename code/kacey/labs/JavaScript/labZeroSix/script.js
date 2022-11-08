const app = Vue.createApp({
    data() {
        return {
            question: "what",
        };
    },
    methods: {
        getQuizData() {
            axios({
                method: "get",
                url: `https://opentdb.com/api.php`,
                params: {
                    amount: 10,
                    category: 18,
                    difficulty: "easy",
                    type: "multiple",
                },
            })
                .then((response) => {
                    let dataArray = response.data.results;
                    console.log(dataArray);
                    console.log(dataArray[0].question);
                    this.question.push(dataArray[0].question);
                })
                .catch((error) => {
                    console.log(error);
                });
        },
    },
    mounted() {
        this.getQuizData();
    },
    setup() {
        // getQuizData();
    },
});
