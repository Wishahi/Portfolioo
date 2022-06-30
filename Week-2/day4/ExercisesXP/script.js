//Exercise 1 ++
//PART I
// function infoAboutMe(){
//     console.log("My name is Leen, I am 24, and I am currently enrolled in a Python course");
// }
// infoAboutMe();

// //PART II
// function infoAboutPerson(personName, personAge, personFavoriteColor){
//     console.log("My name is " + personName + " and I am " + personAge + " years old " + "and my favorite color is " + personFavoriteColor)
//     }
// infoAboutPerson("David", 45, "blue")
// infoAboutPerson("Josh", 12, "yellow")






// //Exercise 2 ++
// function calculateTip() {

//     let billAmount = prompt("Enter amount of bill")
    
//     if (billAmount < 50) {
//         console.log(`You have to pay ${billAmount*1.2}`);
//     } else if (billAmount >= 50 && billAmount < 200) {
//          console.log(`You have to pay ${billAmount*1.15}`);
//     } else { (billAmount >200)
//         console.log(`You have to pay ${billAmount*1.1}`);
//     }

// }

// calculateTip();





//Exercise 3 ++


// function isDivisible(d) {
//     let sum = 0;
//     for (let i = 0; i <= 500; i++){
//         if (i % d==0){
//             console.log(i);
//             sum +=i;
//             console.log(sum);
//         }
//     }
    
// }

//isDivisible(3)
// isDivisible(45);










//Exercise 4


// The function should return the total price of your shoppingList. In order to do this you must follow these rules:
// The item must be in stock. (Hint : check out if .. in)
// If the item is in stock find out the price in the prices object.

// Call the myBill() function.

// // Bonus: If the item is in stock, decrease the item’s stock by 1
// let stock = { 
//     "banana": 6, 
//     "apple": 0,
//     "pear": 12,
//     "orange": 32,
//     "blueberry":1
// }  

// let prices = {    
//     "banana": 4, 
//     "apple": 2, 
//     "pear": 1,
//     "orange": 1.5,
//     "blueberry":10
// } 

// let shoppingList = ["banana", "orange","apple" ];

// function myBill(){
//     let sum = 0;
//     //for (x = 0; x < shoppingList.length; x++ ) {
//     for (key in stock){
//     if (stock == 0) {
//         console.log("Stock is empty");
//         sum += x;
//     } else (stock > 0 )
//     {}

//     }
//  }
// myBill();

// function isInStock(item){
//     //if item is in stock and item is greater than 0
//     if (stock[item] && stock[item] > 0){
//         return true;
//     }
//     return false;
// } 

// function itemPrice(item){
//     return prices[item];
// }

// //bonus
// function updateStock(item){
//     stock[item]--;
// }

// function myBill(){
//     let sum = 0;
//     for ( let i = 0; i < shoppingList.length; i ++){
//         let item = shoppingList[i];
//         if (isInStock(item)){
//             console.log(item, itemPrice(item));
//             updateStock(item);
//             sum += itemPrice(item);
//         }
//     }
//     return sum
// }
// // myBill()
// console.log(myBill());
// console.log(stock);









// //Exercise 5 ++
// function changeEnough(itemPrice, amountOfChange){
//     let quarter = amountOfChange[0] * 0.25;
//     let dimes = amountOfChange[1] * 0.10;
//     let nickel = amountOfChange[2] * 0.05;
//     let penny = amountOfChange[3] * 0.01;
//     if ((quarter + dimes + nickel +penny) >= itemPrice){
//         return true;

//     } 
//     else return false;


// };
// console.log(changeEnough(14.11, [2,100,0,0]));
// console.log(changeEnough(4.25, [25, 20, 5, 0]));




//Exercise 6
// function totalVacation(){
// function hotelCost(){
//     let roomCost = 140;
//     let num;
//     do {
//         let userinput = prompt("Enter a number of nights you would like to stay :");
//         num = Number(userinput); 
//         if (userinput > 0) {
//             roomCost = roomCost * num;
//             console.log(roomCost);
//         }
//     }
//     while (typeof num == 'number' && num <= 0 )

// }
// hotelCost();



// function planeRideCost(){
//     let places = {
//         london: 183,
//         paris: 220,
//         any: 300
//     }

//     do {
//         let userinput = prompt("Where would you like to go ?");
//         let city = String(userinput).toLowerCase();
//         console.log(city);
//         if (city == 'london' || city == 'paris'){
//             //return places.london
            
//             console.log(places[city])
//             return places[city];
//         }
//         else return places.any;

//     }
//     while ( typeof string == 'string')
// }
// console.log(planeRideCost());


// function rentalCarCost(){
//         let carCost = 40;
//         let num;
//     do {
//         let userinput = prompt("Enter a number of days you would like to rent the car :");
//         num = Number(userinput); 
//         if (userinput < 10 ) {
//             carCost = carCost * num;
//             console.log(carCost);
//         }
//         else if (userinput > 10 ) {
//                 dCarCost = carCost * num;
//                 // newCarCost = dcarCost * 0.5;
//                 totalCost = dCarCost * .95;
//                 console.log(totalCost);
//             }

//         }

    
//         while (typeof num == 'number' && num <= 0 )
    
//     }
//     rentalCarCost();
   
// }
// console.log(totalVacation(hotelCost() + rentalCarCost() + rentalCarCost()));
