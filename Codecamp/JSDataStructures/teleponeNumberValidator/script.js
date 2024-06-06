const clearBtn = document.getElementById("clear-btn");
const checkBtn = document.getElementById("check-btn");
const userInput = document.getElementById("user-input");
const result = document.getElementById("results-div");

const isValidNumber = (number) => {
    const phoneRegex = /^1?\s?(\d{3}|\(\d{3}\))\s?-?\d{3}-?\d{4}$/;
    return phoneRegex.test(number);
}

const validate = () => {
    const number = userInput.value
    if(!number){
        alert("Please provide a phone number")
        return
    }
    if(isValidNumber(number)){
        result.innerText = `Valid US number: ${number}`
    }else{
        result.innerText = `Invalid US number: ${number}`
    }
}

checkBtn.addEventListener("click", validate);

clearBtn.addEventListener("click", () => {
    result.innerText = "";
});