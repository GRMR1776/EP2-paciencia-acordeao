from funcoes import *





continuar = False
finalizar = False
while continuar != True and finalizar == False:
    inicio = input ('START? digite SIM ou NAO') 
    if inicio == 'SIM':
        continuar = True
    elif inicio =='NAO':
        finalizar = True
        print ('GAME OVER')


