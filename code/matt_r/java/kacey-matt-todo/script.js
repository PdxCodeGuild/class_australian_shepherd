let todoObject = [
    {
        name: "Eat",
        completed: false,
        id: 1,
    },
    {
        name: "Sleep",
        completed: true,
        id: 2,
    },
];
let submit = document.querySelector("#submit-btn");
let todoSection = document.querySelector("#todos-section");
let completedSection = document.querySelector("#completed-section");
submit.onclick = function () {
    let todoInput = document.querySelector("#todo-input").value;
    let newTodo = {
        name: `${todoInput}`,
        completed: false,
        id: todoObject.length + 1,
    };
    todoObject.push(newTodo);
    console.log(todoObject[0].completed);
    addToDom();
};
function addToDom() {
    let todoSection = document.querySelector("#todos-section");
    todoSection.innerHTML = "";
    completedSection.innerHTML = "";
    todoObject.forEach((task) => {
        if (task.completed === false) {
            todoSection.innerHTML += `<button class="todostyle" onclick="completeTodo(${task.id})">${task.name}</button><p class="todostyle"><button onclick="deleteTodo(${task.id})">Delete</button></p>`;
        }
        let completedSection = document.querySelector("#completed-section");
        if (task.completed === true) {
            completedSection.innerHTML += `<button class="todostyle" onclick="undoComplete(${task.id})">${task.name}</button><p class="todostyle"><button onclick="deleteTodo(${task.id})">Delete</button></p>`;
        }
    });
}
function completeTodo(id) {
    todoObject.forEach((task) => {
        if (task.id === id) task.completed = true;
    });
    addToDom();
}
function undoComplete(id) {
    todoObject.forEach((task) => {
        if (task.id === id) task.completed = false;
    });
    addToDom();
}
function deleteTodo(id) {
    todoObject.forEach((task) => {
        if (task.id === id) todoObject.pop(task);
    });
    addToDom();
}
// initializes the first todos
addToDom();