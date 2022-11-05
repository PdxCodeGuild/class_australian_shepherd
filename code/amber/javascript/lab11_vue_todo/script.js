const app = Vue.createApp({
  data(){
      return{
          todoArray: [
              {
                  name: 'sweep',
                  complete: false,
              },
              {
                  name: 'mop',
                  complete: false,
              },
              {
                name: 'dust',
                complete: true,
              },
          ],
          name: ''
      }
  },
  methods:{
      flipBool(todo){
        console.log(todo)
        for (let i = 0; i < this.todoArray.length; i++){
          // console.log(todo.name)
          // console.log(this.todoArray[i].name)
          if (todo.name === this.todoArray[i].name){
            this.todoArray[i].complete = !this.todoArray[i].complete
          }
        }
    },
      addNewTodo(){
        let newTodo = {
          name: this.name,
          complete: false,
        }
        this.todoArray.push(newTodo)
    },
  },
  mount(){

  }
})
