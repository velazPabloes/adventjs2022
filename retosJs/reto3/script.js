//DECLARACION DE LA FUNCION:
function distributeGifts(packOfGifts, reindeers) {
    /*
    Input: 2 listas : 1 caja de regalos (cada regalo tiene un peso, el número de caracteres)
                       1 lista de renos (cada reno tiene un peso max, 2 veces el numero de caracteres).
    Output: Número de cajas de regalos que puede llevar.*/
    let heigthPresent = packOfGifts.map(function(gift){return gift.length;}).reduce((a,b) => a+b ,0);
    let limitReindeers = reindeers.map(function(gift){return gift.length*2;}).reduce((a,b) => a+b ,0);
    let res =  limitReindeers>heigthPresent? Math.floor(limitReindeers/heigthPresent): 0;
    return(res);
    

}

//LLAMADA DE LA FUNCION:
packOfGifts = ["book", "doll", "ball"]
reindeers = ["dasher", "dancer"]
console.log(distributeGifts(packOfGifts, reindeers))

