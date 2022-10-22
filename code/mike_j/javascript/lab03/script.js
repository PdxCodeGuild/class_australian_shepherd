let first = document.querySelector("#first")
let second = document.querySelector("#second")
let third = document.querySelector("#third")
let result = document.querySelector("#result")

const card_value = {
    "A" : 1,
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "10" : 10,
    "J" : 10,
    "Q" : 10,
    "K" : 10
}

function calc() {
    let total = (card_value[first.value]) + (card_value[second.value]) + (card_value[third.value])
 
    if (total == 21)
        result.innerHTML = (total + " >>> " + "Blackjack!")    
    else if (total > 21)
        result.innerHTML = (total + " >>> " + "Busted!")
    else if (total < 17)
        result.innerHTML = (total + " >>> " + "Hit")
    else if (total > 17 || total == 17)
        result.innerHTML = (total + " >>> " + "Stay") 
}    

function reset() {
    document.getElementById('first').value = ""
    document.getElementById('second').value = ""
    document.getElementById('third').value = ""
    result.innerHTML = ""
}
