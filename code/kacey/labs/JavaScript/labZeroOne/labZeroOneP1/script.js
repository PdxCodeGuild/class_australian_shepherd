let numberOne = document.querySelector('#numberOne')
let numberTwo = document.querySelector('#numberTwo')

let timesBtn = document.querySelector('#timesButton')
let divBtn = document.querySelector('#divButton')
let addBtn = document.querySelector('#addButton')
let subBtn = document.querySelector('#subButton')

let calculation = document.querySelector('#calculation')

// console.log(timesButton)

// console.log(numberOne)
calculateInputs = function(mathOperator) {
    let inputValue = parseInt(numberOne.value)
    let inputValueTwo = parseInt(numberTwo.value)

    if (mathOperator === '*')
    {
        calculation.innerHTML = inputValue * inputValueTwo
    } 
    else if (mathOperator === '/')
    {
        calculation.innerHTML = inputValue / inputValueTwo
    }
    else if (mathOperator === '+')
    {
        calculation.innerHTML = inputValue + inputValueTwo
    }
    else
    {
        calculation.innerHTML = inputValue - inputValueTwo
    }
}

timesButton.onclick = function() {
    let inputValue = numberOne.value
    let inputValueTwo = numberTwo.value

    // console.log(inputValue * inputValueTwo)
    calculateInputs(inputValue, inputValueTwo)
}

divButton.onclick = function() {
    let inputValue = numberOne.value
    let inputValueTwo = numberTwo.value

    // console.log(inputValue * inputValueTwo)
    calculation.innerHTML = inputValue / inputValueTwo

}

addButton.onclick = function() {
    let inputValue = numberOne.value
    let inputValueTwo = numberTwo.value

    // console.log(inputValue + inputValueTwo)
    calculation.innerHTML = parseInt(inputValue) + parseInt(inputValueTwo)
}

subButton.onclick = function() {
    let inputValue = numberOne.value
    let inputValueTwo = numberTwo.value

    // console.log(inputValue - inputValueTwo)
    calculation.innerHTML = inputValue - inputValueTwo
}


