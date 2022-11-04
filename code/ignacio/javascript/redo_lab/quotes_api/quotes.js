let content = document.querySelector('#content')
let author = document.querySelector('#author')
const token = '162ea77a8f3a4110496838e2faa60e31'
let nextPage = document.querySelector('#nextPage')
let pageNumber = 1

function getQuote() {
    axios({
        method: 'get',
        url: 'https://favqs.com/api/quotes/',
        headers: {
            Authorization: `Token token="${token}"`
        },
        params: {
            page: pageNumber
        }

    }).then((response) => {
        let quoteBody = response.data['quotes'][0].body
        let quoteAuthor = response.data['quotes'][0].author
        // console.log(response.data['quotes'])
        content.innerHTML = quoteBody
        author.innerHTML = quoteAuthor


    })
}
getQuote()