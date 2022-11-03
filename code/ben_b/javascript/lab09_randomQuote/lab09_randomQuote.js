let quote = document.querySelector('#quote')
let dataArray = []
let page_id = 1
let filter = ""


function getQuote(){
    quote.innerHTML = ""
    pages.innerHTML = ""
    axios({
        method: 'get',
        url: 'https://favqs.com/api/quotes',
        params: {
            page: page_id,
            filter: "god",
        },
        headers: {
            'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'
        }   
    }).then((response) => {
        console.log(response)
        for (let i = 0; i < 25; i ++)
        {
        quote.innerHTML += `<p>${i + 1}) ${response.data.quotes[i].body} - ${response.data.quotes[i].author}</p><br>`
        }
        pages.innerHTML += `<button onclick="lastPage()">Last Page</button>`
        pages.innerHTML += `<button onclick="nextPage()">Next Page</button>`
    }).catch((error) => {
        console.log(error)
    })
}

function nextPage(){
    quote.innerHTML = ""
    pages.innerHTML = ""
    page_id++
    axios({
        method: 'get',
        url: "https://favqs.com/api/quotes",
        params: {
            page: page_id,
            filter: "god",
        },
        headers: {
            'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'
        }   
    }).then((response) => {
        console.log(response)
        for (let i = 0; i < 25; i ++)
        {
        quote.innerHTML += `<p>${i + 1}) ${response.data.quotes[i].body} - ${response.data.quotes[i].author}</p><br>`
        }
        pages.innerHTML += `<button onclick="lastPage()">Last Page</button>`
        pages.innerHTML += `<button onclick="nextPage()">Next Page</button>`
    }).catch((error) => {
        console.log(error)
    })
}


function lastPage(){
    quote.innerHTML = ""
    pages.innerHTML = ""
    page_id -= 1
    if (page_id === 0 )
    {
        page_id = 1
    }
    axios({
        method: 'get',
        url: "https://favqs.com/api/quotes",
        params: {
            page: page_id,
            filter: "god",
        },
        headers: {
            'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'
        },    
    }).then((response) => {
        console.log(response)
        for (let i = 0; i < 25; i ++)
        {
        quote.innerHTML += `<p>${i + 1}) ${response.data.quotes[i].body} - ${response.data.quotes[i].author}</p><br>`
        }
        pages.innerHTML += `<button onclick="lastPage()">Last Page</button>`
        pages.innerHTML += `<button onclick="nextPage()">Next Page</button>`
    }).catch((error) => {
        console.log(error)
    })
}



getQuote()