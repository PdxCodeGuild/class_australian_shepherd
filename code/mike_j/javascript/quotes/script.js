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

document.getElementById("search").value = ""

submit.onclick = function() {
    axios({
        method: 'get',
        url: 'https://favqs.com/api/quotes',
        headers: {
            Authorization: 'Token token="1ada7bb20e76745351d38e458d0e57b8"'
        },
        params: {
            filter: search.value
        }
    }).then((response) => {
        quotes.innerHTML = ""
        let quoteList = response.data.quotes
            for (i = 0; i < quoteList.length; i++)
                quotes.innerHTML += `<h2>${quoteList[i].body}</h2><p>${quoteList[i].author}</p><br>`
    }).catch((error) => {
        console.log(error)
    })
    document.getElementById("search").value = ""
}

document.addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
        event.preventDefault()
        document.getElementById("subBtn").click()
    }
})
