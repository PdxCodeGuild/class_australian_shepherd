let colorInput = document.querySelector('#colorInput')
let colorBtn = document.querySelector('#colorBtn')
let colorDisplay = document.querySelector('#colorDisplay')


let inputValue = ''

colorInput.oninput = function() {
    inputValue =  colorInput.value
}

colorBtn.onclick = function(){
    console.log(inputValue)

    colorDisplay.innerHTML = `I am the color ${inputValue}`
    colorDisplay.style.color = `${inputValue}`
}



const heroes = ['batman', 'superman', 'homelander', 'ww', 'harley']



let heroDisplay = document.querySelector('#heroDisplay')

for (let i = 0; i < heroes.length; i++)
{
    let paragraph = document.createElement("p")
    let node = document.createTextNode(heroes[i])
    paragraph.appendChild(node)
    heroDisplay.appendChild(paragraph) 
}