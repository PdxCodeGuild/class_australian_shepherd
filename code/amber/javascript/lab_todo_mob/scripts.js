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
submit.onclick = function() {
  console.log('you clicked the submit button, this is supposed to be for adding a new item')
}
function addToDom(){
  let todoSection = document.querySelector('#todos-section')
  todoObject.forEach(task => {
      todoSection.innerHTML += `<p>${task.name}</p> <button onclick="completeTodo(${task.id})">complete</button>`
  }
)}
function completeTodo(id) {
  console.log(`you clicked on complete todo with id ${id}`)
}
function deleteTodo(id) {
}
// initializes the first todos
addToDom()
