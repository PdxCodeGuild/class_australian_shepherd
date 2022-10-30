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

let submit = document.querySelector('#addBtn')
let todoList = document.querySelector('#todo-list')
let doneList = document.querySelector('#done-list')

submit.onclick = function() {
    
}

function addToDom(){
    let todoList = document.querySelector('#todo-list')

    todoObject.forEach(task => {
        todoList.innerHTML += `<p>${task.name}</p> <button onclick="completeTodo(${task.id})">Done</button>`
    }
)}

function completeTodo(id) {
    console.log(`you clicked on complete todo with id ${id}`)
}

function deleteTodo(id) {

}

addToDom()
