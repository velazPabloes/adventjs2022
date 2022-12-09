#Funciones:
def createCube(size):
    #Input: Tamaño del adorno.
    #Output: String con el diseño del programa.
    triangleTop = "/"  + "\\"
    triangleBot = "\\" + "/"
    lTop = "_" + "\\" 
    lBot = "_/"
    res = ""
    lsLinesTop = []
    lsLinesBot = [] 
    for e in range(1, size + 1):    
        lineTop = (" "*(size-e)) + (triangleTop*e) + (lTop*size)
        lineBot = (" "*(size-e)) + (triangleBot*e) + (lBot*size)
        lsLinesTop.append(lineTop)
        lsLinesBot.append(lineBot)
    lsLinesTop.sort()
    lsLinesBot.sort(reverse=True)
    for e in lsLinesTop:
        res+=(e+"\n")
    for e in lsLinesBot:
        res+=(e+"\n")
    return res



if __name__ == "__main__":
    print(createCube(30))