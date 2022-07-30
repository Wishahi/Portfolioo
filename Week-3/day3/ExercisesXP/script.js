//Exercise 1
//1
// function HelloWorld() {
//     alert("Hello World");
//   }
  
//   setTimeout(HelloWorld, 2000)

//2
//   function callContainer(){
//     let div = document.getElementById('container');
//     let p = document.createElement('p');
//     p.textContent = "Hello World";
//     div.appendChild(p).innerHTML;
//   }
//   setTimeout(callContainer, 2000);

// //3++4
//   let id;
//   function callContainer(){
//     let count= 0;
//     id = setInterval(function(){
//             let div = document.getElementById('container');
//             let p = document.createElement('p');
//             p.textContent = "Hello World";
//             div.appendChild(p);
//             count ++;
//             if (count >= 5){
//                 _clear();
//             }
//         }, 2000);
// console.log(id);
//   }
//   callContainer();


//   function _clear(){
//     console.log('clear',id);
//         clearInterval(id);
//   }
  

//Exercise 2
function myMove(){
    let box = document.getElementById('animate');
    let pos = 0;
    // let x = 0
    let id = setInterval(function(){
        if (pos == 350){
            clearInterval(id)
        } else {

        
        pos++;
        // x--;
        box.style.left=pos+ "px";
        // box.style.bottom=x + "px";
        }

    },5)
}



//Exercise 3
// let yellowSquare = document.getElementById('target'); //orange
// let redSquare = document.getElementById('box'); //pink

// redSquare.addEventListener('dragstart', function(event){
//     console.log(event.target, event.target.id);
//     event.dataTransfer.setData('red-square', event.target.id);

//     // event.dataTransfer.effectAllowed = "move";
//     // event.target.style.cursor= 'move';
//     // event.target.classList.add('hide');
// })

// yellowSquare.addEventListener('dragover', function(event){
//   event.preventDefault();
// })

// yellowSquare.addEventListener('drop', function(event){
//     event.preventDefault();
//     let id = event.dataTransfer.getData('red-square');
//     let redBox = document.getElementById(id);
//     event.target.appendChild(redBox);

// })

