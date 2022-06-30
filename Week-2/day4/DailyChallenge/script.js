let userinput = prompt("Enter a sentence ");
let n = 5; // row or column count
let strsplit = userinput.split(' ');
longestWord = 0;
let string = "";

for (let i = 0; i <strsplit.length;i++){
    if (strsplit[i].length > longestWord){
        longestWord = strsplit[i].length;
        console.log(longestWord);
    }
}
//return longestWord;


for (let i = 0; i < n; i++) {
  for (let j = 0; j < n; j++) { 
    if (i === 0 || i === n - 1) {
      string += "*";
    }
    else {
      if (j === 0 || j === n - 1) {
        string += "*";
      }
      else {
        string += " ";
      }
    }
  }
  // newline after each row
  string += "\n";
}

let userWords = prompt("bla bla");
userWords.userWords.split(" ,");
let maxLength = 0;
for (let i = 0; i < maxLength.maxLengthl;i++){
  let x = userWords[i];
  if (x.length>maxLength){
    maxLength = x.length;
  }
  else {
    maxLength =+0;
  }
}
console.log(maxLength);
for (z = "*"; z.length<maxLength+4; z = z+ "*"){

}
console.log(z);


for (j =0; j <userWords.length; j++){
  c = " ";
  multi = maxLength-userWords[j].length;
  rest = c.repeat(multi);
  console.log( " * " + userWords[j] + rest+ " *");
}
console.log(z);


// let words = ["Hello", "World", "in", "a", "frame"];

// //retrun the length of the longest word
// function longestWordLength(arr){
//   let len = arr[0].length;
//    for ( let i =1; i < words.length; i++){
//         if (arr[i].length > len){
//           len = arr[i].length;
//         }
//    }
//    return len;
// }

// //string with spaces
// function addSpaces(word, len){
//   if (word.length == len){
//     return "";
//   }
//   return " ".repeat(len-word.length);

// }


// function stars (){
//   let len =longestWordLength(words);
//   //console.log(len);

//   //length of the word 2 stars before and 2 stars after
//   console.log("*".repeat(len+4));
//   for (x in words){
//     console.log('* ' + words[x] + addSpaces(words[x],len) + ' *');

//   }
//   console.log("*".repeat(len+4));
// }
// stars();