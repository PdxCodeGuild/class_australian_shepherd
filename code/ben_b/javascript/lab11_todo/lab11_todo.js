const app = Vue.createApp({
    data(){
        return{
            items: [
                {
                    name: 'eat',
                    status: true,
                },
                {
                    name: 'sleep',
                    status: false,
                },
                {
                    name: 'gym',
                    status: true,
                }
            ],
            itemToDo: '',
            itemCompleted: '',
        }
    },
    methods:{
        addToDo() {
            let newItem = {
                name: this.itemToDo,
                status: true,
            }
            this.items.push(newItem)
            console.log(this.items)
            this.itemToDo = ''
        },

        addCompleted() {
            let newItem = {
                name: this.itemCompleted,
                status: false,
            }
            this.items.push(newItem)
            console.log(this.items)
            this.itemCompleted = ''
        },

        swap(index) {
            this.items[index].status = !this.items[index].status
        }
    },
    mounted(){
        console.log('mounted', this.message)
    },
})