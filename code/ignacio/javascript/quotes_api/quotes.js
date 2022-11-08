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
        },
    
    
    }).then((response) => {
        let quotes = response.data['quotes']
        for (let i=0; i<quotes.length; ++i) {
            let p = document.createElement('p')
            p.innerText = quotes[i].body
            content.appendChild(p)

            let p2 = document.createElement('p')
            p2.innerText = `- ${quotes[i].author}`
            content.appendChild(p2)
            // console.log(response)
        }


    })
}

nextPage.onclick = function (){
    pageNumber += 1
    getQuote()

    // if (response.data["last_page"] === false)
    // {
     
    // }
}



getQuote()