let quote1 = document.querySelector('#quote1')
let quote2 = document.querySelector('#quote2')
let quote3 = document.querySelector('#quote3')
let quote4 = document.querySelector('#quote4')
let quote5 = document.querySelector('#quote4')


function getData(){
    axios({
        method: 'get',
        url: 'https://favqs.com/api/qotd',
        params: {
            amount: 10,
            category: 18,
            difficulty: 'hard'
        }
    }).then((response) => {
        let dataArray = response.data.results
        // console.log(dataArray[0])
        // console.log(dataArray[0].question)
        // console.log(dataArray[0].correct_answer)
        // content.innerHTML = dataArray[0].question

        // answer1.innerHTML = dataArray[0].correct_answer
        // answer2.innerHTML = dataArray[0].incorrect_answers[0]
        // answer3.innerHTML = dataArray[0].incorrect_answers[1]
        // answer4.innerHTML = dataArray[0].incorrect_answers[2]

    }).catch((error) => {
        console.log(error)
    })
}

getData()
