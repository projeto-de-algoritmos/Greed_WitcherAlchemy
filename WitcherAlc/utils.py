from models import *
from datetime import datetime

def knapsack_(ingredientes, capacidades):
    """
    Função de aplicação do Knapsack 
    (chama adicionar_ingrediente de frasco para poder verificar se é necessário fazer divisão de tamanho ou não)
    """
    frascos = []

    for capacidade_frasco in capacidades:
        frasco = Frasco(capacidade_frasco)

        # Ordena os ingredientes por maior valor / tamanho
        ingredientes_ordenados = sorted(ingredientes, key=lambda x: x.valor / x.tamanho, reverse=True)

        for ingrediente in ingredientes_ordenados:
            # Verifica se o ingrediente é usado (já acabou) ou não antes de alocar
            if not ingrediente.usado:
                frasco.adicionar_ingrediente(ingrediente)

        frascos.append(frasco)

    return frascos

def interval_scheduling(atividades):
    """
    Função de aplicação do Interval Scheduling
    """
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