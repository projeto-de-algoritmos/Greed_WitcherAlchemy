from Greed_WitcherAlchemy.WitcherAlc.models import *
from Greed_WitcherAlchemy.WitcherAlc.utils import *
from Greed_WitcherAlchemy.WitcherAlc.data import *

if __name__ == "__main__":
    # Solicita ao jogador o número de frascos disponíveis
    numero_frascos = int(input("Digite o número de frascos disponíveis: "))

    # Solicita ao jogador a capacidade de cada frasco
    capacidades = []

    for i in range(numero_frascos):
        capacidade_frasco = int(input(f"Digite a capacidade do frasco {i+1} em unidades: "))
        capacidades.append(capacidade_frasco)

    # Empacotamento dos ingredientes nos frascos (Knapsack)
    frascos = empacotar_ingredientes(ingredientes, capacidades)

    # Mostrar os ingredientes em cada frasco
    for i, frasco in enumerate(frascos):
        print(f"Frasco {i + 1}:")
        frasco.mostrar_ingredientes()