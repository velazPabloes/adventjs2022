def fitsInOneBox(boxes):
    #Input:Array con las dimensiones de la caja ({ l: 1, w: 1, h: 1 })
    #Output: True o false si es posible empaquetar una caja en otra
    ls = []
    #Lista con la suma de las dimensiones de cada caja
    for e in boxes:
        ls.append(sum(e.values()))
    indexMaxBox = ls.index(max(ls)) #Saca el mayor indice
    maxBox = boxes[indexMaxBox]     #Saca el mayor diccionario
    boxes.pop(indexMaxBox)
    i = 0
    while(i<len(boxes)):
        if((maxBox.get("l") > boxes[i].get("l")) & (maxBox.get("w") > boxes[i].get("w")) & (maxBox.get("h") > boxes[i].get("h"))):
            res = True
            maxBox = boxes[i]
            i+=1
        else: 
            res = False
            break
    return res

        



if __name__ == "__main__":
    boxes1= [ { "l": 3, "w": 3, "h": 3 }, { "l": 2, "w": 2, "h": 2 }, { "l" : 1, "w": 1, "h": 1 }]
    boxes2 = [ { "l" : 1, "w": 1, "h": 1 },  { "l": 3, "w": 1, "h": 3 }, { "l": 2, "w": 2, "h": 2 }]
    print(fitsInOneBox(boxes1))
    #print(boxes[0].values())