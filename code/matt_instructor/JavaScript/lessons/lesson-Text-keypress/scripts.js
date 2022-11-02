let area = document.querySelector('#area')

let content = 'username: '

document.body.addEventListener('keypress', (event) => {
    console.log(event)
    console.log(`You pressed the key: ${event.key}`)

    content += ' mr_socks '
    
    let text = document.createTextNode(content)
    area.appendChild(text)
})

