



// //Exercise 2
// let user = prompt(enter string sep by commas);
// let sumUser = user.trim().split(" ");
// let result = 0;



//Exercise 3
let str = prompt('Please find my Nemo !');
let pos = str.indexOf('Nemo');


console.log(pos);
// console.log(str.indexOf('Nemo'));
console.log(str.substring(pos, pos+4));


 str = str.substring(pos+5, pos.length);
 console.log(str);
pos = str.indexOf('Nemo');
console.log(str.substring(pos,pos+4));

str = str.substring(pos+5, pos.length);
console.log(str);
pos = str.indexOf('Nemo');
console.log(str.substring(pos,pos+4));


// let arr = str.split(' ');
// console.log(arr.indexOf('Nemo'));


