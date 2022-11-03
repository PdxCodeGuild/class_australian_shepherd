let quote1 = document.querySelector('#quote1')
let quote2 = document.querySelector('#quote2')
let quote3 = document.querySelector('#quote3')
let quote4 = document.querySelector('#quote4')
let quote5 = document.querySelector('#quote4')



function getData(){
  axios({
    method: 'get',
    url: 'https://favqs.com/api/quotes',
    headers: {
      Authorization: 'Token token="49ed81dec6143633eabecd0d09718beb"',
    }
}).then((response) => {
    let dataArray = response.data
    let quotesArray = dataArray.quotes

    for (i = 0; i < quotesArray.length; i++) {
      console.log(quotesArray[i].author)
      console.log(quotesArray[i].body)
    }

    // console.log(dataArray)
    // console.log(quotesArray)
    // console.log(quotesArray.length)

    // quote1.innerHTML = quotesArray[0].author
    // quote2.innerHTML = quotesArray[0].body
}).catch((error) => {
        console.log(error)
    })
}

getData()
