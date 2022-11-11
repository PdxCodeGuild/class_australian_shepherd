

gsap.to('#green-sock', {delay: 1, duration: 1, color: 'green'})

// Rotate Text color: much less robust and easy to understand than vanilla js or css versions
// -1 is an infinite loop. If it was 4, it would loop 4 times
let tl = gsap.timeline({repeat: -1})
tl.to('#rotating-text', {color: 'green'})
tl.to('#rotating-text', {color: 'red'})
tl.to('#rotating-text', {color: 'blue'})


let toggleBtn = document.querySelector('#toggle-btn')
let toggle = false

toggleBtn.addEventListener('click', () => {
    if (toggle)
    {
        gsap.to('#app', {background: '#ffd000'})
    }
    else{
        gsap.to('#app', {background: '#87ceeb'})
    }
    toggle = !toggle
})  



let balloonBtn = document.querySelector('#balloon-btn')

balloonBtn.addEventListener('click', () => {
    gsap.to('#balloon', {duration: 20, y: '-110vh', x: '70vw'})
    gsap.to('#balloon', {display: 'block'})

    let tl = gsap.timeline({repeat: -1})
    tl.to('#balloon', {duration: 1, rotate: '2.5deg'})
    tl.to('#balloon', {duration: 1, rotate: '-2.5deg'})
    tl.to('#balloon', {duration: 1, rotate: '0deg'})
    }
)


gsap.to('#trigger-container', {
    scrollTrigger: {
        trigger: '#trigger-container',
        start: '-100 center',
        end: '100 center',
        toggleActions: 'play none none none',
        scrub: 1,
        // markers: true
    },
    color: 'red',
    display: 'block',
    opacity: 1

})