// ROCK PAPER SCISSORS

let selects = ['rock', 'paper', 'scissors']

let selectsLength = selects.length
// console.log(selectsLength)

let btn = document.querySelector('#btn')

let pTag1 = document.querySelector('#pTag1')
let pTag2 = document.querySelector('#pTag2')
let pTag3 = document.querySelector('#pTag3')

let winner = ''

btn.onclick = function() {
  let userSelection = document.querySelector('input[name="selection"]:checked').value
// console.log('User selection: ' + userSelection)

  let compSelection = selects[Math.floor(Math.random()* selectsLength)]
  // console.log('Comp selection: ' + compSelection)

  // compare values to see who won
  if (userSelection === 'rock' && compSelection === 'scissors') {
    winner = 'YOU WIN!'
  }
  else if (userSelection === 'paper' && compSelection === 'rock') {
    winner = 'YOU WIN!'
  }
  else if (userSelection === 'scissors' && compSelection === 'paper') {
    winner = 'YOU WIN!'
  }
  else if (userSelection === compSelection) {
    winner = 'Its a tie!'
  }
  else {
    winner = 'The computer wins.'
  }

  // tell user who won
  pTag1.innerHTML = `You selected ${userSelection}.`
  pTag2.innerHTML = `The computer selected ${compSelection}.`
  pTag3.innerHTML = `${winner}`

  // change button to 'play again'
  playAgain = btn.setAttribute("value", "Play Again")
}


// how do i make it so that pTag prints "please select one to play" or whatever so they have to choose one without preloading a check

// how do i style variables within the ptag prints? like make the selections a color or putting the winner in bold?
