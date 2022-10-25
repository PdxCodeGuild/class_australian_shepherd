let word = document.querySelector('#check')
let btn = document.querySelector('#btn')
btn.addEventListener('click', function handleClick(event) {
    let wordsplit = word.value.split('')
    // console.log(wordsplit)
    let backwards = wordsplit.reverse()
    console.log(backwards)
    let newword = wordsplit.join("")
    console.log(word.value)
    console.log(newword)
    if (word.value === newword) {
        console.log(true)
        console.log('palindrome')
    } else {
        console.log('not a palindrome')
    }
})