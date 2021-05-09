#Cria Baralho
def cria_baralho():
    baralho=[]
    cartas=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    naipes=['♠','♥','♣','♦']
    for carta in cartas:
        for naipe in naipes:
            baralho.append(carta+naipe)
    return baralho 
# Extrai Naipe de Carta
def extrai_naipe(carta):
    return carta[-1]
# Extrai valor da carta
def extrai_valor(carta):  
    return carta[:-1]
# Empilha carta no Paciência Acordeão
def empilha(baralho,origem,destino):
    baralho[destino] = baralho[origem]
    del(baralho[origem])
    return baralho