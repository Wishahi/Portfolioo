// Change each first name of the two <ul>'s to your name.
// Delete the <li> that contains the text node “Sarah”.
// Bonus - Using Javascript:
// Add a class called student_list to both of the <ul>'s.
// Add the classes university and attendance to the first <ul>.

//Exercise 1
let x = document.getElementById('container');
console.log(x);
let y = document.getElementsByClassName('list')[0].lastElementChild.innerHTML= "Richard";
// console.log(y);

let a = document.getElementsByTagName('li')[0].innerHTML = "Leen";
let c = document.getElementsByTagName('li')[0,2].innerHTML = "Leen";
// console.log(a);


// let parent = document.getElementById('list');
// parent.removeChild(parent);
let myList = document.getElementsByTagName('ul');
let sarah = myList[1].children[1];
myList[1].removeChild(sarah);
// let remove = sarah.remove();

let element = document.getElementsByTagName('ul');
element.add





// Exercise 2

// let elem = document.getElementsByTagName('div');
// let john = elem[0].nextElementSibling.children[0];
// let remove = john.remove();







//Exercise 3
// let newDiv = document.getElementById("navBar");
// // newDiv.setAttribute('id', "socialNetworkNavigation");
// // console.log(newDiv);

// let li = document.createElement('li');
// li.textContent= 'Logout';
// newDiv.appendChild(li).innerHTML;
// document.querySelector('ul').appendChild(li);

// //BONUS
// let ul = document.querySelector('ul');
// let first = ul.firstElementChild.textContent;
// let last = ul.lastElementChild.textContent;
// console.log(first);
// console.log(last);


//Exercise 4
// let div = document.getElementsByClassName('listBooks');
// let table = document.createElement('table');
// div[0].appendChild(table);

// let allBooks = [
//     { title: 'Harry Potter',
//         author: 'JK Rowling',
//         image: src='images/harrypotter.jpg',
//         alreadyRead: false


//     },
//     { title: 'Animal Farm',
//         author: 'George Orwell',
//         image: src='images/animal.png',
//         alreadyRead: true
// }];

// for(x in allBooks){
  
//   if ( x==0 ){
//     let row = document.createElement('tr');
//   table.appendChild(row);
//     let headers = Object.keys(allBooks[x]);
//     for (i in headers) {
//         let column = document.createElement('td');
//         column.textContent=headers[i];
//         row.appendChild(column);

//     }
    
//   }
//   let row = document.createElement('tr');
//   table.appendChild(row);
//   let title = document.createElement('td');
//   title.textContent=allBooks[x].title;
//   row.appendChild(title);
//   let author = document.createElement('td');
//   author.textContent=allBooks[x].author;
//   row.appendChild(author);
//   let imgtd = document.createElement('td');
//   let img = document.createElement('img');
//   img.setAttribute("src", allBooks[x].image)
//   img.style.width="100px";
//   imgtd.appendChild(img);
//   row.appendChild(imgtd);
//   let read = document.createElement('td');
//   read.textContent=allBooks[x].alreadyRead;
//   row.appendChild(read);

// }
