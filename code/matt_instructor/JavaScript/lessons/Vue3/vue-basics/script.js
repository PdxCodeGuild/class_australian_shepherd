const app = Vue.createApp({
    data(){
        return{
            message: 'Hello World',
            counter: 0,
            name: '',
            people: ['bob', 'sara', 'evil tammy', 'tim', 'jimmy']
        }
    },
    methods:{
        makeNewMessage(){
            let messageArray = [
                'Tacos for dinner',
                'Bears eat Beets',
                'Olive is a dog',
                'Mike is my ta',
                'Bee is a cat',
                'Hello World'
            ]
            this.message = messageArray[this.counter]
            this.counter++

            if (this.counter === messageArray.length){
                this.counter = 0
            } 
        },
        addPersonToArray() {
            this.people.push(this.name)
        }
    },
    computed: {
        makeMessageUrgent() {
            return this.message + '!'
        }
    },
    mounted(){
        console.log('the app was mounted ', this.message)
    }
})

