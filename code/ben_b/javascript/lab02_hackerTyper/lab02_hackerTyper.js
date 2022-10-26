let area = document.querySelector('#area')

let content = 'username: '

document.getElementById("area").addEventListener('mouseover', mouseOver)

function mouseOver(){
    content += "test"
    let text = document.createTextNode(content)
    area.appendChild(text)
}


setInterval(function () {document.getElementById("area").innerHTML += "Hello"}, 10000);

// setInterval(displaySomething, 1000)

// setInterval(displayAlert, 100)



function displayAlert(){
    alert("ERROR");
}

// function displaySomething(){
//     document.getElementById("area").innerHTML += "Something ";
// }


