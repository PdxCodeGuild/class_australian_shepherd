let num1 = document.querySelector('#number1')
let num2 = document.querySelector('#number2')

let multBtn = document.querySelector('#multBtn')
let divBtn = document.querySelector('#divBtn')
let addBtn = document.querySelector('#addBtn')
let subBtn = document.querySelector('#subBtn')

let result = document.querySelector('#result')

multBtn.onclick = function() {
    let num1Value = num1.value
    let num2Value = num2.value

    result.innerHTML = num1Value * num2Value
}

divBtn.onclick = function() {
    let num1Value = num1.value
    let num2Value = num2.value

    result.innerHTML = num1Value / num2Value
}

addBtn.onclick = function() {
    let num1Value = num1.value
    let num2Value = num2.value

    result.innerHTML = parseInt(num1Value) + parseInt(num2Value)
}

subBtn.onclick = function() {
    let num1Value = num1.value
    let num2Value = num2.value

    result.innerHTML = num1Value - num2Value
}


