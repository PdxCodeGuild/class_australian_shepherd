

let rock = document.querySelector('#rock');
let paper = document.querySelector('#paper');
let scissors = document.querySelector('#scissors');

let shoot_bt = document.querySelector('#shoot_bt');
let output_div = document.querySelector('#output_div');

let random_number = 0;

shoot_bt.onclick = function() {
    random_number = Math.floor(Math.random() * 3)
    

    if (rock.checked === true && random_number === 0) {
        output_div.innerHTML = `Computer picks Rock. You Tie.`
    }else if (rock.checked === true && random_number === 1) {
        output_div.innerHTML = `Computer picks Paper. You Lose :(`
    }else if (rock.checked === true && random_number === 2) {
        output_div.innerHTML = `Computer picks Scissors. You Win!`
    }else if (paper.checked === true && random_number === 0) {
        output_div.innerHTML = `Computer picks Rock. You Win!`
    }else if (paper.checked === true && random_number === 1) {
        output_div.innerHTML = `Computer picks Paper. You Tie.`
    }else if (paper.checked === true && random_number === 2) {
        output_div.innerHTML = `Computer picks Scissors. You Lose :(`
    }else if (scissors.checked === true && random_number === 0) {
        output_div.innerHTML = `Computer picks Rock. You Lose :(`
    }else if (scissors.checked === true && random_number === 1) {
        output_div.innerHTML = `Computer picks Paper. You Win!`
    }else {
        output_div.innerHTML = `Computer picks Scissors. You Tie.`
    }
}



