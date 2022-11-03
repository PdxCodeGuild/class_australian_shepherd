let quote1 = document.querySelector('#quote1')
let quote2 = document.querySelector('#quote2')
let quote3 = document.querySelector('#quote3')
let quote4 = document.querySelector('#quote4')
let quote5 = document.querySelector('#quote4')


function getData(){
    axios({
        method: 'GET',
        url: 'https://favqs.com/api/qotd',
        params: {
          "id": 4,
          "author": "Albert Einstein",
          "body": "Make everything as simple as possible, but not simpler.",
        }
    }).then((response) => {
        let qotd = response.data.quote
        console.log(qotd)
        // console.log(dataArray)
        // console.log(dataArray[0].correct_answer)
        // content.innerHTML = dataArray[0].question

        quote1.innerHTML = qotd.author
        quote2.innerHTML = qotd.body
        // answer2.innerHTML = dataArray[0].incorrect_answers[0]
        // answer3.innerHTML = dataArray[0].incorrect_answers[1]
        // answer4.innerHTML = dataArray[0].incorrect_answers[2]

    }).catch((error) => {
        console.log(error)
    })
}

getData()
