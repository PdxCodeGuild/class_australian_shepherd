document.getElementById("new").value = ""

document.querySelector("#add").onclick = function() {
    
    document.querySelector("#tasks").innerHTML += `
        <ul class="item">
            <span>
                ${document.querySelector("#new").value}
            </span>
            <button class="delete">Delete</button>
        </ul>
    `
    document.getElementById("new").value = ""

    let tasks = document.querySelectorAll(".delete");
    for(let i=0; i<tasks.length; i++) {
        tasks[i].onclick = function() {
            this.parentNode.remove()
        }
    }
}

document.querySelector("#clr").onclick = function() {

    document.querySelector("#tasks").innerHTML = ""
}

document.addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
        event.preventDefault()
        document.getElementById("add").click()
    }
})
