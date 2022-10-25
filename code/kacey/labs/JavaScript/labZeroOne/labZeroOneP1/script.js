const charList = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "{", "]", "}", "|", ";", ":", "'", ",", ".", "/", "?", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

let generatorBtn = document.querySelector("#generatorBtn")

generatorBtn.onclick = function() {
    let randomPassword = ""
    // console.log("hi")
    while (randomPassword.length < 20) {
        // console.log(randomPassword.length)
        randomPassword = randomPassword + charList[Math.floor(Math.random() * charList.length)]
    }

    resultText.innerHTML = `${randomPassword}`
    console.log(randomPassword)
}


