const winningStates = {
    rock : "scissors",
    paper : "rock",
    scissors : "paper",
    
}

let rockBtn = document.querySelector('#rockBtn')
let paperBtn = document.querySelector('#paperBtn')
let scissorsBtn = document.querySelector('#scissorsBtn')


let computerSelection = function(){
    return Object.keys(winningStates)[Math.floor(Math.random() * 3)]
}






let compare = function(computer, user) {
   console.log(computer)
   console.log(user)
   if (computer === user) {
    resultText.innerHTML = "Tie"
   }
   if (computer === "rock") {
    resultText.innerHTML = "computers answer is rock"
   }
   if (computer === "paper") {
    resultText.innerHTML = "computers answer is paper"
   }
   if (computer === "scissors") {
    resultText.innerHTML = "computers answer is scissors"
   }
}
// document.querySelector  ????


rockBtn.onclick = function() {
    compare(computerSelection(), "rock")
    }

paperBtn.onclick = function() {
    compare(computerSelection(), "paper")
}

scissorsBtn.onclick = function() {
    compare(computerSelection(), "scissors")
}
// paperBtn.onclick = function() {
//     let rockBtn = rockBtn.value
//     let paperBtn = paperBtn.value
//     let scissorsBtn = scissorsBtn.value
// }

// scissorsBtn.onclick = function() {
//     let rockBtn = rockBtn.value
//     let paperBtn = paperBtn.value
//     let scissorsBtn = scissorsBtn.value
// }


