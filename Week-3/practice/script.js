

//longest string in an array
// function longestString(arra){ ++
//     let max_string = arra[0].length
//     let ans = arra[0]
//     for (let i = 1; i < arra.length; i ++){
//         maxi = arra[i].length
//         if (maxi > max_string){
//             ans = arra[i]
//             maxi = max_string
//         }
//     }
//     return ans
// }

// console.log(longestString(["Rana", "George", "Ben", "Mohammed"]));



//second biggest number
// arr= [7,10,8,555,2,4,44,90] ++
// function processData(arr){
//      firstLargestNumber = Math.max(...arr) // firstLargestNumber
//      index = arr.indexOf(firstLargestNumber) // the index of firstLargestNumber
//      arr.splice(index, 1) // Delete first largest number
//      secondLargestNumber = Math.max(...arr) // firstlargestNumber got removed, lets find next largest number
//     //  return (secondLargestNumber)  //return the value
//     console.log(secondLargestNumber);
// }
// processData([7,10,8,555,2,4,44,90])




// get a message and u need to crop it to be K characters ++ 
// const crop = (message, maxLength) => {
//     const part = message.substring(0, maxLength + 1);
//     return part.substring(0, part.lastIndexOf(" ")).trimEnd();
//   }
  
//   console.log(crop("The quick brown fox jumped over the fence", 19)+">");
//   console.log(crop("The quick brown fox jumped over the fence", 9)+">");
//   console.log(crop("The quick brown fox jumped over the fence", 8)+">");
//   console.log(crop("The              ", 6)+">");
//   console.log(crop("The quick ", 20)+">");


//password check ++
// const strongPasswordCheckerII = function(password) {
//     const regex = new RegExp("^(?!.*(.)\\1)(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*()+-]).{8,}$", 'g')
//     return regex.exec(password) !== null
//   };
// console.log(strongPasswordCheckerII("Farfosh1!"))







// function findTransactionAmountByYear(transactions, transactions_dates, year) ++ {
//     let total = 0;
//     for (let i = 0; i < transactions.length; i++) {
//         const amount = transactions[i];
//         const date = transactions_dates[i];
//         if (Number(date.split('-')[2]) === year) {
//             total += amount
//         }
//     }
//     return total;
// }



// const final_result = findTransactionAmountByYear([-100, 50, 60, -10, 200], ['02-08-2019', '20-10-2020', '21-10-2020', '05-10-2020', '20-10-2022',], 2020)
// // should return 50+60-10 = 100
// console.log(final_result)



// csv string max value ++
// function convertCSV(str, delimiter = ',') {
//     const titles = str.slice(0, str.indexOf('\n')).split(delimiter);
//     const rows = str.slice(str.indexOf('\n') + 1).split('\n');
//     return rows.map(row => {
//         const values = row.split(delimiter);
//         return titles.reduce((object, curr, i) => (object[curr] = values[i], object), {})
//     });
// };

// let data;

// data = 'id, name\n55, Leen \n200, Alaa';
// console.log(convertCSV(data, ','))


// function extract_max(data, colName, delimiter = ",") {
//     const rows = convertCSV(data, delimiter);
//     let max = null;
//     rows.forEach(row => {
//         const current_value = Number(row[colName])
//         if (!max)
//             max = current_value
//         else {
//             if (max < current_value) {
//                 max = row[colName]
//             }
//         }
//     })
//     return max;
// }

// console.log(extract_max(data, 'id', ','))







// Given a sorted array of N elements, with the number 1 to N, suggest an algorithm 
// to scramble it in such a way that the i-th element will have
//  an equal probability to be in each index
// void permute(int[] arr) {
//     Random random = new Random();
//     for(int i = 0; i < arr.length(); i++) {
//     int j = random.nextInt(arr.length - i) + i;
//     int tmp = arr[i];
//     arr[i] = arr[j];
//     arr[j] = tmp;
//     }
//     }




// arr = ["Rana", "George", "Ben", "Mohammed"]
// function names(arr){
//     biggestNumber = arr.splice(" ")
//     // biggestNumber = length.arr
//     console.log(biggestNumber);
//     // length = arr.map
// }

// length = arr.map(function(word) {
//     // console.log(word.length);
//     secondLargestNumber = Math.max(word.length)
//     console.log(secondLargestNumber);
// })
// names(["Rana", "George", "Ben", "Mohammed"])



//password match
// var input = document.querySelector('input.keycharac');
// let letters = /^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$/
// function passwordCheck(user){
    
//     if (input != letters) {
//         alert("Please insert new password password")
//     }
// }

// input.addEventListener('keyup', function(e){
    
//     if (!e.key.match(letters)){
//          input.value = input.value.slice(0,-1);
//     }

// })


//cinema seats
// let cin_col= 3;
// let cin_row= 10;
// let cin_count= cin_col * cin_row;

// let reservedSeats = [[cin_col] [cin_row]]

// function cinemaSeats(reservedSeats){
//     firstLargestNumber = Math.max(...reservedSeats) 
//      index = reservedSeats.indexOf(firstLargestNumber)
     
//      if (reservedSeats = null){
//         let emptyseats = !reservedSeats
//         index = reservedSeats.indexOf(emptyseats)
    
//     }
// }

// console.log(cinemaSeats([[2,1],[1,8],[2,6]]));





// get a message and u need to crop it to be K characters
// const crop = (message, maxLength) => {
//     const part = message.substring(0, maxLength + 1);
//     return part.substring(0, part.lastIndexOf(" ")).trimEnd();
//   }
  
//   console.log(crop("The quick brown fox jumped over the fence", 19)+">");
//   console.log(crop("The quick brown fox jumped over the fence", 9)+">");
//   console.log(crop("The quick brown fox jumped over the fence", 8)+">");
//   console.log(crop("The              ", 6)+">");
//   console.log(crop("The quick ", 20)+">");



function brushCount(building)
{
    let brushStroke = 0;
    let height = 0;
    for(let i = 0; i < building.length; i++)
    {
        if(building[i] > height)
             brushStroke = brushStroke + (building[i] - height);
        height = building[i];
    }
    return brushStroke;
}

console.log(brushCount([1,3,2,1,2,1,5,3,3,4,2]))
console.log(brushCount([5,8]))
console.log(brushCount([1,1,1,1]))


function solution(A) {
    A.sort(function (a, b) {
        return a - b;
    })
    let ans = Number.MIN_SAFE_INTEGER;

    if (A.length == 2) return (A[1] - A[0]) / 2;
    for (let i = 0; i < A.length - 1; i++) {
        if (A[i + 1] - A[i] > 1) {
            ans = Math.max(ans, A[i + 1] - A[i]);
        }
    }
    return Math.floor(ans / 2);

}

