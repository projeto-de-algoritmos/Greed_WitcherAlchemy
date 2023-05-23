from models import *

def empacotar_ingredientes(ingredientes, capacidades):
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


def ordernar_frascos_por_tempo(frascos):
    frascos_ordenados = []

    # Criar uma lista de tuplas (inicio, fim) representando os intervalos de tempo de cada frasco
    intervalos = [(sum(ingrediente.tamanho for ingrediente in frasco.ingredientes), frasco) for frasco in frascos]

    # Ordenar os intervalos por fim crescente
    intervalos_ordenados = sorted(intervalos, key=lambda x: x[0])

    # Percorrer os intervalos ordenados e selecionar os frascos compatíveis
    fim_anterior = 0
    for intervalo in intervalos_ordenados:
        inicio, frasco = intervalo
        if inicio >= fim_anterior:
            frascos_ordenados.append(frasco)
            fim_anterior = inicio

    return frascos_ordenados
