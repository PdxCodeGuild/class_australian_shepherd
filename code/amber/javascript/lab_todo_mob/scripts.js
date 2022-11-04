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
// let remove = document.querySelector('#delete-btn')
// let completeP = document.querySelector('#complete-p')

function addToDom() {
  todoObject.forEach(inputItem => {
      if (inputItem.completed === false) {
        todoSection.innerHTML += `<p>${inputItem.name}</p> <button onclick="completeTodo(${inputItem.id})">Complete</button> <button onclick="deleteTodo(${inputItem.id})">Remove</button>`
      }
      else {
        completedSection.innerHTML += `<p>${inputItem.name}</p> <button onclick="todo(${inputItem.id})">To Do</button> <button onclick="deleteTodo(${inputItem.id})">Remove</button>`
      }
  }
  )
}


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
  todoSection.innerHTML = ''
  completedSection.innerHTML = ''
  addToDom()
  // console.log('you clicked the submit button, this is supposed to be for adding a new item')
}

function todo(id) {
  for(let i = 0; i < todoObject.length; i++)
  {
    if (todoObject[i].id === id)
    {
      todoSection.innerHTML += `<p>${inputItem.name}</p> <button onclick="completeTodo(${inputItem.id})">To Do</button>`
      todoObject[i].completed = false
      console.log(todoObject[i])
    }
  }
  todoSection.innerHTML = ''
  completedSection.innerHTML = ''
  addToDom()
}

function completeTodo(id) {
  for(let i = 0; i < todoObject.length; i++)
  {
    if (todoObject[i].id === id)
    {
      completedSection.innerHTML += `<p>${inputItem.name}</p> <button onclick="todo(${inputItem.id})">To Do</button>`
      todoObject[i].completed = true
      console.log(todoObject[i])
    }
  }
  todoSection.innerHTML = ''
  completedSection.innerHTML = ''
  addToDom()
}

//
function deleteTodo(id) {
  for(let i = 0; i < todoObject.length; i++)
  {
    if (todoObject[i].id === id)
    {
      // completedSection.innerHTML += `<p>${inputItem.name}</p> <button onclick="todo(${inputItem.id})<button onclick="deleteTodo(${tasks.id})">Remove</button>">To Do</button>`
      // todoSection.innerHTML += `<p>${inputItem.name}</p> <button onclick="completeTodo(${inputItem.id})<button onclick="deleteTodo(${tasks.id})">Remove</button>">Complete</button>`
      console.log(todoObject[i])
      todoObject.splice(i, 1)
    }
  }
  todoSection.innerHTML = ''
  completedSection.innerHTML = ''
  addToDom()
}

// initializes the first todos
addToDom()
//



// KNOWN BUGS:

// COMPLETED LIST READS NaN WHEN EMPTY

// WHEN LIST IS EMPTY AND A NEW ITEM IS SUBMITTED, THE PREVIOUSLY CLEARED ITEMS RETURN TO COMPLETED

// IF YOU DELETE ONE ITEM FROM THE LIST IT DELETES THEM ALL

// INPUT FIELD DOES NOT CLEAR AFTER SUBMISSION

// should make delete button work in todo and redo button in complete

// redo button could just flip the bool... mess with the buttons in addtodom
