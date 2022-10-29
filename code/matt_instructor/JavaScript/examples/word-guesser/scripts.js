let app = document.querySelector('#app')
let attemptsDom = document.querySelector('#attempts')

// in a real program should be provided by an api or a comprehensive document. potentially with words that are different length too
const words = [
    'which',
    'there',
    'their',
    'about',
    'would',
    'these',
    'other',
    'words',
    'could',
    'write',
    'first',
    'water',
    'after',
    'where',
    'olive'
]

let randomIndex = 0
let currentWord = ''
let missedWords = ''
let attemptsLeft = 7
let matchCounter = 0

let newWord = function() {
    randomIndex = Math.floor(Math.random() * (words.length - 0) + 0)
    currentWord = words[randomIndex]
    // console.log(currentWord)
}
newWord()
// console.log(currentWord)

let gameOverCheck = function() {
    if (attemptsLeft === 0){
        document.querySelector('#messageArea').innerHTML = `You lost: ${currentWord} `
        newWord()
        resetGame()
    }
}

let winningCheck = function() {
    if (matchCounter === currentWord.length)
    {
        document.querySelector('#messageArea').innerHTML = `You Win!  ${currentWord}`
        newWord()
        resetGame()
    }
}

let resetGame = function() {
    matchCounter = 0
    document.querySelector('#index0').innerHTML = '__'
    document.querySelector('#index1').innerHTML = '__'
    document.querySelector('#index2').innerHTML = '__'
    document.querySelector('#index3').innerHTML = '__'
    document.querySelector('#index4').innerHTML = '__'
    
    attemptsLeft = 7
    attemptsDom.innerHTML = attemptsLeft
    document.querySelector('#missedWords').innerHTML = ''
}



document.addEventListener('keypress', (event) => {
    let pressedKey = event.key

    if (currentWord.includes(pressedKey)){
        for (let i = 0; i < currentWord.length; i++){
            if (currentWord[i] === pressedKey){
                matchCounter++
                let domId = '#index' + i
                document.querySelector(domId).innerHTML = pressedKey
            }
        }
        winningCheck()
    }
    else 
    {
        missedWords += ' ' + pressedKey
        document.querySelector('#missedWords').innerHTML = missedWords
        document.querySelector('#missedWords').style.color = 'red'

        attemptsLeft -= 1
        attemptsDom.innerHTML = attemptsLeft
        gameOverCheck()
    }
})