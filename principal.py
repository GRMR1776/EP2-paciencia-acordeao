from funcoes import *



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
while continuar:
    baralho = cria_baralho()
    while possui_movimentos_possiveis(baralho):
        #TODO
    if len(baralho) <= 1:
        print('WON')
    else:
        print('you lose')











