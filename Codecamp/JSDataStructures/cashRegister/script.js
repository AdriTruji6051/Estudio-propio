const cashInput = document.getElementById("cash");
const changeDiv = document.getElementById("change-due");
const purchaseBtn = document.getElementById("purchase-btn")

let required = [];
let price = 19.5;
let cid = [
    ["PENNY", 0.5], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 0], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]
];

const divise = {
    "PENNY": 0.01,
    "NICKEL": 0.05,
    "DIME": 0.1,
    "QUARTER": 0.25,
    "ONE": 1,
    "FIVE": 5,
    "TEN": 10,
    "TWENTY": 20,
    "ONE HUNDRED": 100
}

const getChange = () =>{
    const cash = parseFloat(cashInput.value)

    if(cash < price || isNaN(cash)){
        alert("Customer does not have enough money to purchase the item");
        return
    }

    if(cash === price){
       changeDiv.innerHTML = "No change due - customer paid with exact cash";
        return
    }

    let change = Math.round((cash - price) * 100) / 100;
    change = calculateChange(change);

    if(change > 0){
        changeDiv.innerHTML = "Status: INSUFFICIENT_FUNDS";
    }else{
        const billsToShow = [...required];
        updateCid()

        changeDiv.innerHTML = `Status: ${isOpen() ? "OPEN" : "CLOSED"}`;
        
        billsToShow.forEach((val)=>{
            changeDiv.innerHTML += `
            <div>
                ${val[0]}: $${val[1]}
            </div>`;
            
        });
    }

    required = [];

}

const updateCid = () => {
    for(let i = cid.length -1, r = 0; i != -1 && r != required.length; i--){
        if(cid[i][0] === required[r][0]){
            const substract = Math.round( (cid[i][1] - required[r][1]) * 100 ) / 100;
            cid[i][1] = substract;
            r++;
        }  
    }
}

const isOpen = () => {
    const cashOnCind = cid.reduce((acc, val)=> acc + val[1],0);
    return cashOnCind > 0 ? true : false;
}

const calculateChange = (change) => {
    for(let i = cid.length -1; i != -1; i--){
        if(change === 0) break

        const coinValue = divise[cid[i][0]];
        const valueInRegister = cid[i][1];
        const avalible = Math.round(valueInRegister / coinValue);
        const billsRequired = parseInt(change / coinValue);

        if(coinValue > change) continue

        const substract = billsRequired <= avalible ? billsRequired * coinValue : avalible * coinValue;
        change = Math.round( (change - substract) * 100 ) / 100;
        if(substract > 0) required.push([cid[i][0], substract]);
    }

    return change;
}

purchaseBtn.addEventListener("click", getChange);
