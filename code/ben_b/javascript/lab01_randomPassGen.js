// benjamin birky
// lab01_randomPassGen
// 10/20/22




let length_input = document.querySelector('#length_input');
let run_bt = document.querySelector('#run_bt');
let output_div = document.querySelector('#output_div');

let random_char = "abcdefghijklmnopqurstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-=_+[]{}|;:,./<>?~`'"
let final_password = ""
let random_number = 0
let random_display = ""

run_bt.onclick = function() {
    
    
    for (let i=0; i<length_input.value; i++){
        random_number = Math.floor(Math.random() * random_char.length)
        random_display = random_char[random_number]
        final_password = final_password + random_display
    }
    output_div.innerText = final_password;
    console.log(final_password)
}














// let temperature = 90

// if (temperature < 60)
// {
//     console.log('cold')
// }
// else if (temperature < 80)
// {
//     console.log('warm')
// }
// else 
// {
//     console.log('hot')
// }