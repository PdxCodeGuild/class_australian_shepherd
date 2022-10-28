let area = document.querySelector('#area')

let content = ['inject', '<span class="error">error</span>', 'redirect', 'node', 'package', 'init', 'allocate', 'parse', 'session', 'packet', 'conf', '</br>', 'sudo', 'admin', '$', '#', '*', '{', '^', '@', '!', '(', '/', '?', '<', '>', '}', ')']

let data = ''

document.body.addEventListener('keypress', (event) => {
    console.log(event)
    console.log(`You pressed the key: ${event.key}`)

    data += content[Math.floor(Math.random()*content.length)] + " "
    area.innerHTML = data
})