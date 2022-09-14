// // setTimeout(function(){
// // console.log('after 2 seconds');
// // printHello('Ellie')
// // },3000)
// // //3000 is in millseconds so 3 seconds

// // function printHello(name){
// //     console.log(name);
// // }

// // let id;
// // function start(){
// //      id = setTimeout(function(){
// //         console.log('haha');
// //     },2000)
// //     console.log(id);
// // }

// // function stop(){
// //     clearTimeout(id)
// // }

// // function start(){
// //     let index = 0
// //     id = setInterval(function(){
// //         index++;
// //         console.log(index);
// //     },2000)
// // }

// // function stop(){
// //     clearInterval(id)

// // }

// // let innerbox = document.getElementById('inner');
// // console.log(innerbox);

// function start(){
//     let x = 1;
//     setInterval(function(){
//         x++;
         
// //   let left = x + "px";
//   innerbox.style.left=x;
        
//         // console.log(index);
//     },1000/60)
//     // innerbox.style.right=left;
// }

// function stop(){
//     clearInterval(innerbox)

// }

// function start(){
//     let box = document.getElementById('inner');
//     let pos = 0;
//     let x = 0
//     let id = setInterval(function(){
//         if (pos == 350){
//             clearInterval(id)
//         } else {

        
//         pos++;
//         x--;
//         box.style.left=pos+ "px";
//         box.style.bottom=x + "px";
//         }

//     },5)
// }

// //container
// let orangeSquare = document.getElementById('drop-container');
// let pinkSquareContainer = document.getElementsByClassName('draggable-container')[0];

// //pink square element - draggable element
// let pinkSquare = document.getElementById('draggable-element');

// // console.log(orangeSquare);
// // console.log(pinkSquareContainer);
// // console.log(pinkSquare);

// pinkSquare.addEventListener('dragstart', function(event){
//     console.log(event.target, event.target.id);
//     event.dataTransfer.setData('pink-square', event.target.id);

//     event.dataTransfer.effectAllowed = "move";
//     event.target.style.cursor= 'move';
//     // event.target.classList.add('hide');
// })

// pinkSquare.addEventListener('dragend', function(event){
//     // event.target.style.cursor = 'pointer';
//     // event.target.classList.remove('hide');
// })

// orangeSquare.addEventListener('dragover', function(event){
  
//     event.preventDefault();
// })

// orangeSquare.addEventListener('drop', function(event){
//     event.preventDefault();
//     let id = event.dataTransfer.getData('pink-square');
//     let pinkBox = document.getElementById(id);
//     event.target.appendChild(pinkBox);


// })

// pinkSquareContainer.addEventListener('dragover', function(event){
//     event.preventDefault();
// })

// pinkSquareContainer.addEventListener('drop', function(event){
//     event.preventDefault();
//     let id = event.dataTransfer.getData('pink-square');
//     let pinkBox = document.getElementById(id);
//     event.target.appendChild(pinkBox);


// })

// let elem = document.getElementById('dragelement');


// elem.addEventListener('dragend', function(event){
//     elem.style.border = "none";

// })

// elem.addEventListener('dragend', function(event){
//     // console.log(event);
//     let x = event.clientX;
//     let y = event.clientY;
//     elem.style.border = '5px solid red';
//     console.log(x,y);
//     elem.style.left = x+ 'px';
//     elem.style.top = y + 'px';

// })


function start(){
    let box = document.getElementById('inner');
    let pos = 0;
    let id = setInterval(function(){
      if(pos == 350){
        clearInterval(id)
      }
      else{
        pos++
        box.style.left = pos + "px";
        box.style.top = pos + "px";
      }
  
    },1)
  }