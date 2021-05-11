#Jogo Paciência Acordeão
from funcoes import*


baralho=cria_baralho()
baralho=list(set(baralho))
imprime_baralho(baralho)
for carta in baralho:
    int(input('digite a posição da carta que deseja mover:{1} a {len(cartas)}'.format(cartas)))

