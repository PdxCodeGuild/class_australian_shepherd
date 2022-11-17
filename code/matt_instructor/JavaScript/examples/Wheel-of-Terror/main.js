const app = Vue.createApp({
    data(){
        return{
           students: ['iggy', 'kacey', 'nick', 'justin', 'ben', 'mike', 'amber', 'matt'],
           delayVar: .1
        }
    },
    methods: {
        animate() {
            this.resetVariablesAndNode()
            let numberOfCycles = this.getNumberOfCycles()
            let cycleCounter = 0
            let choseStudentIndex = this.getChosenStudentIndex()

            // while cycle counter is not equal to number of cycles
            while (true){

                for (let i = 0; i < this.students.length; i++){
                    gsap.to(`#${this.students[i]}`, {delay: this.delayVar, color: 'red'})
                    this.resetOtherStudentsColor(i)
                    this.delayVar += .2
                }
                cycleCounter++
         
                // do a final loop to show the 'winner' and stop on the index of the student who won
                if (cycleCounter === numberOfCycles){

                    for(let i = 0; i < choseStudentIndex; i++){
                        gsap.to(`#${this.students[i]}`, {delay: this.delayVar, color: 'red'})
                        this.delayVar += .2
                        this.resetOtherStudentsColor(i)
                    }
                    break
                }

            }


        },



        getNumberOfCycles(){
            return parseInt(Math.random() * (5 - 2) + 2)
        },

        getChosenStudentIndex(){
            return parseInt(Math.random() * (this.students.length - 0) + 0)
        },

        resetOtherStudentsColor(i){
            // if first student, make last student white
            if (this.students[i - 1] === undefined)
            {
                gsap.to(`#${this.students[this.students.length -1]}`, {delay: this.delayVar, color: 'white'})
            }
            else{
                gsap.to(`#${this.students[i -1]}`, {delay: this.delayVar, color: 'white'})

            }
        },

        resetVariablesAndNode(){
            this.delayVar = .1

            for (let i = 0; i  < this.students.length; i++){
                gsap.to(`#${this.students[i]}`, {delay: 0, duration:0 , color: 'white'})
            }
        }

    },
    mounted(){

    }
})
