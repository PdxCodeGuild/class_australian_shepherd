// RANDOM PASSWORD GENERATOR

let pool = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'
pool = Array.from(pool)
console.log(pool)


let pwLength = document.querySelector('#pwLength')

let btn = document.querySelector('#btn')

btn.onclick = function() {
  pwLength = parseInt(pwLength.value)
  console.log(pwLength)
}
