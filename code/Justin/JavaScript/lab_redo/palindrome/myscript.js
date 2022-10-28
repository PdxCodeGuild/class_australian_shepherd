let word = document.querySelector('#check')
let btn = document.querySelector('#btn')
btn.addEventListener('click', function handleClick(event) {
    let wordsplit = word.value.split('')
    // console.log(wordsplit)
    let backwards = wordsplit.reverse()
    let newword = wordsplit.join("")
    let results = document.querySelector('#results')
    if (word.value === newword) {
        results.innerHTML = `${word.value} and ${newword} are a palindrome`
    } else {
        results.innerHTML = `${word.value} and ${newword} are not a palindrome`
    }
})