const app = Vue.createApp({
    data(){
        return{
            message: 'Hello World',
            counter: 0
        }
    },
        methods:{
            makeNewMessage(){
                
                let messageArray = [
                    'tacos for dinner',
                    'something something darkside',
                    'bee is a cat',
                    'olive is a dog',
                    'bears eat beets'
                ]
                // to pull items into scope
                this.message = messageArray[this.counter]
                this.counter ++

                if (this.counter === messageArray.length){
                    this.counter = 0
                }
            }
        },
        setup(){

        },
})