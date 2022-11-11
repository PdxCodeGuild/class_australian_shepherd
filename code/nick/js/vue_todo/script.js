const app = Vue.createApp({
    data(){
        return{
            counter: 0,
            item: '',
            itemList: []
        }
    },
    methods:{
        addItemToArray() {
            this.itemList.push({
                id: this.counter,
                todo: this.item,
                complete: false, 
                archive: false});
            this.counter++
            this.item = ""
            
        }, 
        completeTask(itemId) {
            let i = this.itemList.findIndex(obj => obj.id === itemId)
            this.itemList[i].complete = !this.itemList[i].complete
        },
        archiveTask(itemId) {
            let i = this.itemList.findIndex(obj => obj.id === itemId)
            this.itemList[i].archive = !this.itemList[i].archive
        },
    },
})