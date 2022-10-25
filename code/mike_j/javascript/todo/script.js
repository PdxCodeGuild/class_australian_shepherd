const inc_items = []
const comp_items = []

let input = document.querySelector('#input')
let incomplete = document.querySelector('#incomplete')
let completed = document.querySelector('#completed')

function add() {
    inc_items.push(input.value)
    incomplete.innerHTML = inc_items
}

function mv_to_comp() {
    let popped = inc_items.pop()
    comp_items.push(popped)
    incomplete.innerHTML = inc_items
    completed.innerHTML = comp_items
}

function rem1() {
    inc_items.pop()
    incomplete.innerHTML = inc_items
    completed.innerHTML = comp_items
}

function mv_to_inc() {
    let popped = comp_items.pop()
    inc_items.push(popped)
    incomplete.innerHTML = inc_items
    completed.innerHTML = comp_items
}

function rem2() {
    comp_items.pop()
    incomplete.innerHTML = inc_items
    completed.innerHTML = comp_items
}