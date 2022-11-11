const app = Vue.createApp({
    data(){
        return{
            toDos: [

            ],
            inputValue: ''
        }
    },

        methods:{
            addToDo(){
                let tasks = {
                    task: this.inputValue,
                    completed: false
                }
                this.toDos.push(tasks)
                this.inputValue = ''
                console.log(this.toDos)
            },
            deleteToDoByIndex: function(index) {
                this.toDos.splice(index, 1)
                console.log(this.toDos)
            }
        },

        setup(){

        },
})