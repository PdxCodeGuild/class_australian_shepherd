
let content = document.querySelector('#content')
let answer1 = document.querySelector('#answer1')
let answer2 = document.querySelector('#answer2')
let answer3 = document.querySelector('#answer3')
let answer4 = document.querySelector('#answer4')



function getData(){
    axios({
        method: 'get',
        url: 'https://opentdb.com/api.php',
        params: {
            amount: 10,
            category: 18,
            difficulty: 'hard'
        }
    }).then((response) => {
        let dataArray = response.data.results
        console.log(dataArray[0])
        console.log(dataArray[0].question)
        console.log(dataArray[0].correct_answer)
        content.innerHTML = dataArray[0].question

        answer1.innerHTML = dataArray[0].correct_answer
        answer2.innerHTML = dataArray[0].incorrect_answers[0]
        answer3.innerHTML = dataArray[0].incorrect_answers[1]
        answer4.innerHTML = dataArray[0].incorrect_answers[2]

    }).catch((error) => {
        console.log(error)
    })
}

getData()

