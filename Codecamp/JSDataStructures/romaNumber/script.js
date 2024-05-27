const numberInput = document.getElementById("number");
const convertBtn = document.getElementById("convert-btn");
const output = document.getElementById("output")

const arabicToRoman = [
    { arabico: 1000, romano: "M" },
    { arabico: 900, romano: "CM" },
    { arabico: 500, romano: "D" },
    { arabico: 400, romano: "CD" },
    { arabico: 100, romano: "C" },
    { arabico: 90, romano: "XC" },
    { arabico: 50, romano: "L" },
    { arabico: 40, romano: "XL" },
    { arabico: 10, romano: "X" },
    { arabico: 9, romano: "IX" },
    { arabico: 5, romano: "V" },
    { arabico: 4, romano: "IV" },
    { arabico: 1, romano: "I" }
];

const decimalToRoman = (number) => {
    let romano = '';

    for (const { arabico, romano: valorRomano } of arabicToRoman) {
        while (number >= arabico) {
            romano += valorRomano;
            number -= arabico;
        }
    }

    return romano;
};

const convertNumber = () =>{
    if(!numberInput.value){
        output.innerText = "Please enter a valid number";
    }else if(numberInput.value >= 4000){
        output.innerText = "Please enter a number less than or equal to 3999";
    }else if(numberInput.value < 1){
        output.innerText = "Please enter a number greater than or equal to 1";
    }else{
        output.innerText = decimalToRoman(numberInput.value);
    }
};

convertBtn.addEventListener("click", convertNumber);