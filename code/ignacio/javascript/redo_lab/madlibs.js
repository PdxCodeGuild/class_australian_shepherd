let word1 = document.querySelector('#word1')
let word2 = document.querySelector('#word2')
let word3 = document.querySelector('#word3')
let GenBtn = document.querySelector('#GenBtn')
let result = document.querySelector('#result')


GenBtn.onclick = function ()
{
    let word1Value = word1.value
    let word2Value = word2.value
    let word3Value = word3.value

    result.innerHTML =  'hey look  that ' + word1Value + ' landed on that ' + word2Value + '! it was so ' + word3Value
    

}
