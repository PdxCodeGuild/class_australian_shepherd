const winningStates = {
    Rock : "Scissors",
    Paper : "Rock",
    Scissors : "Paper",
}

let rockBtn = document.querySelector('#rockBtn')
let paperBtn = document.querySelector('#paperBtn')
let scissorsBtn = document.querySelector('#scissorsBtn')

let computerSelection = function(){
    return Object.keys(winningStates)[Math.floor(Math.random() * 3)]
}

let compare = function(computer, user) {
   if (computer === user) {
    resultText.innerHTML = `Both Opponents picked ${user}, Tie!`
   }
   else if (winningStates[computer] === user) {
    resultText.innerHTML = `Computer's ${computer} Defeats User's ${user}!`
   }
   else if (winningStates[computer] !== user) {
    resultText.innerHTML = `User's ${user} Defeats Computer's ${computer}!`
   }
}

rockBtn.onclick = function() {
    compare(computerSelection(), "Rock")
    }

paperBtn.onclick = function() {
    compare(computerSelection(), "Paper")
}

scissorsBtn.onclick = function() {
    compare(computerSelection(), "Scissors")
}
