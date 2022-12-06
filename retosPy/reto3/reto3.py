#Funcion:
def distributeGifts(packOfGifts, reindeers):
    #Input: 2 listas : 1 caja de regalos (cada regalo tiene un peso, el número de caracteres)
    #                  1 lista de renos (cada reno tiene un peso max, 2 veces el numero de caracteres).
    #Output: Número de cajas de regalos que puede llevar.
    heigthPresents = 0
    for e in packOfGifts:
        heigthPresents += len(e)
    
    limitReindeers = 0
    for i in reindeers:
        limitReindeers += (2*len(i))
    res = limitReindeers//heigthPresents if heigthPresents<limitReindeers else 0
    return res

#Funcion Test:
def distributeGifts_Test():
    packOfGifts = ["book", "doll", "ball"]
    reindeers = ["dasher", "dancer"]
    nBoxs = distributeGifts(packOfGifts, reindeers)
    print("Santa Claus puede entregar {} cajas de regalos.".format(nBoxs))
    

if __name__ == "__main__":
    distributeGifts_Test()

    