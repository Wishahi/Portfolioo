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