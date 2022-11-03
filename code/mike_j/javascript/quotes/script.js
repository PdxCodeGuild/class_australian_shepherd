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
let quote = document.querySelector("#quote")
let author = document.querySelector("#author")

document.getElementById("search").value = ""

submit.onclick = function() {
    axios({
        method: 'get',
        url: 'https://favqs.com/api/quotes',
        headers: {
            'Authorization': 'Token token="1ada7bb20e76745351d38e458d0e57b8"'
        },
        params: {
            filter: search.value
        }
    }).then((response) => {
        quote.innerHTML = response.data.quotes[0].body
        author.innerHTML = response.data.quotes[0].author
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
