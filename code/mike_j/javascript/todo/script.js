document.getElementById("new").value = ""

document.querySelector("#add").onclick = function() {
    
    document.querySelector("#tasks").innerHTML += `
        <ul class="item">
            <span class="span">
                ${document.querySelector("#new").value}
            </span>
            <div class="buttons">
                <button class="todo">ToDo</button>
                <button class="done">Done</button>
                <button class="delete">Delete</button>
            </div>    
        </ul>
    `
    document.getElementById("new").value = ""

    let todo = document.querySelectorAll(".todo");
    for(let i=0; i<todo.length; i++) {
        todo[i].onclick = function() {
            this.parentNode.previousElementSibling.style.textDecoration = "none"
            this.parentNode.parentNode.style.color = "black"
        }
    }

    let done = document.querySelectorAll(".done");
    for(let i=0; i<done.length; i++) {
        done[i].onclick = function() {
            this.parentNode.previousElementSibling.style.textDecoration = "line-through"
            this.parentNode.parentNode.style.color = "red"
        }
    }

    let tasks = document.querySelectorAll(".delete");
    for(let i=0; i<tasks.length; i++) {
        tasks[i].onclick = function() {
            this.parentNode.parentNode.remove()
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
