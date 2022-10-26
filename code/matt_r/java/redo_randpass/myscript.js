



const game = ['rock', 'paper', 'scisors']
let choice = Math.floor(Math.random() * 3);

let comp = game[choice]

console.log('comp: ' + comp)

// let human = 'rock'
let human = nextline('human')


console.log('human: ' + human)

if (human == 'rock') {
    
    if (comp == 'rock') {
        outcome = 'its a tie'
    } else if (comp == 'scissors') {
        outcome = 'Player wins'
    } else {
        outcome = 'Computer wins'
    }
}

if (human == 'paper') {
    
    if (comp == 'paper') {
        outcome = 'its a tie'
    }
    else if (comp == 'rock') {
        outcome = 'Player wins'
    }
    else {
        outcome = 'Computer wins'
    }
}

if (human == 'scissors'){
    
    if (comp == 'scissors'){
        outcome = 'its a tie'
    }
    else if (comp == 'paper'){
        outcome = 'Player wins'
    }
    else {
        outcome = 'Computer wins'
    }
}

console.log(outcome)



