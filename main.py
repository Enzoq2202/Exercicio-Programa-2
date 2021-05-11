#Jogo Paciência Acordeão
from funcoes import*


print('Paciência Acordeão ')
print('================== ')
print('')
print('Seja bem-vindo(a) ao jogo de Paciência Acordeão! O objetivo deste jogo é colocar todas as cartas em uma mesma pilha. ')
print('')
print('Existem apenas dois movimentos possíveis: ')
print('')
print('1. Empilhar uma carta sobre a carta imediatamente anterior; ')
print('2. Empilhar uma carta sobre a terceira carta anterior. ')
print('')
print('Para que um movimento possa ser realizado basta que uma das duas condições abaixo seja atendida: ')
print('')
print('1. As duas cartas possuem o mesmo valor ou ')
print('2. As duas cartas possuem o mesmo naipe. ')
print('')
print('Desde que alguma das condições acima seja satisfeita, qualquer carta pode ser movimentada. ')
print('')
input('Aperte [Enter] para iniciar o jogo...')

baralho=cria_baralho()
baralho=list(set(baralho))
while possui_movimentos_possiveis(baralho):
    imprime_baralho(baralho)
    a=int(input('digite a posição da carta que deseja mover:{1} a {len(baralho)}'.format(baralho)))

