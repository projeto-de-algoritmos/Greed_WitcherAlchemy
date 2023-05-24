from models import *
from utils import *
from data import *

from flask import Flask, render_template, request

if __name__ == "__main__":
    # Solicita ao jogador o número de frascos disponíveis
    numero_frascos = int(input("Digite o número de frascos disponíveis: "))

    # Solicita ao jogador a capacidade de cada frasco
    capacidades = []
    for i in range(numero_frascos):
        capacidade_frasco = float(input(f"Digite a capacidade do frasco {i+1} em unidades: "))
        capacidades.append(capacidade_frasco)

    # Empacotamento dos ingredientes nos frascos
    frascos = empacotar_ingredientes(ingredientes, capacidades)

    # Ordenar os frascos por tempo total de preparação
    frascos_ordenados = ordernar_frascos_por_tempo(frascos)

    # Mostrar os ingredientes em cada frasco e a ordem de produção
    print("Ordem de produção dos frascos:")
    for i, frasco in enumerate(frascos_ordenados):
        print(f"Frasco {i + 1}:")
        frasco.mostrar_ingredientes()