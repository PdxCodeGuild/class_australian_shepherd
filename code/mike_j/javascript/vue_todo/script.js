const app = Vue.createApp({
    data(){
        return{
            todoArray: [],
            input: ''
        }
    },
        methods:{
            addItem(){
                let tasks = {
                    task: this.input,
                    completed: false
                }
                this.todoArray.push(tasks)
                this.input = ''
                console.log(this.todoArray)
            },
            deleteItem: function(index) {
                this.todoArray.splice(index, 1)
                console.log(this.todoArray)
            },
            focusInput() {
                this.$refs.input.focus();
              }
        },
        mounted() {
            this.focusInput();
          },
        setup(){
            document.addEventListener("keydown", function(event) {
                if (event.key === "Enter") {
                    event.preventDefault()
                    document.getElementById("addBtn").click()
                }
            })
        }
})
