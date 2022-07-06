let form = document.forms[0].textbox;
console.log(form);

let listTasks = [];
let list = document.getElementsByClassName('listTasks')[0];

function addTask(event){
    event.preventDefault();
    if (form.value == null){
        return alert("fill input");
    }
    listTasks.push(form.value);
    console.log(listTasks);
    newText();
    // let div = document.createElement('div');
    // div.textContent=form.value;
    // list.appendChild(div);

   
}

function newText(){
list.innerHTML = '';
for (i = 0; i < listTasks.length; i++){
    let div = document.createElement('div');
    let cross = document.createElement('i');
    cross.classList.add("fa-solid");
    cross.classList.add("fa-circle-xmark");
    let checkbox = document.createElement('input');
    let span = document.createElement('span');
    checkbox.type = "checkbox";
    checkbox.style.left="left";
    span.textContent=listTasks[i];
    div.appendChild(checkbox);
    div.appendChild(cross);
    div.appendChild(span);

    list.appendChild(div);
    
    // console.log(list);
}
}

