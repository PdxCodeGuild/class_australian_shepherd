let nums = []
let sum = 0

let input1 = document.querySelector('#input1')
let entBtn = document.querySelector('#entBtn')
let disp_nums = document.querySelector('#disp_nums')
let result = document.querySelector('#result')  

entBtn.onclick = function() {
    
    sum += Number(input1.value)
    
    nums.push(input1.value)
    
    disp_nums.innerHTML = nums
    
    let avg = (sum/nums.length)
    
    let rounded = avg.toFixed()
    
    result.innerHTML = rounded
    
    document.getElementById('input1').value = ""
}
