

let area= document.querySelector('#area')

let alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z', '¼', '½', '¾', '⅓', '⅔', '⅛', '⅜', '⅝', '≈', '>', '≥', '≧', '≩', '≫', '≳', '⋝', '÷', '±', '∓', '≂', '⊟', '⊞', '⨁', '⨤', '⨦', '%', '∟∠∡', '⊾⟀', '⦜', '⦛', '⦠', '√', '∛', '∜', '⍍', '≡', '≢', '⧥', '⩧', '⅀', '◊', '⟠', '⨌⨍⨏', '⨜', '⨛', '◜', '◝', '◞', '◟', '⤸', '⤹', '◆', '◇', '❖', '○', '◍', '●', '◐', '◑', '◒', '◓', '◔', '◕', '◖', '◗', '⬡', '⬢', '‰', 'ⁿ', '¹', '²', '³', '§', '∞', 'ㅅ', '⌖', '◧', '◨', '◩', '◪', '▢', '▣', '▤', '▥', '▦', '▧', '▨', '▩', '▬', '▭', '▮', '▯', '▰', '▱', '◆', '◇', '◈', '◉', '◊', '○', '◌', '◎', '◘', '◙', '◚', '◛', '◜', '◝', '◞', '◟', '◠', '◡', '◢', '◣', '◤', '◥', '◦', '◫', '◬', '◭', '◮', '◯', '▲', '△', '▴', '▵', '▷', '▸', '▹', '►', '▻', '▼', '▽', '▾', '▿' , '◁', '◂', '◃', '◄', '◅']
const textArray = [
    'hello ', 
    "You've been hacked!",
    '<span class="test"> andfhg a </span>',
    '<span class="center"> hello </span>',
]


let content = ''
let counter = 1

// document.body.addEventListener('keypress', (event) => {
//     console.log(event)

//     content=''
    
//     for (let i=0; i < counter; i++){
        
//         content += textArray[i]
//     }

//     counter += 1
    
//     area.innerHTML=''
//     area.innerHTML= content
    
// })


document.body.addEventListener('keypress', (event) => {
    console.log(event)

    content=''
    let word=''


    for (let i=0; i < counter; i++){
        
        content += textArray[i]
    }

    
    let wordLength = Math.floor(Math.random() * (10 - 0) + 0)
    
    for (let i=0; i < wordLength; i++){
        
        let alphaIndex = Math.floor(Math.random() * (166 - 0) + 0)
        let letter = alphabet[alphaIndex]
        
        
        word = word + letter 
        
    }
    
    textArray.push(word + '....')
    console.log(word)

    counter += 1
    
    area.innerHTML=''
    area.innerHTML= content
    
})