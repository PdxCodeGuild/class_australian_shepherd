const app = Vue.createApp({
    data() {
        return {
            todoList: [{
                item:'cook',
                completed: false
            },
        ],
        item:''
    }
    },

    methods: {
        mounted() {
            // console.log('the app was mounted ', this.message)
        },
        addTask() {
            let task = {
                item: this.item,
                completed: false
            }
            this.todoList.push(task)
            // console.log(this.todoList)
        },

    }
})