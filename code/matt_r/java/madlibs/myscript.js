


let btn = document.querySelector('#btn')
let adjNode = document.querySelector('#adj')
let animalNode = document.querySelector('#animal')
let verbNode = document.querySelector('#verb')
let foodNode = document.querySelector('#food')
let partNode = document.querySelector('#part')
let animal_2Node = document.querySelector('#animal_2')
let transNode = document.querySelector('#trans')

btn.onclick = function(){
    console.log('hello')


    let adj = adjNode.value
    let animal = animalNode.value
    let verb = verbNode.value
    let food = foodNode.value
    let part = partNode.value
    let animal_2 = animal_2Node.value
    let trans = transNode.value


    console.log(adj,)//animal,verb,food,part,animal_2,trans)





    let result = document.querySelector('#result')
    result.innerHTML = `Today I went to the zoo. I saw a ${adj} 
        ${animal} jumping up and down in its tree.
        He ${verb} through the large tunnel that 
        led to its home. He the ate a ${food} 
        and rubbed his ${part}. after i headed to see the ${animal_2}s
        and left in my ${trans} to get home.`
}



