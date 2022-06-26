//Exercise 1
let fruits = ["Banana", "Apples", "Oranges", "Blueberries"];
newFruits = fruits.slice(1);
newFruits.sort();
newFruits.push("Kiwi"); 
newFruits.splice(0,1);
newFruits.reverse();
console.log(newFruits);


//Exercise 2

let moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
console.log(moreFruits[1][1][0]);