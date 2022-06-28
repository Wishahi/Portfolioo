//Exercise 1 ++
// let people = ["Greg", "Mary", "Devon", "James"];
// newpeople = people.slice(1);

//  newpeople.splice(2,1,"Jason");
// newpeople.push("Leen");
// console.log(newpeople.indexOf("Mary")); //0
// console.log(newpeople.slice(0)); 
// console.log(newpeople.indexOf("Foo")); // returns -1 because the value is not contained in the array

// //length of the array - 1
// let last = newpeople.length-1; ///help
// console.log(last);

// //UNCOMMENT
// // for ( let i = 0; i < newpeople.length; i ++){
// //     console.log(newpeople[i]);
// // }



// for (let i = 0; i  < newpeople.length;i++){
//     if (newpeople[i] === "Jason"){
//         break;
//     }
//     console.log(newpeople[i]);   
// }







// //Exercise 2 ++
// let colors = ['pink', 'white', 'red', 'purple', 'gray'];
// for (let i = 0; i < colors.length; i++){
//     let indexNumber = Number(i) +1;
//     console.log("My #" + indexNumber + " choice is " + colors[i]);    
// }
//  let suffix = ["st", "nd", "rd", "th", "th"];
//  for (i in colors, suffix) {
//     let numIndex = Number(i)+1;
//     console.log("My " + numIndex+suffix[i] +" choice is " + colors[i] );
//  }










//Exercise 3 ++
// Prompt the user for a number.
// Hint : Check the data type you receive from the prompt 
//(ie. Use the typeof method)

// While the number is smaller than 10 continue asking the user 
// for a new number.
// Tip : Which while loop is more relevant for this situation?

// let userinput = prompt("Enter a number :");
// let num = Number(userinput); //string to numbe
// while (typeof num == 'number' && num < 10 ){
//     userinput= prompt("Enter a number :");
//     num = Number(userinput);
// }







//Exercise 4 ++

// let building = {
//     numberOfFloors : 4,
//     numberOfAptByFloor : {
//         firstFloor : 3,
//         secondFloor : 4,
//         thirdFloor : 9,
//         fourthFloor : 2,
//     },
//     nameOfTenants : ["Sarah", "Dan", "David"],
//     numberOfRoomsAndRent:  {
//         sarah: [3, 990],
//         dan :  [4, 1000],
//         david : [1, 500],
//     },
// }

// console.log(building.numberOfFloors);
// console.log(building.numberOfAptByFloor.firstFloor, building.numberOfAptByFloor.thirdFloor);
// console.log(building.nameOfTenants[1], building.numberOfRoomsAndRent.dan[0]);
// //console.log(building.numberOfRoomsAndRent.sarah[1])
// if (building.numberOfRoomsAndRent.sarah[1] + building.numberOfRoomsAndRent.david[1] > building.numberOfRoomsAndRent.dan[1]){
  
//   building.numberOfRoomsAndRent.dan[1] += 200;                          
// }
// console.log(building);









//Exercise 5 ++
// Create an object called family with a few key value pairs.
// Using a for in loop, console.log the keys of the object.
// Using a for in loop, console.log the values of the object.

// let family = {
//     lastname: 'Miller',
//     members: 6,
//     female: 2,
//     male: 5,
//     }
//     for (let key in family){
//         console.log(`${key}`);
//         console.log(`${family[key]}`);
//     }








//Exercise 6 ++
// let details = {
//     my: 'name',
//     is: 'Rudolf',
//     the: 'raindeer'
//   }

//   for (let key in details) {
//     console.log(`${key} ${details[key]}`);
//   }





//  Exercise 7
// A group of friends have decided to start a secret society. 
// The society’s name will be the first letter of each of their names sorted in alphabetical order.
// Hint: a string is an array of letters
// Console.log the name of their secret society. The output should be “ABJKPS”


// let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
// //let index= 0;
// for (let i =0; i < names.length; i++){
//     console.log(names.charAt(i));
// }

//secretname.sort();
//console.log(secretname);

//charatindex0
//let secretname = names.map((name) => name[0]).join('');



 