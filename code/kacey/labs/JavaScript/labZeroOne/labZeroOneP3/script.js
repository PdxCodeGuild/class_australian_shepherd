let readyBtn = document.querySelector("#readyBtn")
readyBtn.onclick = function() {
    let nounPerson1 = document.querySelector('#nounPerson1').value;
    let nounPerson2 = document.querySelector('#nounPerson2').value;
    let nounThing = document.querySelector('#nounThing').value;
    let nounPersonPlaceThing1 = document.querySelector('#nounPersonPlaceThing1').value;
    let nounPersonPlaceThing2 = document.querySelector('#nounPersonPlaceThing2').value;
    let nounPersonPlaceThing3 = document.querySelector('#nounPersonPlaceThing3').value;

    displayText.innerHTML = `${nounPerson1} went to the beach with ${nounPerson2}.First,they swam in the ${nounThing}.Then,they saw ${nounPersonPlaceThing1} and ${nounPersonPlaceThing2}.Lastly, they built a sandcastle out of ${nounPersonPlaceThing3}`;

}