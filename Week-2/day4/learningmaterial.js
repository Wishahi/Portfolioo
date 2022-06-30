//Exercise 1
// function age(myAge) {
//     console.log("My mom is twice my " + myAge + " and my dad is 1.2 the " + myAge + " of my mom");
// }
// age(30);




// //Exercise 2
// function age(myAge) {
//     let result = "My mom is twice my " + myAge
//     return result
// }
// let ageInfo = age(30)
// console.log(ageInfo)



//Exercise reverse
//reverse each word in a given string
//for example:
//given this "word in a given string"
//result "drow ni a nevig gnirts"

// let arr = ["word", "in", "a", "given", "string"];
//  //let strsplit = arr.sp

// function reverse(){ no
//     for ( i = 0; i < arr.length; i--){
//         return true;
//     }
// }




// function reverseWord(str){
//     let ret = '';
//     //looping a string by reverse from end to beginning
//     //starting from end let i = str.length-1
//     for (let i = str.length-1; i >= 0; i--) {
//         ret +=str[i];
 
//     }

//     return ret;
// }
// // console.log(reverseWord('word'));

// //reverse all sentence
// function reverseAll(str){
//     let arr = str.split(' ');
//     let ret = ('');
//     //let ret = [];
//     for ( let i = 0; i < arr.length; i++){
//         ret += reverseWord(arr[i]) + ' '
//         //ret.push(reverseWord(arr[i]))
//     }
//     return ret;
//     //retrun ret.join(' ');
// }
// console.log(reverseAll("word in a givenn String"));

//uou need recursive 
// Given n, take the sum of the digits of n.
// If that value has more than one digit,
// continue reducing in this way until a single-digit
// number is produced.
// This is only applicable to the natural numbers.
// Examples
//     16  -->  1 + 6 = 7
//    942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
// 132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
// 493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2