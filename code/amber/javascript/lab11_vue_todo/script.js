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
      flipBool(){

    },
      addTodoToArray(){

    },
  },
  setup(){

  }
})
