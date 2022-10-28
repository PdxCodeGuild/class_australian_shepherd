let animal = document.querySelector('#animal')
let displayAnimal = document.querySelector('#span_animal')
let country = document.querySelector('#country')
let displayCountry = document.querySelector('#span_country')
let number = document.querySelector('#number')
let displayNumber = document.querySelector('#span_number')
let vehicle = document.querySelector('#vehicle')
let displayVehicle = document.querySelector('#span_vehicle')
let names = document.querySelector('#name')
let displayNames = document.querySelector('#span_name')
let sport = document.querySelector('#sport')
let displaySport = document.querySelector('#span_sport')
let movie = document.querySelector('#movie')
let displayMovie = document.querySelector('#span_movie')
let measure = document.querySelector('#measure')
let displayMeasure = document.querySelector('#span_measure')
let spans = document.getElementsByTagName('span')
for (let i = 0; i < spans.length; i++){
    spans[i].style.color = 'red'
}

let btn = document.querySelector('#btn')
btn.onclick = function(){
    displayMeasure.innerHTML = measure.value
    // displayMeasure.style.color = 'red'
    displayMovie.innerHTML = movie.value
    // displayMovie.style.color = 'red'
    displaySport.innerHTML = sport.value
    // displaySport.style.color = 'red'
    displayNames.innerHTML = names.value
    // displayNames.style.color = 'red'
    displayVehicle.innerHTML = vehicle.value
    // displayVehicle.style.color = 'red'
    displayNumber.innerHTML = number.value
    // displayNumber.style.color = 'red'
    displayCountry.innerHTML = country.value
    // displayCountry.style.color = 'red'
    displayAnimal.innerHTML = animal.value
    // displayAnimal.style.color = 'red'
}

 // let displayText = document.querySelector('#displayText')
// input.oninput = function() {
//     console.log('you typed' + input.value)
//     displayText.innerHTML = input.value