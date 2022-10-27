let code = document.querySelector('#code')

let content = ['hacker', 'firewall', ]
// make list of 5 words,use for now and work my way up to a longer list of words (use word counter lab as refrence)
// use matts example to do the lab instead of labs suggestion
document.body.addEventListener('keypress', (event) => {
    console.log(event)
    console.log(`You pressed the key: ${event.key}`)

    content += ' mr_socks '
    
    let text = document.createTextNode(content)
    area.appendChild(text)
})