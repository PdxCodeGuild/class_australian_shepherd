let todoObject = [
    {
        name: "Eat",
        completed: false,
        id: 1
    },
    {
        name: "Sleep",
        completed: true,
        id: 2
    }   
]

let input = document.querySelector("#input")
let add = document.querySelector("#addBtn")
let todoList = document.querySelector("#todo-list")
let doneList = document.querySelector("#done-list")

add.onclick = function() {
    todoObject.push(input.value)
    addToDom()
}

function addToDom(){
    let todoList = document.querySelector("#todo-list")

    todoObject.forEach(task => {
        todoList.innerHTML += `<p>${task.name}</p> <button onclick="completeTodo(${task.id})">Done</button>`
    }
)}

function completeTodo(id) {
    
}

function deleteTodo(id) {

}

document.addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
        event.preventDefault()
        document.getElementById("addBtn").click()
    }
})