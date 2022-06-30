function playTheGame(){
    let result = window.confirm("Would you like to play a game ?");
    // if (confirm == false){
    //     prompt("OK, GOODBYE");
    // }
   let message = result ? 'Lets play!' : (alert("OK GOODBYE"));
   let guessLimit = 3;
   let attempts = 0;

    let userinput = prompt("Pick a number between 0 and 10:");
     let num = Number(userinput); 
      while (typeof num == 'number' && userinput !=num ){
         userinput= prompt("Sorry not a number, enter a number :");
         num = Number(userinput);
      }
     // }
    //  if (userinput != num){
    //     alert("Sorry not a number, Goodbye");
    //  }

     if (userinput > 0 && userinput > 10) {
            alert("Sorry it's not a good number, Goodbye");

     }
     else if (userinput >= 0 && userinput <=10) {
        let computerNumber = Math.floor(Math.random() * 11);
        console.log(computerNumber);
        let ret = compareNumbers(userinput,computerNumber);
        
        while (ret){
            userinput = prompt("Enter a new number");
            num = Number(userinput);
            ret = compareNumbers(num, computerNumber)
            attempts = num;
            if ( attempts > guessLimit ){
               return false;
            }
            //break;
        }
     }
    }

function compareNumbers(userinput,computerNumber){
    console.log(userinput, computerNumber);
    if ( userinput == computerNumber){
        alert("WINNER");
        return false;
    }
    else if (userinput > computerNumber){
        alert("Your number is bigger then the computer’s, guess again");
        // userinput = prompt("Enter a new number");
        return true;
    } 
    else if (userinput < computerNumber) {
        alert("Your number is smaller then the computer’s, guess again");
        // userinput = prompt("Enter a new number")
        return true;
    }
}

//compareNumbers();
