let content = document.querySelector("#content");
let keywordInput = document.querySelector("#keywordInput");
let nextPageBtn = document.querySelector("#nextPageBtn");
let backPageBtn = document.querySelector("#backPageBtn");

// let userKeyword = keywordInput;
let userPageSelect = 1;

const tester = (inputButton.onclick = function () {
    userPageSelect = 1;
    getQuote();
});

function getQuote() {
    axios({
        method: "get",
        url: "https://favqs.com/api/quotes",
        params: {
            page: userPageSelect,
            filter: keywordInput.value,
        },
        headers: {
            Authorization: `Token token="825c7707461345382289059ad7120acb`,
        },
    })
        .then((response) => {
            let dataArray = response.data;
            // console.log("here is dataArray ", dataArray);
            // console.log("here is dataArray.quotes ", dataArray.quotes);
            // console.log(
            //     "here is dataArray.quotes[0] ",
            //     dataArray.quotes[0]["body"]
            // );
            // console.log(dataArray.quotes);
            let quotesPage = dataArray.quotes;
            console.log("quotesPage ", quotesPage);
            content.innerHTML = "";

            quotesPage.forEach((data) => {
                content.innerHTML += `<p>${data.body}</p>`;
                if (content.innerHTML === "<p>No quotes found</p>") {
                    content.innerHTML =
                        "Try Searching Keyword to Display Quotes";
                }
            });
            if (dataArray.page == "1") {
                backPageBtn.disabled = true;
            } else {
                backPageBtn.disabled = false;
            }
            if (
                dataArray.last_page === true ||
                dataArray.quotes[0]["body"] === "No quotes found"
            ) {
                nextPageBtn.disabled = true;
            } else {
                nextPageBtn.disabled = false;
            }
            // console.log("last page ", dataArray.last_page);

            // console.log(dataArray[0].author);
            // console.log(dataArray[0].body);
            // content.innerHTML = dataArray[0].body;
        })
        .catch((error) => {
            console.log(error);
        });
}

nextPageBtn.onclick = function () {
    userPageSelect += 1;
    getQuote();
    window.scrollTo(0, 0);
};

backPageBtn.onclick = function () {
    userPageSelect -= 1;
    getQuote();
    window.scrollTo(0, 0);
};
getQuote();

// document.querySelector('#keywordInput').addEventListener('keypress', function(){
//     if
// })

// document.body.addEventListener("keypress", function (event) {
//     // if (event.charCode === 13) {
//     //     console.log("TEST");
//     // }
//     console.log(event);
//     console.log(`You pressed the key: ${event.key}`);
// });

document.body.addEventListener("keydown", function (test) {
    // console.log("test", test);
    // console.log("test.code", test.code);
    if (test.code === "Enter") {
        tester();
    }
    if (test.code === "ArrowRight") {
        userPageSelect += 1;
        getQuote();
        window.scrollTo(0, 0);
    }
    if (test.code === "ArrowLeft") {
        userPageSelect -= 1;
        getQuote();
        window.scrollTo(0, 0);
    }
});
