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

      }
  },
  methods:{
      flipBool(todo){
        // todo.complete = !todo.complete
        console.log(todo)
        console.log(todo.complete)
    },
      addNewTodo(){
        let newTodo = {
          name: this.name,
          complete: false,
        }
        this.todoArray.push()
    },
  },
  setup(){

  }
})
