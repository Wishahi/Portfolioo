// const container = document.getElementById("container");

// function makeRows(rows, cols) {
//   container.style.setProperty('--grid-rows', rows);
//   container.style.setProperty('--grid-cols', cols);
//   for (c = 0; c < (rows * cols); c++) {
//     let cell = document.createElement("div");
//     // cell.innerText = (c);
//     container.appendChild(cell).className = "grid-item";
//   };
// };

// makeRows(200, 200);

// console.log('hello');
let color_col= 3;
let color_row= 8;
let color_count= color_col * color_row;

let main_col = 60;
let main_row = 50;
let main_count = main_col * main_row;
let color = '';
let mousedown= false;



let sidebar = document.getElementById('sidebar');
let main = document.querySelector('#main');


//sidebar
for (let i = 0; i < color_count; i++){
    let div = document.createElement('div');
    div.style.backgroundColor = generateRandomColor();
    div.addEventListener('click', function(event){
        color = div.style.backgroundColor;
        console.log(color);
    })
    sidebar.appendChild(div);

}

document.body.addEventListener('mousedown', function(event){
    mousedown = true;
})

document.body.addEventListener('mouseup', function(event){
    mousedown = false;
})

//main grid
for (let i = 0; i < main_count; i++){
    let div = document.createElement('div');
    main.appendChild(div);
    div.addEventListener('mouseover', function(event){
        if (mousedown){
        div.style.backgroundColor = color;
        
        console.log(color);
        }
    })


}


function generateRandomColor(){
    let letters = '0123456789ABCDEF' //16
 color = '#';
    for (let i = 0; i < 6; i++){
        color += letters[Math.floor(Math.random()*16)]

    }
    return color;

}

// let userDrawing= false;



// div.style.color
// sidebar.addEventListener('mousedown', startDrawing);
// main.addEventListener('mouseup', stopDrawing);
// main.addEventListener('mousemove', draw);

// function startDrawing(event){
//     userDrawing = true;
//     context.beg




