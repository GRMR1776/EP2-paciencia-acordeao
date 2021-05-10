from funcoes import *

print('As 52 cartas de um baralho são embaralhadas e distribuídas em sequência. O objetivo do jogo é colocar todas as cartas em uma mesma pilha.\n')
print('Existem apenas dois movimentos possíveis:\n')
print('Empilhar uma carta sobre a carta imediatamente anterior:\n')
print('Empilhar uma carta sobre a terceira carta anterior.\n')
print('Para que um movimento possa ser realizado basta que uma das duas condições abaixo seja atendida:\n')
print('As duas cartas possuem o mesmo valor ou\n')
print('As duas cartas possuem o mesmo naipe.\n')
print('Desde que alguma das condições acima seja satisfeita, qualquer carta pode ser movimentada')
#iniciar

continuar = False
finalizar = False
while continuar != True and finalizar == False:
    inicio = input ('START? digite SIM ou NAO\n') 
    if inicio == 'SIM':
        continuar = True
    elif inicio =='NAO':
        finalizar = True
        print ('Até logo')



#movimentos posiveis 
'''while continuar:
    baralho = cria_baralho()
    while possui_movimentos_possiveis(baralho):
        #TODO
    if len(baralho) <= 1:
        print('WON')
    else:
        print('you lose')
'''









