const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");

canvas.width = 800;
canvas.height = 700;

const map = new Image();
map.src = "RED.png";


map.addEventListener("load", function(){
    ctx.drawImage(map, 0,0,960,540);
});

canvas.addEventListener("click", function(event){
    let x = event.offsetX;
    let y = event.offsetY;
    
    console.log(`X: ${x} and Y: ${y}`)

    ctx.fillStyle = "blue";
    ctx.beginPath();
    ctx.arc(x,y,5,0, Math.PI*2);
    ctx.fill();
    ctx.stroke();
});