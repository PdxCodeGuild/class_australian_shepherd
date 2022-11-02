let quote = document.querySelector('#quote')
let author = document.querySelector('#author')

let dataArray = []


function getQuote(){
    axios({
        method: 'get',
        url: 'https://favqs.com/api/quotes',
        headers: {
            'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'
        }   
    }).then((response) => {
        console.log(response)
        for (let i = 0; i < 25; i ++)
        {
        quote.innerHTML = response.data.quotes[i].body
        author.innerHTML = response.data.quotes[i].author
        }
    }).catch((error) => {
        console.log(error)
    })
}

getQuote()