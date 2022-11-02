let quote1 = document.querySelector('#quote1')
let quote2 = document.querySelector('#quote2')
let quote3 = document.querySelector('#quote3')
let quote4 = document.querySelector('#quote4')
let quote5 = document.querySelector('#quote4')


function getData(){
    axios({
        method: 'get',
        url: 'https://favqs.com/api',
        params: {
          id: 4,
          author: "Albert Einstein",
          body: "Make everything as simple as possible, but not simpler.",
        }
    }).then((response) => {
        let dataArray = response
        console.log(dataArray)
        // console.log(dataArray)
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
