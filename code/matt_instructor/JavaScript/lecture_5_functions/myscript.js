// Overview --------------------------------------------------------------------------------------------------------------------------------
// Function allow us to isolate sections of code.

// Defining Functions 
// There are two ways to define functions in JavaScript. You can declare a function:

// ok since hoisted 
// console.log(add(5, 2))

// function add(a, b)
// {
//     return a + b
// }

// console.log(add(5, 2))



// You can also assign an anonymous function to a variable:


// crashes since not hoisted
// console.log(add(5, 2))

// var add = function(a, b) {
//     return a + b
// }

// console.log(add(5, 2))


// When we declare a function, it's automatically moved to the top of the script
// when the script is run. This means it can be called before it's declared.
// Hoisting: JavaScript Hoisting refers to the process whereby the interpreter 
// appears to move the declaration of functions, variables or classes to the top of their
// scope, prior to execution of the code.



// Default Arguments ------------------------------------------------------------------------------------------------------------------------------------------------------
// function add(a, b=1) {
//     return a + b
// }
// add(5, 2) // 7
// add(5) // 6

// Passing Functions as Parameters
// It's very common to pass a function as a parameter to another function. You can see an example of this in element.addEventListener(), setTimeout(), and windowRequestAnimationFrame().


// Arrow functions in vanilla JS -----------------------------------------------------------------------------------------------

// A traditional function
// function add (num1, num2) {
// 	return num1 + num2;
// }
// console.log(add(1, 2))


// The arrow function version

let add = (num1, num2) => {
    return num1 + num2
}

console.log(add(1, 2))