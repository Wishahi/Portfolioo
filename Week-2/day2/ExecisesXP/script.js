//Exercise 1
let x = 10;
let y = 3;

if (x>y) {
    console.log('x is the biggest number');
}
else if (x<y){
    console.log('y is the biggest number');
}


//Excercise 2
let newDog = 'Chihuahua';
console.log(newDog.length);
console.log(newDog.toUpperCase());
console.log(newDog.toLowerCase());
if (newDog=='Chihuahua') {
    console.log("I love Chihuahua, it's my favorite dog breed");
}
else {
    console.log("I dont care, I prefer cats")
}




//Exercise 3
let number = prompt("Enter a number: ");
if (number % 2 == 0) {
    console.log("The number is even")
}
else {
    console.log("The number is odd")
}



//Exercise 4
 let activeuser = prompt("Number of users ");
let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];
let newsfeed = [
            {users: 'Lea123', status:'online'},
            {users: 'Princess45', status: 'offline'},
            {users: 'doglovers', status: 'online'},
            {users: 'helooo@000', status: 'offline'},
            {users: 'koko', status: 'online'}
    
        ]

  if (activeuser ==0 ){
     console.log('No one is online')
 }
 if ( newsfeed[0].status == 'online' ){
    console.log(newsfeed[0].users,"is online");
}
 if ( newsfeed[1].status == 'online' ){
    console.log(newsfeed[1].users,"is online");
}
 if ( newsfeed[2].status == 'online' ){
    console.log(newsfeed[0].users, newsfeed[2].users,"are online");
}
 if ( newsfeed[4].status == 'online' ){
    console.log(newsfeed[0].users, newsfeed[4].users, "and", users.length-2, "are online" );
}
