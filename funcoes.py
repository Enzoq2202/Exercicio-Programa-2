#Cria Baralho
def cria_baralho():
    baralho=[]
    cartas=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    naipes=['♠','♥','♣','♦']
    for carta in cartas:
        for naipe in naipes:
            baralho.append(carta+naipe)
    return baralho 