let num = document.querySelector('#num')
let AvgBtn = document.querySelector('#AvgBtn')
let nums1 = []

AvgBtn.onclick = function () {
    let numValue = num.value
    let nums1 = numValue

    numValue = numValue.split(',')
    numValue = String(numValue)
    // console.log(numValue)
    let total = numValue + numValue
    console.log(total)
}
