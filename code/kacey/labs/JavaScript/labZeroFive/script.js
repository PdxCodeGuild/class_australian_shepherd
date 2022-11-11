// const toggleDisplay = document.querySelector("#toggleDisplay");

const app = Vue.createApp({
    data() {
        return {
            newTask: "",
            items: [
                {
                    todo: "eat",
                    displayed: true,
                },
                {
                    todo: "sleep",
                    displayed: false,
                },
                {
                    todo: "code",
                    displayed: true,
                },
            ],
        };
    },
    methods: {
        toggleDisplay(index) {
            console.log(this.items[index]);

            this.items[index].displayed = !this.items[index].displayed;
            // for (item in this.items) {
            //     console.log(item);
            //     console.log("task.todo", task.todo);
            //     console.log("this.items[item].id", this.todo[item]);
            //     if (this.items[item].id === task.todo) {
            //         console.log("this clicking?");
            //         this.item.displayed = !this.item.displayed;
            //     }
            // }
        },
        addNewTask() {
            console.log("this.items", this.items);
            console.log("this.newTask", this.newTask);
            let newArray = {
                todo: this.newTask,
                displayed: true,
            };
            this.items.push(newArray);
        },
        deleteArray(index) {
            // console.log("this is index", index);
            // console.log("this.items.splice(index)", this.items.splice(index));
            // console.log(
            //     "this.items.splice(index, 1)",
            //     this.items.splice(index, 1)
            // );
            this.items.splice(index, 1);
        },
    },
    setup() {},
});

// const tester = (onclick.toggleDisplay = function () {
//
// });

// document.body.addEventListener("keydown", function (event) {
//     // console.log("test", test);
//     console.log("test.code", test.code);
//     if (event.code === "Enter") {
//         tester();
//     }
// });
