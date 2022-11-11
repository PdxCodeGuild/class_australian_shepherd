let passage = document.querySelector("#passage")
let countrymen = document.querySelector("#countrymen")
let ears = document.querySelector("#ears")
let bury = document.querySelector("#bury")
let men = document.querySelector("#men")
let good = document.querySelector("#good")
let bones = document.querySelector("#bones")

passage.innerHTML = `Friends, Romans, countrymen, lend me your ears<br>
    I come to bury Caesar, not to praise him.<br>
    The evil that men do lives after them<br>
    The good is oft interred with their bones<br>
    So let it be with Caesar.`    

function org() {
    passage.innerHTML = `Friends, Romans, countrymen, lend me your ears<br>
    I come to bury Caesar, not to praise him.<br>
    The evil that men do lives after them<br>
    The good is oft interred with their bones<br>
    So let it be with Caesar.`
}

function madlib() {
    passage.innerHTML = `Friends, Romans, ${countrymen.value}, lend me your ${ears.value}<br>
    I come to ${bury.value} Caesar, not to praise him.<br>
    The evil that ${men.value} do lives after them<br>
    The ${good.value} is oft interred with their ${bones.value}<br>
    So let it be with Caesar.`
}

function reset() {
    passage.innerHTML = `Friends, Romans, countrymen, lend me your ears<br>
    I come to bury Caesar, not to praise him.<br>
    The evil that men do lives after them<br>
    The good is oft interred with their bones<br>
    So let it be with Caesar.`

    document.getElementById('countrymen').value = ""
    document.getElementById('ears').value = ""
    document.getElementById('bury').value = ""
    document.getElementById('men').value = ""
    document.getElementById('good').value = ""
    document.getElementById('bones').value = ""
}
