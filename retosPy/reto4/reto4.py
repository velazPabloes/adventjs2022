#Funcion:
def fitsInOneBox(boxes):
    #Input:Array con las dimensiones de la caja ({ l: 1, w: 1, h: 1 })
    #Output: True o false si es posible empaquetar una caja en otra.
    listTam = []
    #Lista con la suma de las dimensiones de cada caja
    for e in boxes:
        listTam.append(sum(e.values()))
    #Lista tam ordenada de mayor a menor:
    listTamOrd = sorted(listTam, reverse=True)
    #Lista con las cajas ordenadas por dimensiones:
    boxesOrd = [boxes[listTam.index(listTamOrd[i])] for i in range(len(listTam))]
    #Bucle para comprobar si una caja cabe en otra:
    for i  in range(1, len(boxesOrd)):
        if((boxesOrd[i].get("l") < boxesOrd[i-1].get("l")) & (boxesOrd[i].get("w") < boxesOrd[i-1].get("w")) & (boxesOrd[i].get("h") < boxesOrd[i-1].get("h"))):
            res = True
        else:
            res = False
            break
    return res

#Funcion Test:
def fitsInOneBox_Test(boxes):
    boxes1= [ { "l": 3, "w": 3, "h": 3 }, { "l": 2, "w": 2, "h": 2 }, { "l" : 1, "w": 1, "h": 1 }]
    boxes2 = [ { "l" : 1, "w": 1, "h": 1 },  { "l": 3, "w": 1, "h": 3 }, { "l": 2, "w": 2, "h": 2 }]
    print(fitsInOneBox(boxes1))#True
    print(fitsInOneBox(boxes2))#False
        



if __name__ == "__main__":
    boxes1= [ { "l": 3, "w": 3, "h": 3 }, { "l": 2, "w": 2, "h": 2 }, { "l" : 1, "w": 1, "h": 1 }]
    fitsInOneBox_Test()