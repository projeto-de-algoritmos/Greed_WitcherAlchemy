from models import *
from datetime import datetime

def knapsack_(ingredientes, capacidades):
    frascos = []

    for capacidade_frasco in capacidades:
        frasco = Frasco(capacidade_frasco)

        ingredientes_ordenados = sorted(ingredientes, key=lambda x: x.valor / x.tamanho, reverse=True)

        for ingrediente in ingredientes_ordenados:
            if not ingrediente.usado:
                frasco.adicionar_ingrediente(ingrediente)

        frascos.append(frasco)

    return frascos

def interval_scheduling(atividades):
    # Ordena as atividades pelo tempo de término em ordem crescente
    atividades.sort(key=lambda x: x.termino)

    atividades_selecionadas = []
    ultimo_termino = datetime.min

    for atividade in atividades:
        # Verifica se a atividade é compatível com as atividades já selecionadas
        if atividade.inicio >= ultimo_termino:
            atividades_selecionadas.append(atividade)
            ultimo_termino = atividade.termino

    return atividades_selecionadas