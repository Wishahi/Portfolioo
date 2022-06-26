//NUMBERS

// declaring and assigning a variable 
// let my_num=100; 
// let a;
// a=10; //assigning a value in 2 ways
// let b = a+my_num;
// console.log(my_num);//100
// console.log(a); //10
// console.log(a + my_num); //110
// console.log(b); //110
// console.log(b+a);//120

// let a =5;
// let b=10;
// //or
// // let c=7, d=8, f=a+b;
// let c = a+b;

// a=6;

// console.log(a, b, c);

//const cannot be changed whatsoever, declare with uppercase (TOTAL+CLICKS)


//STRINGS

// let name = 'John';
// let last_name = 'Miller';
// let space = ' ';
// console.log( name + ' ' + last_name);
// //or
// console.log( name + space + last_name);
// //or
// console.log(`${name} ${last_name}`); //template strings

// let a = 10; //if inside '' it will considered a string
// let b = 'Hello';
// let c = true; // 1
// let d = false; // 0
// let f= ''; // will be considered a string and not null


// console.log( typeof(a));
// console.log( typeof(b));
// console.log( typeof(c));
// console.log( typeof(d));
// console.log( typeof(f));

//undefined is not declared;
//null is nothing


//NUMBER METHODS

// //convert number to string
// var x =123;
// console.log(x.toString() + 4); //1234
// console.log(x + 4); //127
// 123.toString;
// (100+23).toString();

// toFixed()
// var x = 9.656;
// x.toFixed(0); //10
// x.toFixed(2); // 9.66
// x.toFixed(4); //9.6560
// x.toFixed(6); //9.656000

// toPrecision()
// var x= 9.656;
// x.toPrecision(0); //9.656
// x.toPrecision(2); //9.7
// x.toPrecision(4);//9.656 
// x.toPrecision(6);//9.65600 

// //convert string to number
// let a = '10';
// let b ='20';
// a + b; //1020
// Number (a) + Number(b); //30

// parseInt //returns without decimals
// parseFloat //retruns with decimals

//////////////CHECK DOCUMENT SENT ON SLACK - NUMBER METHODS////////////////

//STRING METHODS

// var txt = "ABCDEFGH";
// var a = txt.length;
// console.log(a);


// var str = "Please locate";
// var pos = str.indexOf("locate");
// console.log(pos);


// var str = "Please locate where 'locate' occurs";
// var pos = str.lastIndexOf("locate");
// console.log(pos);

// var str = "Please locate";
// var pos = str.search('locate');
// console.log(pos); //7

// //slice
// //substring
// //substr

// var str = "HELLO WORLD";
// let a = str.charAt(4); //a will be O;

// //exercise 1
// let addressNumber = 26;
// let addressStreet = 'Lehi';
// let country = 'israel';
// let globalAddress =  `I live in ${addressNumber} ${addressStreet} ${country}`; //template strings
// //let globalAddress = addressNumber + " " + addressStreet + " " + country;
// console.log(globalAddress);

// //exercise 2
// let birthyear = 1997;
// let futureyear = 2050;
// let age = futureyear - birthyear;
// console.log(age.toFixed(0));


//ARRAY

// let arr = [];
// //or
// let arr1 = new Array();


let arr = [1,3,4,6];
let a = arr[2];
console.log(a);

arr[3] = 8;
console.log(arr);// [1,3,4,8]

arr[4] = 8;
console.log(arr); // [1,3,4,6,8]

arr[7] = 9;
console.log(arr); //[1,3,4,6,'','',',9']

let arr1 = [1,3,4,
                [3,5,
                [7,8,9]]
                    ];

console.log(arr1[3][2][1]); //8

//ARRAY METHODS

//toString //converts into string
//join // joins elemtns
//pop remove last element
//push add new element to end of array
//shift removes first element 
//unshift add new element to beginning of array
//concat joins elements
//slice cust elements





