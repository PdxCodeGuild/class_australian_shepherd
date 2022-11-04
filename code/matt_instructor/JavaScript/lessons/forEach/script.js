const people = [
    {
        name: 'Bob',
        age: 45,
        location: 'Oregon',
        id: 1
    },
    {
        name: 'Sarah',
        age: 33,
        location: 'Washington',
        id: 2
    }
]

// let container = document.querySelector('#container')
// let output = document.querySelector('#output')

// for (let i = 0; i < people.length; i++)
// {
//     // console.log(people[i].name)
//     let person = `<button onclick="logIt(${people[i].id})">Reveal Info of Person ${people[i].id}</button>`


//     container.innerHTML += person
// }

// const logIt = function(id){

//     console.log(id)
//     for (let i = 0; i < people.length; i++)
//     {
//         if (people[i].id === id)
//         {
//             output.innerHTML = `${people[i].name} ${people[i].age} ${people[i].location} <button>remove</button>`
//         }
//     }
// }

let container = document.querySelector('#container')
let output = document.querySelector('#output')

people.forEach(person => {
    container.innerHTML += `<button onclick="logIt(${person.id})">Reveal Info of Person ${person.id}</button>` 
})


const logIt = function(id){
    people.forEach(person => {
        if (person.id === id){
           output.innerHTML = `${person.name} ${person.age} ${person.location} <button onclick="{removeName()}">remove</button>`
        }
    })
}


const removeName = function() {
    console.log('if you gave the function an id as an argument, you could pass that into this function, and then delete the element from the dom')
}