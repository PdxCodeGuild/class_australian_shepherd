let num = document.querySelector('#num')
let AvgBtn = document.querySelector('#AvgBtn')
let result = document.querySelector('#result')

AvgBtn.onclick = function () {
    let numValue = num.value
    let total = 0

    numValue = numValue.split(',')
    
    // console.log(numValue)
    for (let count = 0; count < numValue.length; count++) {
        total += parseInt(numValue[count])
    }
    let avg = total/numValue.length
    // console.log(avg)
    result.innerHTML = avg
}
