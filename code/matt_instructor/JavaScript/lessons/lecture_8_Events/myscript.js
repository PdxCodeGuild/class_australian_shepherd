let btn = document.querySelector('#btn')
// console.log(btn)

btn.onclick = function() {
    console.log('hello')
}

let btn2 = document.querySelector('#btn2')


// addEventListener events
// https://www.w3schools.com/jsref/met_element_addeventlistener.asp
btn2.addEventListener('click', function(){
    console.log(`${btn2.name} was clicked`)
})

let input1 = document.querySelector('#input1')
let displayText = document.querySelector('#displayText')

input1.oninput = function() {
    console.log('You typed: ' + input1.value)
    displayText.innerHTML = input1.value
}

// Fun examples ---------------------------------------

let btn3 = document.querySelector('#btn3')
let bodyApp = document.querySelector('#app')


let colors = ['red', 'blue', 'green', 'teal', 'black']
let counter = 0

btn3.onclick = function() {
    console.log(counter)
    
    bodyApp.style.backgroundColor = colors[counter]
    
    if (colors[counter] === 'black')
    {
        displayText.style.color = 'white'
    }
    else 
    {
        displayText.style.color = 'black'
    }

    if (colors.length - 1 === counter)
    {
        counter = -1
    }
    counter++
    
}