let form = document.getElementById('form');
let username = document.getElementById('username');
let email = document.getElementById('email');
let password = document.getElementById('password');
let password2 = document.getElementById('password2');

let usernameBool = false;
 let emailBool = false;
 let passwordBool = false;
 let password2Bool = false;



 //signing up
function signup(event){
    event.preventDefault();


    let username = document.getElementById('username').value;
    let email = document.getElementById('email').value;
    let password = document.getElementById('password').value;


    let user = {
      email: email,
      user: username,
      password: password
    }


    let json = JSON.stringify(user);
    localStorage.setItem('users', json);

    console.log(json);


}



//login in function
function loginFunction(e){
    e.preventDefault();
    let username = document.getElementById('username').value;
    let password = document.getElementById('password').value;

    let user = localStorage.getItem('users');
    let data = JSON.parse(user)||[];
    console.log(data);


    if (data.length == 0){
      return alert('not correct')
    }
    else if (data.length > 0){
      for (let i = 0; i < data.length; i++) {
        if(data[i].username == username && data[i].password==password){
          window.location.href = "http://127.0.0.1:5500/Week-3/TrelloAttempt/index.html";
          return;
        }
      }

    } else {
      alert("try again");
    }

}


//login in button
form.addEventListener('submit', (e) => {
    e.preventDefault();

    loginFunction(e);
});




//sign up button
form.addEventListener('submit', (e) => {
    e.preventDefault();

    checkInputs();
});



//check user input
function checkInputs(){
    let usernameValue = username.value.trim();
    let emailValue = email.value.trim();
    let passwordValue = password.value.trim();
    let password2Value = password2.value.trim();



    if (usernameValue === ''){
        setErrorFor(username, 'Username cannot be blank');

    } else {
        usernameBool = true;
        setSuccessFor(username);
    }


    if (emailValue === ''){
        setErrorFor(email, 'Email cannot be blank');

    } else {
        emailBool= true;
        setSuccessFor(email);
    }


    if (passwordValue === ''){
        setErrorFor(password, 'Password cannot be blank');

    } else {
        passwordBool = true;
        setSuccessFor(password);
    }


    if (password2Value === ''){
        setErrorFor(password2, 'Password cannot be blank');

    } else if (passwordValue !== password2Value){
        setErrorFor(password2, 'Passwords do not match');
    }
    else {
        password2Bool = true;
        setSuccessFor(password2);
    }



}


function setErrorFor(input, message){
    let formControl = input.parentElement;
    let small = formControl.querySelector('small');
    small.innerText = message;

    formControl.className = 'form-control error';
}



function setSuccessFor(input){
    let formControl = input.parentElement;
    formControl.className = 'form-control success';
    if (usernameBool === true && emailBool === true && passwordBool === true && password2Bool === true){
        // alert('Login succesful')
        window.location.href = "http://127.0.0.1:5500/Week-3/TrelloAttempt/login2.html";
    }
}