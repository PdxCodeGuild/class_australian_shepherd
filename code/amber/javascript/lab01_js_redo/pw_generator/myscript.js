// RANDOM PASSWORD GENERATOR

let pool = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'
pool = Array.from(pool)
console.log(pool)

let poolLength = pool.length
console.log(poolLength)

function RandInt(max) {
  return Math.floor(Math.random()*max)
}

let poolCopy = []

let pwArray = []

let pwLength = document.querySelector('#pwLength')

let btn = document.querySelector('#btn')

btn.onclick = function() {
  pwLength = parseInt(pwLength.value)
  // console.log(pwLength)



  // loop thru pool and add to new array pwLength # of times
  for (let i = 0; i < poolLength; i++) {
    poolCopy.push(pool[i])

  }
  // console.log(poolCopy)
  // console.log(pool)

  for (let i = 0; i < pwLength; i++) {
    pwArray.push(poolCopy[Math.floor(Math.random()* poolLength)])

  }
  // console.log(pwArray)

  // convert array to string
  let pwString = pwArray.join('')
  // console.log(pwString)

  // return pw to user in dom
  let pTag = document.querySelector('#pTag')

  pTag.innerHTML = `Your cool new ${pwLength} character password is: ${pwString}`

}
