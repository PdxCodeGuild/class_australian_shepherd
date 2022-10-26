



const game = ['rock', 'paper', 'scisors']
let choice = Math.floor(Math.random() * (2 - 0) + 0);

let comp = game[choice]
let outcome = ''

console.log('comp: ' + comp)


// let human = nextline('human')






let btn = document.querySelector('#btn')

btn.onclick = function(){
    // console.log('hello')

    let humanNode = document.querySelector('#human')
    let human = humanNode.value
    console.log(human)

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

    let result = document.querySelector('#result')
    result.innerHTML = `${outcome}, computer chose ${comp}`
}


