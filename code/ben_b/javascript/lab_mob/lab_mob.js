let todoObject = [
    {
        name: 'Eat',
        completed: false,
        id: 1
    },
    {
        name: 'Sleep',
        completed: true,
        id: 2
    }   
]
let submit = document.querySelector('#submit-btn')
let todoSection = document.querySelector('#todos-section')
let completedSection = document.querySelector('#completed-section')
let tasks = document.querySelector('#tasks')
let idCounter = todoObject.length
submit.onclick = function() {
    idCounter ++
    let obj = {
        name : tasks.value,
        completed : false,
        id : idCounter
    }
    todoObject.push(obj)
    todoSection.innerHTML = ""
    completedSection.innerHTML = ""
    addToDom()
}
function addToDom(){
    let todoSection = document.querySelector('#todos-section')
    todoObject.forEach(tasks => {
        if (tasks.completed === true) {
            completedSection.innerHTML += `<p>${tasks.name}</p> <button onclick="todo(${tasks.id})">todo</button> <button onclick="deleteTodo(${tasks.id})">Remove</button>`
        } else {
        todoSection.innerHTML += `<p>${tasks.name}</p> <button onclick="completeTodo(${tasks.id})">complete</button> <button onclick="deleteTodo(${tasks.id})">Remove</button>`
        }
    }
)}
function completeTodo(id) {
    console.log(`you clicked on complete todo with id ${id}`)
    for (let i = 0; i < todoObject.length; i++)
    {
        if (todoObject[i].id === id)
        {
            completedSection.innerHTML += `<p>${tasks.name}</p> <button onclick="completeTodo(${tasks.id})">ToDo</button>`
            todoObject[i].completed = true
            console.log(todoObject[i])
        }
    }
    todoSection.innerHTML = ""
    completedSection.innerHTML = ""
    addToDom()
}
function todo(id) {
    console.log(`you clicked on complete todo with id ${id}`)
    for (let i = 0; i < todoObject.length; i++)
    {
        if (todoObject[i].id === id)
        {
            todoSection.innerHTML += `<p>${tasks.name}</p> <button onclick="todo(${tasks.id})">completed</button>`
            todoObject[i].completed = false
            console.log(todoObject[i])
        }
    }
    todoSection.innerHTML = ""
    completedSection.innerHTML = ""
    addToDom()
}
function deleteTodo(id) {
    for (let i = 0; i < todoObject.length; i++)
    {
        if (todoObject[i].id === id)
        {
            todoSection.innerHTML += `<p>${tasks.name}</p> <button onclick="todo(${tasks.id})">remove</button>`
            completedSection.innerHTML += `<p>${tasks.name}</p> <button onclick="todo(${tasks.id})">remove</button>`
            console.log(todoObject[i])
            todoObject.splice(i, 1)
        }
    }
    todoSection.innerHTML = ""
    completedSection.innerHTML = ""
    addToDom()
}
addToDom()