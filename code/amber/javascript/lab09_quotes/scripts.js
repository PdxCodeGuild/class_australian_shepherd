// let quote1 = document.querySelector('#quote1')
// let quote2 = document.querySelector('#quote2')
// let quote3 = document.querySelector('#quote3')
// let quote4 = document.querySelector('#quote4')
// let quote5 = document.querySelector('#quote4')

let quote = document.querySelector('#quote')
let quoteSection = document.querySelector('#quoteSection')
let page = 1
let filterTerm = ''

function getData(){
  axios({
    method: 'get',
    url: 'https://favqs.com/api/quotes',
    headers: {
      Authorization: 'Token token="49ed81dec6143633eabecd0d09718beb"',
    },
    params: {
      page: page,
      filter: filterTerm
  }
}).then((response) => {
    quoteSection.innerHTML = ''
    let dataArray = response.data
    page = dataArray.page
    let quotesArray = dataArray.quotes

    for (i = 0; i < quotesArray.length; i++) {
      quoteSection.innerHTML += `<p>${quotesArray[i].author}</p><p>${quotesArray[i].body}</p>`
    }

    console.log(response)
    console.log(page)
    // console.log(dataArray)
    // console.log(quotesArray)
    // console.log(quotesArray.length)

    // quote1.innerHTML = quotesArray[0].author
    // quote2.innerHTML = quotesArray[0].body
}).catch((error) => {
        console.log(error)
    })
}

// getData()

let filter = document.querySelector('#filterBtn')
let filterInput = document.querySelector('#filterInput')
let nextPage = document.querySelector('#nextBtn')

filter.onclick = function () {
  filterTerm = filterInput.value
  getData()

}

nextPage.onclick = function () {
  page = page + 1
  console.log(page)
  quoteSection.innerHTML += ''
  getData()

}
