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
#Lista Movimentos possíveis no paciência acordeão
def lista_movimentos_possiveis(baralho,i):
    if i==0:
        return []
    if i<=2:   
        if baralho[i][-1]==baralho[i-1][-1]:
            return [1]
        if baralho[i][:-1]==baralho[i-1][:-1]:
            return [1]
    else:
        if (baralho[i][-1]==baralho[i-1][-1] or baralho[i][:-1]==baralho[i-1][:-1]) and (baralho[i][-1]==baralho[i-3][-1] or baralho[i][:-1]==baralho[i-3][:-1]):
            return [1,3]
        if baralho[i][-1]==baralho[i-1][-1]:
            return [1]
        if baralho[i][:-1]==baralho[i-1][:-1]:
            return [1]
        if baralho[i][-1]==baralho[i-3][-1]:
            return [3]
        if baralho[i][:-1]==baralho[i-3][:-1]:
            return [3]
    return[]
# Possui movimentos
def possui_movimentos_possiveis(baralho):
    possui = False
    i = 0
    while i < len(baralho):
        if lista_movimentos_possiveis(baralho, i) != []:
            possui = True
        i += 1
    return possui

# Importando cores

import colorama
colorama.init(autoreset=True)


#novas funções

def imprime_baralho(baralho):
    i = 1
    for carta in baralho:
        if extrai_naipe(carta) == '♥':
            print(f'{i}. '+ colorama.Fore.RED + carta)
        if extrai_naipe(carta) == '♠':
            print(f'{i}. '+ colorama.Fore.BLUE + carta)
        if extrai_naipe(carta) == '♣':
            print(f'{i}. '+ colorama.Fore.GREEN + carta)
        if extrai_naipe(carta) == '♦':
            print(f'{i}. '+ colorama.Fore.MAGENTA + carta)
        i += 1
def extrai_cor(carta):
    if extrai_naipe(carta) == '♥':
        cor = colorama.Fore.RED
            
    if extrai_naipe(carta) == '♠':
        cor = colorama.Fore.BLUE
            
    if extrai_naipe(carta) == '♣':
        cor = colorama.Fore.GREEN
            
    if extrai_naipe(carta) == '♦':
        cor = colorama.Fore.MAGENTA
    return cor+carta
        
        
    

