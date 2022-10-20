// CREDIT CARD VALIDATOR

let cardInput = document.querySelector('#cardInput')

let btn = document.querySelector('#btn')

let cardNumbers = []

let checkDigit = []

let reversedDigits = []

// how to error handle for integers and length of input?

btn.onclick = function() {
  cardInput = cardInput.value // on btn click save value of cardInput

  // convert string into array of strings
  cardInput = Array.from(cardInput)


  // iterate thru array to convert strings to ints
  for (let i = 0; i < cardInput.length; i++)
    cardNumbers.push(parseInt(cardInput[i]))
    // console.log(cardNumbers)

  // slice off the last digit and save as check digit
  checkDigit.push(cardNumbers.pop())
  // console.log(checkDigit)
  // console.log(cardNumbers.length)

  // reverse the remaining digits
  // for (let i = 0; i < cardNumbers.length; i++) {
  //   reversedDigits.push(cardNumbers.pop())
  //   console.log('rd:' + reversedDigits)
  //   console.log('cn' + cardNumbers)
  // }



}
