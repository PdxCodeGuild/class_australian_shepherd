// CREDIT CARD VALIDATOR

let cardInput = document.querySelector('#cardInput')

let btn = document.querySelector('#btn')

let cardNumbers = []


// how to error handle for integers and length of input?

btn.onclick = function() {
  cardInput = cardInput.value // on btn click save value of cardInput

  // convert string into array of strings
  cardInput = Array.from(cardInput)
  // console.log(cardInput)

  // iterate thru array to convert strings to ints
  for (let i = 0; i < cardInput.length; i++)
    cardNumbers.push(parseInt(cardInput[i]))
    // console.log(cardNumbers)

  // slice off the last digit and save as check digit
  // checkDigit.push(cardNumbers.pop())
  let checkDigit = cardNumbers.pop()
  // console.log('Check digit: ' + checkDigit)
  // console.log(cardNumbers.length)

  // reverse the remaining digits
  cardNumbers.reverse()
  // console.log(cardNumbers)

  // double every other element in the reversed list
  for (let i = 0; i < cardNumbers.length; i = i + 2) {
   cardNumbers[i] *= 2
  }
  // console.log(cardNumbers)

  // subtract 9 from numbers over 9 in the doubled reversed list
  for (let i = 0; i < cardNumbers.length; i = i + 2) {
    if (cardNumbers[i] > 9) {
      cardNumbers[i] -= 9
    }
   }
  //  console.log(cardNumbers)

  // sum all values in reversed list
  let sumNumbers = 0
  for (let i = 0; i < cardNumbers.length; i++) {
    sumNumbers += cardNumbers[i]
   }
  //  console.log(sumNumbers)

  // take the second digit of that sum
  sumNumbers = sumNumbers.toString()
  sumNumbers = Array.from(sumNumbers)
  // console.log(sumNumbers)

  let sumDigit = sumNumbers.pop()
  sumDigit = parseInt(sumDigit)
  // console.log('Sum digit: ' + sumDigit)

  // compare to check digit. if it matches, the card is valid
  // return valid or invalid

  let pTag = document.querySelector('#pTag')

  if (checkDigit === sumDigit) {
    // console.log('valid')
    pTag.innerHTML = 'Congrats, your card is VALID!'
  }
  else {
    // console.log('invalid')
    pTag.innerHTML = 'Sorry, your card is INVALID!'
  }


}
