// for (var temp = 0; temp < 5; temp++) {
//     // Runs 5 times, with values of temp 0 through 4.
//     console.log(temp + ": Institute!");
//   }


//   // && both sides should be true if e.g (1==1 && 2==2)
//     // || only one should be true e.g (1==1 || 2==3)

 let arr = ['a', 'b','c','d','e'];

// //console.log(arr[1]);

// for (let i =0 ; i <arr.length;i++){
//     console.log(i,arr[i]);
// }


for (x in arr){
    console.log(x);
    //console.log(x, arr[x]);

}









//For/In Loop
//   Loops through the properties of an object. This loop continues until all of the properties of the Object are processed.
//   Loops also through the index of an array. This loop continues until all of the elements of the array are processed.

// let obj = {
//     name: 'John',
//     last: 'Miller',
//     age: 18
// }
// for (x in obj){
//     console.log(x);
//     //console.log(x, obj[x]);

// }


// //iterate like an array
// let arr1 = Object.keys(obj);
// console.log(arr1);

// let arr2 = Object.values(obj);
// console.log(arr2);

// let arr3 = Object.entries(obj);
// console.log(arr3);

// // For/Of Loop
// // Loops through the values of an iterable objects such as Arrays and Strings.

// // Careful: an object is not iterable
// //shows value

// for ( x of arr){
//     console.log(x);
// }


// //While Loop
// //Allows code to be executed repeatedly, based on a given Boolean condition.
// for (let i = 0; i <5; i++){
//     console.log(i);
// }

// //OR

// let i =0;
// while (i<5){
//     console.log(i);
//     i++; //i = i+2;
// }

// let i= 0;
// do {
//     console.log(i);
//     i++;
// }
// while(i < 0)


// //i is index
// //item is value
// //forEach is calling back a function

// arr.forEach((item, i) => {
//     console.log(item)
// });


//   //Exercise 1
// for (var num = 0; num <=15 ; num++){
//     if (num % 2 == 0) {
//         console.log( num + " is even")
//     }
//     else {
//         console.log( num  +" is odd")
//     }
// }

// 1. Write a JavaScript for loop that will go through the variable names.

// if the item is not a string, pass.
// if the item is a string, check if its first letter is in uppercase. If not, change it to uppercase and then display the name.
// 2. Write a JavaScript for loop that will go through the variable names

// if the item is not a string, go out of the loop.
// if the item is a string, display it.


let names= ["john", "sarah", 23, "Rudolf",34];
for (let i = 0; i <names.length;i++) {
    if (isNaN(names[i]) ){
        if (names[i].charAt(0).toLowerCase() == names[i].charAt(0)) {
            let name = names[i][0].toUpperCase() + names[i].slice(1);
            names[i] = name; 
        }
       
    } 
} 
console.log(names);




//arr.map
//arr.filter
//arr.sort
//arr.find (finding an element-write condition in it)
//arr.findIndex
//arr.reduce