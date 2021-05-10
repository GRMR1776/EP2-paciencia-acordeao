import random
def cria_baralho():
    
    baralho_final = []

   
    valores_do_baralho = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    
    naipes_do_baralho = ['♠', '♥', '♦', '♣']

   
    for valor in valores_do_baralho:
        for naipe in naipes_do_baralho:
            
            baralho_final.append(valor + naipe)
    
    random.shuffle(baralho_final)
    return(baralho_final)
#print(cria_baralho())

def extrai_naipe (carta):
    naipes_do_baralho = ['♠', '♥', '♦', '♣']
    for valor in naipes_do_baralho:
        if valor in carta:
            return valor

def extrai_valor(carta):
    valores_do_baralho = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    for valor in valores_do_baralho:
        if valor in carta:
            return valor



def lista_movimentos_possiveis(baralho, posicao):
    movimentos = []
    
    carta = baralho[posicao]
    naipe = extrai_naipe(carta)
    valor = extrai_valor(carta)

    if posicao == 0:
        return movimentos
    elif posicao <= 2:

        naipe_1 = extrai_naipe(baralho[posicao - 1])
        valor_1 = extrai_valor(baralho[posicao - 1])
    
        if naipe == naipe_1 or valor == valor_1:
            return [1]
        else:
            return []
    
    else:
        naipe_1 = extrai_naipe(baralho[posicao - 1])
        valor_1 = extrai_valor(baralho[posicao - 1])

        naipe_3 = extrai_naipe(baralho[posicao - 3])
        valor_3 = extrai_valor(baralho[posicao - 3])
        if naipe == naipe_1 or valor == valor_1:
            movimentos.append(1)
        if naipe == naipe_3 or valor == valor_3:
            movimentos.append(3)
    return movimentos

def empilha(baralho, origem, destino):
    baralho[destino] = baralho[origem]
    baralho.pop(origem)
    return baralho

def possui_movimentos_possiveis(baralho):
    for i in range(len(baralho)):
        if lista_movimentos_possiveis(baralho, i) != []:
            return True
    return False



