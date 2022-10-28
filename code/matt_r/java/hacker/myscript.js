let area= document.querySelector('#area')

const textArray = [
    'hello ', 
    "You've been hacked!",
    '<span class="test"> andfhg a </span>',
    '<span class="center"> hello </span>',
]


let content = ''
let counter = 1

// document.body.addEventListener('keypress', (event) => {
//     console.log(event)

//     content=''
    
//     for (let i=0; i < counter; i++){
        
//         content += textArray[i]
//     }

//     counter += 1
    
//     area.innerHTML=''
//     area.innerHTML= content
    
// })


document.body.addEventListener('keypress', (event) => {
    console.log(event)

    content=''
    
    for (let i=0; i < counter; i++){
        
        content += textArray[i]
    }

    counter += 1
    
    area.innerHTML=''
    area.innerHTML= content
    
})