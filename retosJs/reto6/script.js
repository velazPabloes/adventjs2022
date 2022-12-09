//DECLARACION DE LA FUNCION:
function createCube(size) {
    //Input: Tamaño del adorno.
    //Output: String con el diseño del programa.
    const triangleTop = "/"  + "\\";
    const triangleBot = "\\" + "/";
    const lTop = "_" + "\\"; 
    const lBot = "_/";
    let res = "";
    let lsLinesTop = [];
    let lsLinesBot = [];
    for(let e =1;e<=size;e++){
        let lineTop = (" ".repeat(size-e)) + (triangleTop.repeat(e)) + (lTop.repeat(size));
        let lineBot = (" ".repeat(size-e)) + (triangleBot.repeat(e)) + (lBot.repeat(size));
        lsLinesTop.push(lineTop);
        lsLinesBot.push(lineBot);
    }
    lsLinesTop.sort();
    lsLinesBot.sort().reverse();
    for(let e = 0; e<lsLinesTop.length;e++){
        res+=(lsLinesTop[e] +"\n");
    }
    for(let e = 0; e<lsLinesBot.length;e++){
        res+= e == (lsLinesBot.length-1)? (lsLinesBot[e]) : (lsLinesBot[e]+"\n");
    }
    return res;
}






//LLAMADA DE LA FUNCION:
console.log(createCube(3))