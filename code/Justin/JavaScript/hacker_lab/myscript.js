
// var canvas = document.querySelector('canvas'),
//     ctx = canvas.getContext('2d');

// canvas.width = window.innerWidth;
// canvas.height = window.innerHeight;

// var letters = 'ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよ';
// letters = letters.split('');

// var fontSize = 15,
//     columns = canvas.width / fontSize;

// var drops = [];
// for (var i = 0; i < columns; i++) {
//   drops[i] = 0;
// }

// function draw() {
//   ctx.fillStyle = 'rgba(0, 0, 0, .1)';
//   ctx.fillRect(0, 0, canvas.width, canvas.height);
//   for (var i = 0; i < drops.length; i++) {
//     var text = letters[Math.floor(Math.random() * letters.length)];
//     ctx.fillStyle = '#ff1818';
//     ctx.fillText(text, i * fontSize, drops[i] * fontSize);
//     drops[i]++;
//     if (drops[i] * fontSize > canvas.height && Math.random() > .95) {
//       drops[i] = 1;
//     }
//   }
// }

// setInterval(draw, 85);

// let login = document.querySelector('#login')
// document.body.addEventListener('keypress', (event) => {
//   login.style.display = 'flex'
// })


// let btn = document.querySelector('#btn')

// btn.addEventListener('click', function handleClick(event) {
//     if (user.value === 'admin') {
//       console.log('ok')
//       login.style.display = 'none'
//       location.replace(src='newpage.html')
//     }
//     else {
//       console.log('no')
//     }
// })



// setTimeout (() => {

//   background.style.display = 'none'
//   progbar.style.display = 'none'
// }, 1000);

let code = [
  'hack = start', 
  '......', 
  'if hack == TRUE:', 
  'event = context.parameter.event', 
  'text = context.split(" ");', 
  'run.event.SQLInject(DBMS+user+id+^[a-zA-Z])', 
  '%%%%%injecting good stuff%%%%%', 
  'trying search bar', '.......', 
  'Hey there, World', '......no results', 
  'trying iframe',
'.....',
'iframe src="javascript:alert(`xss`)"',
'....success', 'trying email.....', 
'email:', 'OR true--', 'Password:sdf', 
'.....success','running search bar exploit',
'....',
"http://yoursite.com/rest/products/search?q='--", 
'....sucess',
'running gather....', 
"http://yoursite.com/rest/products/search?q'--)) UNION SELECT id,email,password FROM Users--", 
'.....success', 
'RESULTS: =>', 
'status: "success"', 
'data:', 
'0:',    
'id: 1',   
"name: 'admin@yoursite.com'",    
"description: '01SEc92qz356se' - SHA 256 Encryption"
]


let progbar = document.querySelector('#progbar')
let hackercode = document.querySelector('#hackercode')
let counter = 0

document.body.addEventListener('keypress', (event) => {
  hackercode.innerHTML = ''
  progbar.style.display = 'none';
  for (let i=0; i < counter; i++) {
    console.log(code[i]);
    hackercode.style.color = 'rgb(0,255,0)'
   
    if (counter < code.length) {
      hackercode.innerHTML += '<p>' + code[i] + '</p>'
    } else {
      counter = 0
    }
  }
  counter ++
})
