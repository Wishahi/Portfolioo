let startNumbertake = 1;
let bottles;
let noBottles;
// console.log('ppppp');
function beerSong(){
    let userinput = prompt ("Enter a number: ");
    let num = Number(userinput);
    //let startNumberbottles = 99;
    // console.log(num);


    for (let i = num; i >1; i-=startNumbertake){
        // console.log(i, startNumbertake);
        if (i == 1) {
            bottles = "bottle";
            noBottles = "No bottles of beer on the wall";
        }
        else {
            bottles = "bottles";
        // noBottles = (i-startNumbertake) + " bottles of beer on the wall"
        }
        //console.log(i+ " " + bottles + " of beer on the wall,");
        if(i > startNumbertake){
            console.log(i+ " " + bottles + " of beer,");
            console.log("Take " + takeOne() + " down, pass it around,");
            // console.log(noBottles);
            console.log((i-startNumbertake) + " bottles of beer on the wall");
        }
        else {
            console.log(i+ " " + bottles + " of beer,");
        console.log("Take " + i + " down, pass it around,");
        // console.log(noBottles);
        console.log((i) + " bottles of beer on the wall");
        }

    }
}
function takeOne(){
    let ret = 0
    for (let i = 0; i <= startNumbertake; i++ )
    {
         ret++;
        //console.log("Take "+ ret + " down, pass it around");
    }
    startNumbertake=ret
    return ret;
}


beerSong();

// function updateLyrics(item){
//     userinput[item]--;
//     //startNumberbottles[item]--;
//     startNumbertake[item]++;
// }

// console.log(userinput + " bottles of beer on the wall " + userinput + " bottles of beer" + " Take " + startNumbertake + 
// " one down, pass it around".repeat(updateLyrics));


