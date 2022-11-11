let quoteList = document.querySelector("#results")
let page_num = 1
let tag = ""

function getSome(page_id, tag){
    axios({
        method: 'get',
        url: "https://favqs.com/api/quotes/?page=&filter=&type=tag",
        headers: {
            Authorization: 'Token token="f9ae980cb1eb8fe60504dd227a28aec5"'
        },
        params: {
            'page': page_id,
            'filter': tag
        }
        
    }).then((response) => {
        console.log(response.data);
        let results = response.data;
        quoteList.innerHTML = ""
        results.quotes.forEach(quote => {
            console.log(quote)
            quoteList.innerHTML += `<li>"${quote.body}" - ${quote.author}</li><br>`
        });
    })
    document.getElementById("pageNum").innerHTML = `Page ${page_num}`

}

function submitBtn(){
    // console.log(document.getElementById("searchBar").value)
    let tag = document.getElementById("searchBar").value;
    getSome(page_num, tag);
    document.getElementById("searchBar").value = "";
    document.getElementById("filter").innerHTML = `"${tag}"`

}

function nextPage(){
    page_num ++
    getSome(page_num, document.getElementById("filter").innerHTML);
    console.log(page_num)
}

function lastPage(){
    if (page_num === 1) {
        getSome(page_num, document.getElementById("filter").innerHTML);
        console.log(page_num)
    } else {
        page_num -=1
        getSome(page_num, document.getElementById("filter").innerHTML);
        console.log(page_num)
    }
}

document.addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
        event.preventDefault()
        document.getElementById("submit").click()
        
    }
})
