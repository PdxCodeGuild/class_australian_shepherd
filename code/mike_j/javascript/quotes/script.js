// ver.1

// let quote = document.querySelector('#quote')
// let author = document.querySelector('#author')

// axios({
//     method: 'get',
//     url: 'https://favqs.com/api/qotd'
//     }).then((response) => {
//     console.log(response.data)
//     quote.innerHTML = response.data.quote.body
//     author.innerHTML = response.data.quote.author
//     })   

// ver.2

let search = document.querySelector("#search")
let submit = document.querySelector("#subBtn")
let quotes = document.querySelector("#quotes")
let page = 1
let prvPage = document.querySelector("#prvBtn")
let nxtPage = document.querySelector("#nxtBtn")

document.getElementById("search").value = ""

function getData() {
    axios({
        method: 'get',
        url: 'https://favqs.com/api/quotes',
        headers: {
            Authorization: 'Token token="1ada7bb20e76745351d38e458d0e57b8"'
        },
        params: {
            page: page,
            filter: search.value
        }
    }).then((response) => {
        quotes.innerHTML = ""
        let quoteArray = response.data
        page = quoteArray.page
        let quoteList = quoteArray.quotes
            for (i = 0; i < quoteList.length; i++)
                quotes.innerHTML += `<h2>${quoteList[i].body}</h2><p>${quoteList[i].author}</p><br>`
    }).catch((error) => {
        console.log(error)
    })
}

submit.onclick = function() {
    getData()
}

nxtPage.onclick = function() {
    page = page + 1
    quotes.innerHTML += ""
    getData()
    window.scrollTo(0, 0)
}

prvPage.onclick = function() {
    if (page === 1) {
        quotes.innerHTML = ""
    }
    else if (page > 1) {
        page = page - 1
        quotes.innerHTML += ""
        getData()
    }
    window.scrollTo(0, 0)
}

document.addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
        event.preventDefault()
        document.getElementById("subBtn").click()
    }
})
