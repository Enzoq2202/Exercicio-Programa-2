#Jogo Paciência Acordeão
from funcoes import*
import colorama

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

baralho = cria_baralho()
baralho=list(set(baralho))
while possui_movimentos_possiveis(baralho):
    imprime_baralho(baralho)
    origem=int(input('Escolha uma carta (digite um número entre 1 e {}): '.format(len(baralho))))
    movim = lista_movimentos_possiveis(baralho, origem-1)
    if movim == []:
        print(f'A carta {baralho[origem-1]} não pode ser movida. Por favor, digite um número entre 1 e {len(baralho)}:')
    elif movim == [1]:
        baralho = empilha(baralho,origem-1,origem-2 )
    elif movim == [3]:
        baralho = empilha(baralho,origem-1,origem -4)
    else:
        print(f'Sobre qual carta você quer empilhar o {baralho[origem-1]}?')
        print(f'1. {extrai_cor(baralho[origem-2])}')
        print(f'2. {extrai_cor(baralho[origem-4])}')
        c = int(input('Digite o número de sua escolha (1-2):'))
        if c == 1:
            baralho = empilha(baralho,origem-1,origem -2)
        if c == 2:
            baralho = empilha(baralho,origem-1,origem -4)
if len(baralho) == 1:
    print('Você ganhou!')
else:
    print('Você Perdeu!') 




    