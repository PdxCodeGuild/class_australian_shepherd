// Let's write a python program to give basic blackjack playing advice during a game by asking the player for cards using a Dictionary. 
// First, ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). Then, figure out the point value of each card individually. 
// Number cards are worth their number, all face cards are worth 10. At this point, assume aces are worth 1. Use the following rules to determine the advice:

// Less than 17, advise to "Hit"
// Greater than or equal to 17, but less than 21, advise to "Stay"
// Exactly 21, advise "Blackjack!"
// Over 21, advise "Already Busted"

const cardValues = {
    'A': 11,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
}

const cardList = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
document.getElementById("hitButton").style.display = "none"
document.getElementById("stayButton").style.display = "none"
document.getElementById("refresh").style.display = "none"
let userCards = []
let dealerCards = []

function advice(count, dealerCount) {
    if (count <= 11) {
        return 'HIT'
    }
    else if (count <= 16 && dealerCount <=6) {
        return 'STAY'
    } 
    else if (count <= 16 && dealerCount > 6) {
        return 'HIT'
    }
    else {
        return 'STAY'
    }
}

let sum = 0
let dealerSum = 0
function dealCards() {
    while (userCards.length < 2) {
        userCards.push(cardList[(Math.floor(Math.random() * 13))]);
        console.log(userCards);
        dealerCards.push(cardList[(Math.floor(Math.random() * 13))]);
        console.log(dealerCards);
    }
    sum += (cardValues[userCards[0]] + cardValues[userCards[1]])
    dealerSum += (cardValues[dealerCards[0]])
    console.log(sum)
    document.getElementById("dealButton").style.display = "none"
    document.getElementById("hitButton").style.display = "block"
    document.getElementById("stayButton").style.display = "block"
    document.getElementById("yourCards").innerHTML = `You have ${userCards[0]} and ${userCards[1]}. For a count of: ${sum}`
    document.getElementById("faceCard").innerHTML = `Dealer is showing ${dealerCards[0]}.`
    document.getElementById("advice").innerHTML = `You should: ${advice(sum, dealerSum)}.`
}


function userHit() {
    userCards.push(cardList[(Math.floor(Math.random() * 13))]);
    sum += (cardValues[userCards.slice(-1)[0]])
    if (sum > 21) {
        document.getElementById("userCount").innerHTML = `You have: ${userCards.join()}. For a count of ${sum}. BUST!`
        document.getElementById("refresh").style.display = "block"
    }
    else {
        console.log(cardValues[userCards[-1]])
        document.getElementById("userCount").innerHTML = `You have: ${userCards.join()}. For a count of ${sum}.`
    }
}

function userStay() {
    dealerSum += cardValues[dealerCards[1]]
    document.getElementById("userCount").innerHTML = `You have: ${userCards.join()}. For a count of ${sum}.`
    document.getElementById("dealerCount").innerHTML = `Dealer had: ${dealerCards.join()}. For a count of ${dealerSum}.`    
    document.getElementById("refresh").style.display = "block"    
    
    while (dealerSum < 17 ) {
        dealerCards.push(cardList[(Math.floor(Math.random() * 13))]);
        dealerSum += (cardValues[dealerCards.slice(-1)[0]])
    }

    document.getElementById("dealerNextCount").innerHTML = `Dealer now has: ${dealerCards.join()}. For a count of ${dealerSum}.`
    
    if (dealerSum >=17) {
        if (dealerSum === sum ) {
            document.getElementById("result").innerHTML = "Push!"
        }
        else if (sum > 21) {
            document.getElementById("result").innerHTML = "Bust!"
        }
        else if ((dealerSum >= 17 && dealerSum < 22) && (sum < dealerSum))  {
            document.getElementById("result").innerHTML = "You lost!"
        }
        else if (sum >= 17 && dealerSum > 21) {
            document.getElementById("result").innerHTML = "You won!"
        } 
        else {
            document.getElementById("result").innerHTML = "You won!"
        }
        }
    }





