let content = document.getElementById('content')
const token = '162ea77a8f3a4110496838e2faa60e31'
let nextPage = document.querySelector('#next-page')
let prevPage = document.querySelector('#prev-page')
let pageNumber = 1
let allQuotes = document.getElementById('all-quotes')
let input = document.querySelector('#input-filter')

function getQuote() {
    axios({
        method: 'get',
        url: 'https://favqs.com/api/quotes/',
        headers: {
            Authorization: `Token token="${token}"`
        },
        params: {
            page: pageNumber,
            filter: `${input.value}`
        },


    }).then((response) => {
        let quotes = response.data['quotes']
        if (response.data["last_page"] === true) {
            nextPage.disabled = 'disabled'
        }

        if (response.data['page'] === 1) {
            prevPage.disabled = 'disabled'
        }
        else {
            prevPage.disabled = !'disabled'
        }
        // console.log(input)
        allQuotes.remove()
        allQuotes = document.createElement('div')
        content.appendChild(allQuotes)

        for (let i = 0; i < quotes.length; ++i) {
            let p = document.createElement('p')
            p.innerText = quotes[i].body
            allQuotes.appendChild(p)

            let p2 = document.createElement('p')
            p2.innerText = `- ${quotes[i].author}`
            allQuotes.appendChild(p2)
        }


    })
}

nextPage.onclick = function () {

    pageNumber += 1
    getQuote()
}

prevPage.onclick = function () {

    pageNumber -= 1
    getQuote()
}

search.onclick = function () {

    getQuote()
}