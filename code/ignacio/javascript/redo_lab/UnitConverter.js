let distance = document.querySelector('#distance')
let unit = document.querySelector('#unit')
let ConvBtn = document.querySelector('#ConvBtn')
let result = document.querySelector('#result')
let calculator = {
    'in': .0254,
    'yd': .9144,
    'ft': .3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000
}

ConvBtn.onclick = function () {
    let distanceValue = distance.value
    let unitValue = unit.value
    let outcome = calculator[unitValue] * distanceValue
    console.log(outcome)
    result.innerHTML = outcome
}