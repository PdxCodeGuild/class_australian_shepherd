

let btn = document.querySelector('#btn')

btn.onclick = function(){    //42
    // console.log('hi')

    let passchar = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','!','@','#','$','%','&']
    let password = ''

    let i = 0

    while (i < 8){
        password = password + passchar[Math.floor(Math.random() * (42 - 0) + 0)]
        i++;
        console.log(password)
    }

       

    let result = document.querySelector('#password')
    result.innerHTML =`Your random password is:  ${password}`
}

console.log(password)