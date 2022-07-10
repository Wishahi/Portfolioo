// console.log("hello");
let form = document.forms[0].textbox;

let listTasks = [];
let list = document.getElementsByClassName('to-do-list')[0];

function submitTask(event){
    event.preventDefault();
    if (form.value == null){
        return alert("Please add Task");
    }
    listTasks.push(form.value);
    console.log(listTasks);
    newText();
  }


function newText(){
    list.innerHTML = '';
    for (i = 0; i < listTasks.length; i++){
        let div = document.createElement('div');
        div.setAttribute("draggable", "true");
        div.setAttribute('id', "todolist"+i)
        let span = document.createElement('span');
        span.textContent=listTasks[i];
        div.appendChild(span);
        list.appendChild(div);

        div.addEventListener('dragstart', function(event){
            console.log(event.target, event.target.id);
            event.dataTransfer.setData('doing-square', event.target.id);
        
        })
       
    }
}
    
let todoSquare = document.getElementsByClassName('to-do-list')[0];
console.log(todoSquare);
let doingSquare = document.getElementsByClassName('doing-list')[0]; 
let doneSquare = document.getElementsByClassName('done-list')[0]; 

// doingSquare.addEventListener('dragstart', function(event){
//     console.log(event.target, event.target.id);
//     event.dataTransfer.setData('doing-square', event.target.id);

// })

todoSquare.addEventListener('dragover', function(event){
  event.preventDefault();
})

todoSquare.addEventListener('drop', function(event){
    event.preventDefault();
    console.log(event.target);
    let id = event.dataTransfer.getData('doing-square');
    let doingBox = document.getElementById(id);
    event.target.appendChild(doingBox);

})
doingSquare.addEventListener('dragover', function(event){
    event.preventDefault();
  })
  
  doingSquare.addEventListener('drop', function(event){
      event.preventDefault();
      let id = event.dataTransfer.getData('doing-square');
      let doingBox = document.getElementById(id);
      event.target.appendChild(doingBox);
  
  })
  doneSquare.addEventListener('dragover', function(event){
    event.preventDefault();
  })
  
  doneSquare.addEventListener('drop', function(event){
      event.preventDefault();
      let id = event.dataTransfer.getData('doing-square');
      let doingBox = document.getElementById(id);
      event.target.appendChild(doingBox);
  
  })