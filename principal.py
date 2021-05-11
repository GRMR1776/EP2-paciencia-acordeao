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

#colorir
RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
YELLOW  = "\033[1;33m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"
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
while continuar:
    #baralho=['6♥', 'J♥', '9♣', '9♥']
    baralho = cria_baralho()
    while possui_movimentos_possiveis(baralho):
        print('O estado atual do baralho é:\n')
        for i in range(len(baralho)):
            if extrai_naipe(baralho[i])=="♥":
                carta2=RED+baralho[i]+RESET 
            elif extrai_naipe(baralho[i])=="♦":
                carta2=BLUE+baralho[i]+RESET 
            elif extrai_naipe(baralho[i])=="♣":
                carta2=GREEN+baralho[i]+RESET 
            elif extrai_naipe(baralho[i])=="♠":
                carta2=CYAN+baralho[i]+RESET 
            carta=str(i+1)+'. '+ carta2
            print(carta)
        posicao= int(input(f'escolha uma carta:(entre 1 e {len(baralho)})'))
        posicao=posicao-1
        possiveis_movimentos=lista_movimentos_possiveis(baralho, posicao)
        while possiveis_movimentos == []:
            if extrai_naipe(baralho[posicao])=="♥":
                carta2=RED+baralho[posicao]+RESET 
            elif extrai_naipe(baralho[posicao])=="♦":
                carta2=BLUE+baralho[posicao]+RESET 
            elif extrai_naipe(baralho[posicao])=="♣":
                carta2=GREEN+baralho[posicao]+RESET 
            elif extrai_naipe(baralho[posicao])=="♠":
                carta2=CYAN+baralho[posicao]+RESET 
            posicao= int(input(f'A carta {carta2} nao pode ser movida: escolha uma carta:(entre 1 e {len(baralho)}) '))
            posicao = posicao-1
            possiveis_movimentos=lista_movimentos_possiveis(baralho, posicao)
        if possiveis_movimentos == [1]:
            baralho = empilha(baralho, posicao, posicao-1)
        elif possiveis_movimentos == [3]:
            baralho = empilha(baralho, posicao, posicao-3)
        elif possiveis_movimentos == [1, 3]:
            print(f'Sobre qual carta vc deseja empilhar {baralho[posicao]}? ')
            print(f'1. {baralho[posicao -1]}')
            print(f'2. {baralho[posicao -3]}')

            escolha =  int(input('Digite (1 ou 2)'))
            if escolha == 1:
                baralho = empilha(baralho, posicao, posicao-1)
            elif escolha==2:
                baralho = empilha(baralho, posicao, posicao-3)
        
        #break
    #continuar=False

        #TODO
    if len(baralho) <= 1:
        print('WON')
    else:
        print('you lose')
    resposta= input("Você deseja continuar? (Digite S ou N)\n")
    if resposta== "N":
        continuar=False
        print("Até breve!")
    











