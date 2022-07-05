// //Exercise 1
// //1
// let article1= document.getElementsByTagName('article');
// // console.log(article1[0].firstElementChild);

// //2
// for (let i = 0; i < article1[0].children.length; i ++){
//     //console.log(article1[0].lastElementChild.textContent);
// }
// article1[0].removeChild(article1[0].lastElementChild);

// //3
// let h2 = document.getElementsByTagName('h2');
// h2[0].addEventListener('click', function onClick(event)
// {
//     event.target.style.backgroundColor="red";
// })

// //4
// let h3 = document.getElementsByTagName('h3');
// h3[0].addEventListener('click', function onClick(event){
//     event.target.style.display="none";
// })

// //5
// function inform(){
//     document.body.style.fontWeight= "bold";
//     }
// let input = document.getElementsByTagName('input')
// input[0].addEventListener('click', inform);

// //BONUS
//1
// let h1 = document.getElementsByTagName('h1')
// h1[0].addEventListener("mouseenter", function( event ) {
//     document.body.style.fontSize = Math.floor((Math.random() * 8) + 3)+"px";
//     //settimeout

// })
//2 CHECK CSS




//Exercise 2
// 1
let form = document.getElementsByTagName('form');
console.log(form[0]);
//2
// let input = document.querySelectorAll('input #id');
let input = document.getElementsByTagName('input #id');
console.log(input);
//3 
// let input1 = document.getElementsByTagName('input').attributes["fname"].value;
// console.log(input1);
let name = document.forms.elements.fname.value;
console.log(name);

// //Exercise 3
// let allBoldItems = document.getElementsByTagName('strong');
// // function getBold_items(){
// //  allBoldItems = 
// // console.log(allBoldItems[0]);
// // }
// function highlight(){
//     for ( let i = 0; i<allBoldItems.length; i++){
//         allBoldItems[i].style.color = "blue";
//          }
// }
// allBoldItems[0].addEventListener("mouseover", highlight);
// // hightlight();

// function returnNormal(){
    
//         for ( let i = 0; i<allBoldItems.length; i++){
//             allBoldItems[i].style.color = "black";
        
//         }
    
// }
// allBoldItems[0].addEventListener("mouseout", returnNormal);
// // returnNormal();

// Exercise 4
// function calculateVolume(){
//     // 'use strict';
//     let volume;
//     let radius = document.getElementById('radius').value;
//     radius = Math.abs(radius);
//     volume =  (4/3)* Math.PI * Math.pow(radius,3);
//     volume = volume.toFixed(4);

//     document.getElementById('volume').value = volume;
//     return false;
// }

// function all(){
//     // 'use strict';
//     document.getElementById('MyForm').onsubmit = calculateVolume;
// }
// window.onload = all;


//Exercise 5
// let x = document.getElementById("btn");

// x.addEventListener("click", RespondClick); 
// x.addEventListener("mouseover", RespondMouseOver); 
// x.addEventListener("mouseout", RespondMouseOut);
// x.addEventListener("dblclick", DoubleClick);

// function RespondClick() { 
   
//     document.body.style.backgroundColor="red"
// } 

// function RespondMouseOver() { 
//     //alert("My mouse is over the btn")
//     for ( let i = 0; i<x.length; i++){
//                 // x[i].style.color = "blue";
//                 document.style.color="blue";
//      }
// } 

// function RespondMouseOut() { 
//     //alert("My mouse is out of the btn")
// } 

// function DoubleClick(){
//     // x[0].body.style.backgroundColor="red";
//     alert("Button Clicked")

// }




