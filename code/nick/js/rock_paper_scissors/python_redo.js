// Lab Rock Paper Scissors
// Let's play rock-paper-scissors with the computer. You may want to try using these emojis 🗿📃✂️✊✋✌

// The computer will ask the user for their choice (rock, paper, scissors)
// The computer will randomly choose rock, paper or scissors
// Determine who won and tell the user

// Version 2 (optional)
// After playing, ask them if they'd like to play again. If they say yes, restart the game, otherwise exit.

const weaknesses = {
    rock: 'paper',
    paper: 'scissors', 
    scissors: 'rock'
};

// Pull random number to get random element
function cpu_choice(list) {
    return list[Math.floor(Math.random()*elements.length)];
}
let elements = document.getElementsByClassName("images")

// results function
function rockPaperScissors(user_select, cpu_select, weakness) {
    if (weakness[user_select] === cpu_select) 
        {
            // console.log(weakness[user_select])
            return('loser')
        }
    
    else if (user_select === cpu_select)
        {
            return('tie')
        }
    
    else 
        {
            return('winner')
        }
}

// image onclick actions -- couldn't figure out how to consolidate for each id type
document.getElementById("rockImage").onclick = function userChoice() {
    let choice = (document.getElementById("rockImage").getAttribute("value"))
    userSelection.innerText = `You selected ${choice}.`  
    let elements = document.getElementsByClassName("images")
    // console.log(cpu_choice(elements).getAttribute("value"))
    let cpu_selection = cpu_choice(elements).getAttribute("value")
    cpuSelection.innerText = `CPU selected ${cpu_selection}.`
    // console.log(rockPaperScissors(choice, cpu_selection, weaknesses))
    let result = rockPaperScissors(choice, cpu_selection, weaknesses)
    outcomeResult.innerText = `Result: ${result}`
}

document.getElementById("paperImage").onclick = function userChoice() {
    let choice = (document.getElementById("paperImage").getAttribute("value"))
    userSelection.innerText = `You selected ${choice}.`
    let elements = document.getElementsByClassName("images")
    // console.log(cpu_choice(elements).getAttribute("value"))
    let cpu_selection = cpu_choice(elements).getAttribute("value")
    cpuSelection.innerText = `CPU selected ${cpu_selection}.`
    // console.log(rockPaperScissors(choice, cpu_selection, weaknesses))
    let result = rockPaperScissors(choice, cpu_selection, weaknesses)
    outcomeResult.innerText = `Result: ${result}`
}   

document.getElementById("scissorsImage").onclick = function userChoice() {
    let choice = (document.getElementById("scissorsImage").getAttribute("value"))
    userSelection.innerText = `You selected ${choice}.`
    let elements = document.getElementsByClassName("images")
    // console.log(cpu_choice(elements).getAttribute("value"))
    let cpu_selection = cpu_choice(elements).getAttribute("value")
    cpuSelection.innerText = `CPU selected ${cpu_selection}.`
    // console.log(rockPaperScissors(choice, cpu_selection, weaknesses))
    let result = rockPaperScissors(choice, cpu_selection, weaknesses)
    outcomeResult.innerText = `Result: ${result}`
}