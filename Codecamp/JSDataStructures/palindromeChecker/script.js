const textInput = document.getElementById('text-input');
const checkBtn = document.getElementById('check-btn');
const resultDiv = document.getElementById('result');

function cleanInputString(str) {
    const regex = /[^a-zA-Z0-9]/g;
    return str.replace(regex, '');
}

const isPalindrome = (cleanText, textLength) => {
    let first = 0;
    let last = textLength - 1;

    while(first !== textLength){
        if(cleanText[first] === cleanText[last]){

            if(first + 1 !== last) last--;
            first++;
    
            if(first === last){
                if(cleanText[first] === cleanText[last]) return true
                else return false
            }
        }else return false

    }
}

function checkPalindrome(){
    const text = textInput.value;
    
    if(text === ""){
        alert("Please input a value")
        return
    }

    const cleanText = cleanInputString(text).toLowerCase();
    const textLength = cleanText.length;

    if(textLength === 1){
        resultDiv.innerText = `${text} is a palindrome`;
    }else{
        if(isPalindrome(cleanText, textLength)) resultDiv.innerText = `${text} is a palindrome`;
        else resultDiv.innerText = `${text} is not a palindrome`;
    }

}

checkBtn.addEventListener('click', checkPalindrome);
console.log('Final');
