let content = document.querySelector("#content");
let userPageSelect = 1;
let userKeyword = "cats";
function getQuote() {
    axios({
        method: "get",
        url: "https://favqs.com/api/quotes",
        params: {
            page: userPageSelect,
            filter: userKeyword,
        },
        headers: {
            Authorization: `Token token="825c7707461345382289059ad7120acb`,
        },
    })
        .then((response) => {
            let dataArray = response.data;
            console.log(dataArray);
            // console.log(dataArray.quote.body);
            // console.log(dataArray[0].author);
            // console.log(dataArray[0].body);
            content.innerHTML = `<p>${dataArray.quote.body}</p>`;
            // content.innerHTML = dataArray[0].body;
        })
        .catch((error) => {
            console.log(error);
        });
}

getQuote();
