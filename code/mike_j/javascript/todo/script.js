let todoObject = []

let input = document.querySelector("#inputBox")
let add = document.querySelector("#addBtn")
let todoList = document.querySelector("#todo-list")
let doneList = document.querySelector("#done-list")
let idCounter = todoObject.length

document.getElementById("inputBox").value = ""

add.onclick = function() {
    let inputVal = input.value
    idCounter++
    let task = {
        name: inputVal,
        completed: false,
        id: idCounter
    }
    todoObject.push(task)
    addToDom()
    document.getElementById("inputBox").value = ""
}

function addToDom(){
    todoList.innerHTML = ""
    todoObject.forEach(task => {
        if (task.completed === false) {
            todoList.innerHTML += `<p>${task.name}</p><button onclick="completeTodo(${task.id})">Done</button>`
        }
        else if (task.completed === true)
            doneList.innerHTML += `<p>${task.name}</p><button onclick="deleteTodo(${task.id})">Delete</button>`
        }
    )
}

function completeTodo(id) {
    doneList.innerHTML = ""
    todoObject.forEach(task => {
        if (task.id === id) {
            task.completed = !task.completed
        }
    })
    addToDom()   
}

function deleteTodo(id) {
    doneList.innerHTML = ""
    todoObject.forEach(task => {
        if (task.id === id) {
            todoObject.splice(todoObject.indexOf(id), 1)
        }
    })
    addToDom()
    console.log(todoObject)
}

document.addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
        event.preventDefault()
        document.getElementById("addBtn").click()
    }
})
