function getFinalOpenedDoors(numDoors) {
    var iteration = numDoors;
    var openedDoors = new Set();
  
    for(var value = 2; iteration > 0; value++){
      for(var i = 1; value * i <= numDoors && iteration >= 0; i++){
        if(openedDoors.has(value * i)){
          openedDoors.delete(value * i);
        }else{
          openedDoors.add(value * i);
        }
        iteration--;
      }
    }
  
    return Array.from(openedDoors).sort((a,b) => a - b);
  }
  
  console.log(getFinalOpenedDoors(10));