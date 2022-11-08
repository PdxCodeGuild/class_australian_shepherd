const app = Vue.createApp({
    data(){
        return{
            message: 'Hello World',
            inputValue: '',
            todo: [ 
                // {
                //     name: "Eat",
                //     completed: true,
                // },
                // {
                //     name: 'sleep',
                //     completed: false
            
                // }
            
                
            ],

        }
    },
    methods:{
        makeNewTodo(){
            let todoArray = {
                    name: this.inputValue,
                    completed: false,
                }
            
            
            this.todo.push(todoArray)
            
        },
        changeComplete(item){
            for (let i = 0; i<this.todo.length; i++){
                if (this.todo[i].name === item.name){
                    this.todo[i].completed = !this.todo[i].completed
        
                }
            }
        },
        change(item){
            for (let i = 0; i<this.todo.length; i++){
                 if (this.todo[i].name === item.name){
                    this.todo.pop(item)
                    console.log(item)       
                 }
             }            
        },


        
    },
    setup(){
        
    }
})