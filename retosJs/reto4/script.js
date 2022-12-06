//PASOS:
//1-Sacar la lista con los pesos de cada array.
//2-Meter en un array nuevo los elementos por orden segun el peso.
//3-Comprobar si el primero cabe en el segundo y este en el tercero y asi sucesivamente.

//DECLARACION DE LA FUNCION:
function fitsInOneBox(boxes){
    //Variables:
    let res; //True o False
    let tamBox; //Suma de las propiedades de cada array
    let listTam; //Lista con todos los tamaños
    let listAux = []; //Lista aux para ordenar la listTam
    let listTamOrd; //Lista con los tamaños ordenados
    let boxesOrd = []; //Array de las cajas ordenadas

    //funcion para sacar los tamaños:
    listTam = boxes.map(function(box){return Object.values(box).reduce((a,b) => a+b,0)});  
    listTam.forEach(e => {listAux.push(e)});
    listTamOrd = listAux.sort().reverse();
    //Bucle para sacar el array ordenado por tamaño:
    for (let i = 0; i < listTam.length; i++) {
        let tamIndex = listTam.indexOf(listTamOrd[i])
        boxesOrd.push(boxes[tamIndex])
    }
    //Bucle para comprobar si cabe una caja dentro de la otra:
    for (let i = 1; i < boxesOrd.length; i++) {
        if((boxesOrd[i-1].l > boxesOrd[i].l) & (boxesOrd[i-1].w > boxesOrd[i].w) & (boxesOrd[i-1].h > boxesOrd[i].h)){
          res = true;
        }else{
          res = false;
          break;
        }
    }
    return res;
}
//Datos:
const boxes = [
    { l: 1, w: 1, h: 1 },
    { l: 2, w: 1, h: 2 },
    { l: 3, w: 3, h: 3 }
  ]
//LLAMADA DE LA FUNCION:
console.log(fitsInOneBox([
    { l: 1, w: 1, h: 1 },
    { l: 3, w: 3, h: 3 },
    { l: 2, w: 2, h: 2 }
]))