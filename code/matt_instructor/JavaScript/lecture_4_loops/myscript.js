// While-Loops --------------------------------------------------------------------------------------------------------------------------------------------
// While-loops will run while the given condition is true.

// let i = 0
// while (i < 5)
// {
//     console.log(i)
//     // i = i + 1
//     i++
// }
// 0 1 2 3 4


// For-Loops ----------------------------------------------------------------------------------------------------------------------------------------------
// For-loops have three parts, separated by semi-colons. 
// The first is the initialization, 
// the second is the condition 
// and the third is the increment. 
// These are simply the parts of the while loop from above re-arranged.

// for (initialization; condition; increment)




// for (let i = 0; i < 5; i++)
// {
//     console.log(i)
// }

// console.log('hello class')
// console.log('this is the second one')
// console.log('this is the third one')

// Iterating over a String ---------------------------------------------------------------------------------------------------------------------------------


let s = 'hello'

// let i = 0

// while (i < s.length)
// {
//     console.log(s[i])
//     i++
// }


// iterate over the indices of the characters of a string using a for-loop
// for (let i = 0; i < s.length; i++)
// {
//     console.log(s[i])
// }

// iterate over the indices of a string using for-in
// for (index in s)
// {
//     console.log(s[index])
// }

// iterate over the characters of a string using for-of
// for (element of s)
// {
//     console.log(element)
// }


// Iterating over an Object/Array -------------------------------------------------------------------------------


let fruits = {
    'apples': 1,
    'bananas': 1.5,
    'plums': 1.25
}

for (key in fruits)
{
    console.log(key + ' ' + fruits[key])
}

// Continue and Break --------------------------------------------------------------------------------
// The continue keyword will skip the rest of the current iteration and start 
// with the next iteration.


let nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]

for (let i = 0; i < nums.length; i++)
{
    if (nums[i] % 2 == 1)
    {
        continue
    }
    console.log(nums[i])
}
// // 0 2 4 6 8

let nums_2 = [1, 2, 3, 4, 5, 6, 7, 8]
for (let i = 0; i < nums_2.length; i++)
{
    if (nums_2[i] % 2 == 1)
    {
        break
    }
    console.log(nums_2[i])  //not reachable 
}