
let author = document.querySelector('#author')
let quote = document.querySelector('#quote')
const token = 'de1f470fb3234cbec6e5c44636abacaa'
let quoteSearch = document.querySelector('#quoteSearch')
let btn = document.querySelector('#btn')
let pageNumber = 1
let nextPage = document.querySelector('#nextPage')
let lastPage = false

function getQuote(){
    axios({
        method: 'get',
        url: "https://favqs.com/api/quotes/",
        headers: {
            Authorization: `Token token="${token}"`
        },
        params: {
            page: pageNumber,
            filter: `${quoteSearch.value}`
        }
    }).then((response) => {
        console.log(response.data)
        lastPage = response.data.last_page
        for (let i = 0; i < response.data.quotes.length; i++) {
            author.innerHTML += response.data.quotes[i].author + '<br></br>'
            author.innerHTML += response.data.quotes[i].body + '<br></br>'
        }
        checkLastPage()
    })
}

btn.addEventListener('click', function handleClick(event){

    author.innerHTML = ''
    quote.innerHTML = ''
    pageNumber = 1
    getQuote()

})

function checkLastPage(){
    
    if (lastPage) {
        nextPage.style.display = 'none' 
        console.log('it works')     
    } else {
        nextPage.style.display = 'block'
    }
}

nextPage.addEventListener('click', function handleClick(event){
    author.innerHTML = ''
    quote.innerHTML = ''
    if (lastPage) {
        console.log('ok')      
    } else {
        function nextPage() {
            getQuote(pageNumber += 1)
        }
        console.log(pageNumber)
        nextPage()
    }

})

