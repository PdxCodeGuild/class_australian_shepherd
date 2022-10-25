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
]
let randomNumber = ''
let currentWord = ''
let newWord = function(){
    randomNumber = Math.floor(Math.random() * words.length) + 0 
    currentWord = words[randomNumber]
}
newWord()

console.log(currentWord)
let guess = document.querySelector('#guess')
let submit = document.querySelector('#submit')

let counter = 0



submit.onclick = function(){
    if (currentWord.includes(guess.value))
    {
        for (let i = 0; i < currentWord.length; i++)
        {
            if (currentWord[i] === guess.value) revealWord(i)
        }
    }
    else{
        counter++
        document.querySelector('#score').innerHTML = counter
        gameOver()
    }
}

let revealWord = function(index){
    if (index === 0)
    {
        document.querySelector('#letter0').innerHTML = guess.value
    }
    else if (index === 1)
    {
        document.querySelector('#letter1').innerHTML = guess.value
    }
    else if (index === 2)
    {
        document.querySelector('#letter2').innerHTML = guess.value
    }
    else if (index === 3)
    {
        document.querySelector('#letter3').innerHTML = guess.value
    }
    else{
        document.querySelector('#letter4').innerHTML = guess.value
    }
}



let gameOver = function() {
    if (counter === 7)
    {
        document.querySelector('#gameOverScreen').style.display = 'flex'
        document.querySelector('#answer').innerHTML = currentWord
    }
}

let playBtn = document.querySelector('#playBtn')

playBtn.onclick = function() {
    document.querySelector('#gameOverScreen').style.display = 'none'
    counter = 0
    document.querySelector('#score').innerHTML = counter
    newWord()
    document.querySelector('#letter0').innerHTML = '_'
    document.querySelector('#letter1').innerHTML = '_'
    document.querySelector('#letter2').innerHTML = '_'
    document.querySelector('#letter3').innerHTML = '_'
    document.querySelector('#letter4').innerHTML = '_'
    document.querySelector('#answer').innerHTML = ''
}


guess.oninput = function() {
    if (this.value.length > 1)
    {
        let replaceChar = this.value[1]
        guess.value = replaceChar
    }
}