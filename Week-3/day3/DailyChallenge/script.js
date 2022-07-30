var input = document.querySelector('input.keycharac');
// console.log(input);
specialChars = `\`!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?~`;
// let letters = /^[A-Za-z]+$/
let letters = /^(?=.*?[A-Z])(?=(.*[a-z]){1,})(?=(.*[\d]){1,})(?=(.*[\W]){1,})(?!.*\s).{8,}$/
input.addEventListener('keyup', function(e){
    
    if (!e.key.match(letters)){
         input.value = input.value.slice(0,-1);
    }

})