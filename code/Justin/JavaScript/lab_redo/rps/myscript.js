let enemy = ['rock' , 'paper' , 'scissors']


// This was a pain to figure out
let radioButtons = document.querySelectorAll('input[name="game"]')
btn.addEventListener("click", () => {
    let randIndex = Math.floor(Math.random() * enemy.length)
    let enemyChoice = (enemy[randIndex])
    let selectedName;
    for (let radioButton of radioButtons) {
        if (radioButton.checked) {
            selectedName = radioButton.id
        }
    }
    console.log(enemyChoice)
    console.log(selectedName)
    let status = document.querySelector
    ('#status')
    let btn2 = document.querySelector('#btn2')
    if (enemyChoice === selectedName){
        status.innerHTML = `Enemy selected ${enemyChoice}! You draw!`
    } else if (enemyChoice === 'scissors' && selectedName === "rock") {
        status.innerHTML = `Enemy selected ${enemyChoice}! You Win!`
    } else if (enemyChoice === "scissors" && selectedName === "paper") {
        status.innerHTML = `Enemy selected ${enemyChoice}! You Lose!`
    } else if (enemyChoice === "paper" && selectedName === "rock") {
        status.innerHTML = `Enemy selected ${enemyChoice}! You Lose!`
    } else if (enemyChoice === "paper" && selectedName === "scissors") {
        status.innerHTML = `Enemy selected ${enemyChoice}! You Win!`
    } else if (enemyChoice === "rock" && selectedName === "scissors") {
        status.innerHTML = `Enemy selected ${enemyChoice}! You Lose!`
    } else if (enemyChoice === "rock" && selectedName === "paper") {
        status.innerHTML = `Enemy selected ${enemyChoice}! You Win!`
    };
    btn2.style.display = 'block';
    btn2.addEventListener('click', function handleClick(event) {
        document.querySelector('input[name="game"]:checked').checked=false;
        btn2.style.display = 'none'
        document.querySelector('#status').innerHTML = '';
    })
});