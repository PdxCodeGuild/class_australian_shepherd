// Setting innerText and innerHTML

// innerText returns all text contained by an element and all its child elements.
// innerHtml returns all text, including html tags, that is contained by an element.


let div1 = document.querySelector('#div1')
div1.innerText = 'Hello World!'

let div2 = document.querySelector('#div2')
div2.innerHTML = "<p><b>Hello WOrld!</b></p>"

let demo_div = document.querySelector('#demo_div')
demo_div.innerHTML = 'Hello World'
demo_div.style.fontSize = '24px'


// For more examples such as
// Input Fields
// Radio Buttons and Checkboxes
// Dropdown Lists
// Creating and Adding Elements

// see the following github repo in our class
// https://github.com/PdxCodeGuild/class_australian_shepherd/blob/main/Upcoming%20Topics/4%20JavaScript/docs/11%20-%20Editing%20HTML.md