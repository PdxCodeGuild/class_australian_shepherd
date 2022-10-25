

let name_input = document.querySelector('#name_input');
let location_input = document.querySelector('#location_input');
let adjective_input = document.querySelector('#adjective_input');
let dessert_input = document.querySelector('#dessert_input');

let run_bt = document.querySelector('#run_bt');
let output_div = document.querySelector('#output_div');



run_bt.onclick = function() {
    let madLib_output = `Welcome to Chef ${name_input.value}'s restaurant!
                        We are currently located in ${location_input.value}.
                        Tonight we will be serving a ${adjective_input.value} ${dessert_input.value}.
                        Enjoy :)`
    console.log(madLib_output)
    output_div.innerText = madLib_output;
    madLib_output = ""
}

