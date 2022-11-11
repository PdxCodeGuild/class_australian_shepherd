// Lab Credit Card Validation
// Let's write a function which returns whether a string containing a credit card number is valid as a boolean. The steps are as follows:

// Convert the input string into a list of ints
// Slice off the last digit. That is the check digit.
// Reverse the digits.
// Double every other element in the reversed list.
// Subtract nine from numbers over nine.
// Sum all values.
// Take the second digit of that sum.
// If that matches the check digit, the whole card number is valid.

let x = document.querySelector('#creditCardNumber');
console.log(x.value)

function validation(cc_number) {
    // Convert the input into an array
    let number_list = cc_number.split("");
    console.log(number_list);
    // Grab the check digit from the end
    let check_digit = number_list.pop();
    console.log(check_digit);
    console.log(number_list);
    // Reverse the existing list
    number_list.reverse();
    console.log(number_list)
    // Double every other element in reversed list
    let new_list = []
    for (number in number_list) {
        if (number % 2 === 0) {
            new_list.push((number_list[number]) * 2); 
        }
        else {
            new_list.push(parseInt(number_list[number]))
        }
    }
    console.log(new_list);
    // Subtract nine from numbers over nine
    for (number in new_list) {
        if (new_list[number] > 9) {
            let new_number = (new_list[number] - 9);
            new_list.splice(number, 1, new_number)
        }
    }
    console.log(new_list)
    // Sum array
    let sum_array = 0;
    for (number in new_list) {
        sum_array += new_list[number] 
    }
    console.log(sum_array)
    // Take second digit of sum
    let final_digit = sum_array.toString();
    
    if (Array.from(final_digit)[1] === check_digit) {
        return document.getElementById("validCCstatus").innerHTML = "Valid!";
    } else {
        return document.getElementById("validCCstatus").innerHTML = "Invalid CC number!";
    }
}

function ccValidator() {
    var x = document.getElementById("creditCardNumber").value;
    if (x.length === 16) {
        validation(x)
    } else {
        document.getElementById("validCCstatus").innerHTML = "Invalid!";
    }
}