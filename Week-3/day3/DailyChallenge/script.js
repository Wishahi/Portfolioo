var input = document.querySelector('input.keycharac');
// console.log(input);
specialChars = `\`!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?~`;
let letters = /^[A-Za-z]+$/
input.addEventListener('keyup', function(e){
    
    if (!e.key.match(letters)){
         input.value = input.value.slice(0,-1);
    }

})