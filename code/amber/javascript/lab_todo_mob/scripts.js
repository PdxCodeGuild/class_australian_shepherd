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
  },
]
let submit = document.querySelector('#submit-btn')
let todoSection = document.querySelector('#todos-section')
let completedSection = document.querySelector('#completed-section')
let inputItem = document.querySelector('#input')
let idCounter = todoObject.length
// let removeTodo = document
submit.onclick = function () {
  let inputItemValue = inputItem.value
  idCounter++
  let person = {
      name: inputItemValue,
      completed: false,
      id: idCounter
  }
  todoObject.push(person)
  // console.table(todoObject)
  addToDom()
  // console.log('you clicked the submit button, this is supposed to be for adding a new item')
}
function addToDom() {
  todoSection.innerHTML = ''
  completedSection.innerHTML = ''
  todoObject.forEach(task => {
      if (task.completed === false) {
          todoSection.innerHTML += `<p>${task.name}</p> <button onclick="completeTodo(${task.id})">complete</button>`
      }
      else if (task.completed === true)
          completedSection.innerHTML += `<p>${task.name}</p> <button onclick="deleteTodo(${task.id})">delete</button>`
  }
  )
}
function completeTodo(id) {
  todoObject.forEach(task => {
      if (task.id === id) {
          task.completed = !task.completed
          console.log(task.completed)
          console.log(`you clicked on complete todo with id ${id}, ${task.id}`)
      }
  })
  addToDom()
}
function deleteTodo(id) {
  completedSection.innerHTML -= ''
  todoObject.forEach(task => {
      if (task.id == id) {
          // task.remove(id)
          console.log(task)
      }
  })
}
// initializes the first todos
addToDom()
