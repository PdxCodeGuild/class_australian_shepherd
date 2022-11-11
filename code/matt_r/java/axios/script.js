

let content = document.querySelector('#content')
let search = document.querySelector('#search')
let searchBtn = document.querySelector('#searchBtn')
let pageNum = document.querySelector('#pageNum')
let pageVar = 1
let htmlString = ''

function getData(){
    axios({
        method:'get',
        url:'https://favqs.com/api/quotes',
        params: {
            page: pageVar,
            filter: search.value ,
        },
        headers:{ Authorization: 'Token token="eed6951b3a9e15dd239957782e4134b7"'}

     }).then((response) => {
        console.log(pageVar)
        htmlString=''
        content1.innerHTML=''

        let dataArray = response.data.quotes
        console.log(response.data)
        console.log(dataArray)
        console.log(dataArray[0].author)
        console.log(dataArray[0].body)
        console.log(dataArray[0].id)
        // content1.innerHTML = dataArray[0].author
        // content2.innerHTML = dataArray[0].body
        // content3.innerHTML = dataArray[0].id
        // pageNum.innerHTML = response

        for (let i=0; i < dataArray.length; i++){
            htmlString +=`<p>${dataArray[i].body}</p>`
            
        }
        content1.innerHTML = htmlString

     }).catch((error) => {
        console.log(error)
     })
}

searchBtn.onclick = function(){
    
    getData()
  
}

pageNum.onclick = function(){
    pageVar++
    
    getData()
}