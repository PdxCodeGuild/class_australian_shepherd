// Printing in JS -------------------------------------------------------------------------------------------------------------
// In JavaScript, we can see our data like a Python print() by using console.log()

// console.log('hello world')

// Declaring Variables --------------------------------------------------------------------------------------------------------

// Unlike in python, we need to declare the type of variable we are working with

// let
// let is a flexible way of declaring a variable. It allows for re assignment of the
// storage space and standard scope

let x = 1

x = 8

// let x = 8 DONT DO THIS. dont use let on a already declared variable 

// console.log(x)

// var
// var is similar to let that it can be re-declared, however it has a global scope.
// var is sometimes used for older browser support, but let should be used unless 
// the global scope is being used and makes sense 

var y = 2

y = 9

// console.log(y)


// const
// const is a constant variable, meaning it cannot be changed. It is helpful for when you
// do not want a variable to be changeable.
// depending on the environment you are running, const can be helpful for efficiency 
// like with 3d animations using Three.js

const z = 3

// z = 5 // this will not work. const can NOT be re assigned

// console.log(z)


// NOTE ABOUT CONST. we can change the values in an array (list) or object (dict) and 
// our program does not break

const people = ['bob', 'tim', 'jill']
people[0] = 'Greg'
// console.log(people)



// Booleans, Comparisons, and Conditionals --------------------------------------------------------------------------------------------------------

// console.log(5 == '5') // true
// console.log(5 == 5) // true

// console.log(5 === 5) // true
// console.log(5 === '5') // false

// == equal-to, may coerce types 
// === equal-to, does not coerce types (recommended)
// != not-equal, may coerce types (not recommended)
// !== not-equal, does not coerce types (recommended)

// < less-than
// <= less-than-or-equal-to
// > greater-than
// >= greater-than-or-equal-to

// console.log(5 == '5') // true
// console.log(5 === '5') // false

// console.log(5 !== 5) // is the same as in python print(5 not 5)


// There are three boolean operators: 'and' &&, 'or' || and 'not' !. -----------------------------------------------------------

// DO NOT USE:          and or not
// use the following:   &&  || !

let a = 5

if (a > 0 && a < 10) 
{
    console.log('a is between 5 and 10')
}   

if (a === 5 || a === 6)
{
    console.log('a is 5 or 6')
}

let b = true
if (b)
{
    console.log('true is truthy therefore the conditional is true')
}

b = false

if (!b)
{
    console.log('will display if b has a truthy value')
}


// Type Coercion --------------------------------------------------------------------------------------------
// If the two operands of == aren't of the same type, the JavaScript interpreter will try to convert 
// them to the same type so they can be compared. This may result in unexpected behavior.
// In practice, it's better to use === which will only be true if both operands are of the 
// same type and value.

// console.log(5 == '5') // true
// console.log(5 == 5) // true
// console.log(5 === '5') // false
// console.log(5 === 5) // true

// == tries to convert
// === dose not try to convert

// == will confuse you and cause bugs, === is your friend and will never let you down


// Conditionals ---------------------------------------------------------------------------------------------
// Conditionals in JavaScript require parentheses and curly-braces.


let temperature = 90

if (temperature < 60)
{
    console.log('cold')
}
else if (temperature < 80)
{
    console.log('warm')
}
else 
{
    console.log('hot')
}


// Truthy and Falsey ------------------------------------------------------------------------------------------------
// JavaScript lets you pass non-boolean types into conditionals, which may evaluate to true or false, depending on
// what generally makes sense. All values are 'truthy' except false, 0, "", null, undefined, and NaN. 


let c = 0
if (c){
    console.log('true')
} else{
    console.log('false!')
}


// Functions in vanilla JS also Arrow Functions -----------------------------------------------------------------------------------------------


// A traditional function
function add(num1, num2)
{
    return num1 + num2
}

// console.log(add(5, 9))


// The arrow function version 
let add_2 = (num1, num2) => {
    return num1 + num2
}

// console.log(add_2(1, 2))


// Ternary Operator  -----------------------------------------------------------------------------------------------

// Conditional (ternary) operator
// The conditional (ternary) operator is the only JavaScript operator that takes 
// three operands: a condition followed by a question mark (?), then an expression 
// to execute if the condition is truthy followed by a colon (:), and finally the 
// expression to execute if the condition is falsy. This operator is frequently used 
// as an alternative to an if...else statement.


function getFee(isMember) {
    return (isMember ? '$2.00' : '$10.00');
}

console.log(getFee(true))
// expected output: "$2.00"

console.log(getFee(false))
// expected output: "$10.00"

console.log(getFee(null));
// expected output: "$10.00"

console.log(getFee('apples'));
// expected output: "$2.00" because truthy

console.log(getFee(''));
// expected output: "$10.00"