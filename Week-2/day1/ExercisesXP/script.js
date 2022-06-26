//Excercise 1
let favoritefood = "cheesecake";
let favoritemeal = "dinner";
console.log(` I eat ${favoritefood} at every ${favoritemeal}`);

//Excercise 2
//Part I
let myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];
let f = myWatchedSeries.join(", ");
let x = f;
let myWatchedSeriesLength = myWatchedSeries.length;
console.log(`I watched ${myWatchedSeriesLength} series :  ${myWatchedSeries[0]}, ${myWatchedSeries[1]} and ${myWatchedSeries[2]} `);

//Part II
myWatchedSeries[0]='friends';
myWatchedSeries.push("Suits");
myWatchedSeries.unshift("Finding Ola");
myWatchedSeries.slice(2);
console.log(`${myWatchedSeries[2].substr(2,1)}`);
console.log(myWatchedSeries);

//Excercise 3
let tempcel = 32;
let tempfaren = tempcel / 5 * 9 +32;
console.log(tempfaren.toFixed(2));






//Excercise 4 
let c;
let a = 34;
let b = 21;

console.log(a+b) //first expression
// Prediction: The answer will be 55, because 34 and 21 are numbers
// Actual:55

a = 2;

console.log(a+b) //second expression
// Prediction: The asnwer will be 23, because the a in the first expression has been overridden by a new number
// Actual: 23

//There is no value for c, as it has been declared with nothing assigned to it. 

console.log(3 + 4 + '5'); 
//Answer : The answer is 75 because th 3 and 4 = 7 and the 5 is a string, so it will be written next to the 4 and not added to it.






//Excercise 5

typeof(15)
// Prediction: Number
// Actual: Number

typeof(5.5)
// Prediction: Number
// Actual: Number

typeof(NaN)
// Prediction: Not a number
// Actual: Number

typeof("hello")
// Prediction: Greeting
// Actual: String

typeof(true)
// Prediction: True
// Actual: Boolean

typeof(1 != 2)
// Prediction: Not equal
// Actual: Boolean

"hamburger" + "s"
// Prediction: Both elements are strings
// Actual: String

"hamburgers" - "s"
// Prediction: Both elements are strings
// Actual: Strings

"1" + "3"
// Prediction: Numbers but strings because of ""
// Actual: Strings

"1" - "3"
// Prediction: Numbers but strings because of ""
// Actual:

"johnny" + 5
// Prediction: String 
// Actual: String

"johnny" - 5
// Prediction: Number 
// Actual: Number

99 * "hello"
// Prediction: Number
// Actual: Number

1 != 1
// Prediction: Not equal
// Actual: Boolean

1 == "1"
// Prediction: Equal
// Actual: Boolean

1 === "1"
// Prediction: Equally strict
// Actual: Boolean







//Excercise 6

5 + "34"
// Prediction: String
// Actual: String

5 - "4"
// Prediction: Number
// Actual: Number 

10 % 5
// Prediction: Divides and produces remainder = 2
// Actual: Number

5 % 10
// Prediction: Divides and produces remainder = 0.5
// Actual: Number

"Java" + "Script"
// Prediction: String
// Actual: String

" " + " "
// Prediction: Empty String
// Actual: String

" " + 0
// Prediction: String
// Actual: String

true + true
// Prediction: Number
// Actual: Number

true + false
// Prediction: Number
// Actual: Number 

false + true
// Prediction: Number
// Actual: Number 

false - true
// Prediction: Number
// Actual: Number 

!true
// Prediction: Not Equal 
// Actual: Number 

3 - 4
// Prediction: Subtraction = -1
// Actual: Number

"Bob" - "bill"
// Prediction: Number
// Actual: Number 

