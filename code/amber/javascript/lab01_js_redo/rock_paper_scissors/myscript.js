// ROCK PAPER SCISSORS

let selects = ['rock', 'paper', 'scissors']

let selectsLength = selects.length
// console.log(selectsLength)

let btn = document.querySelector('#btn')

let winner = 'Try again.'


btn.onclick = function() {
  let userSelection = document.querySelector('input[name="selection"]:checked').value
  console.log('User selection: ' + userSelection)

  let compSelection = selects[Math.floor(Math.random()* selectsLength)]
  console.log('Comp selection: ' + compSelection)

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
  let pTag = document.querySelector('#pTag')

  pTag.innerHTML = `You selected ${userSelection}. The computer selected ${compSelection}. ${winner}`

  // change button to 'play again'
  playAgain = btn.setAttribute("value", "Play Again")
}


// how do i make it so that pTag prints "please select one to play" or whatever so they have to choose one
