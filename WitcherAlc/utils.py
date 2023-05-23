from models import *

def empacotar_ingredientes(ingredientes, capacidades):
    """
    Função que aplica o Knapsack, basicamente para cada frasco (de capacidade), faz a alocação dos ingredientes
    """
    frascos = []

    for capacidade_frasco in capacidades:
        frasco = Frasco(capacidade_frasco)

        for ingrediente in ingredientes:
            if not ingrediente.usado:
                frasco.adicionar_ingrediente(ingrediente)
                if frasco.espaco_livre == 0:
                    break

        frascos.append(frasco)

    return frascos
