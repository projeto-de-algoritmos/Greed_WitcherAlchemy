from pocoes import *

def empacotar_ingredientes(ingredientes, capacidade_frasco):
    n = len(ingredientes)

    dp = [[0] * (capacidade_frasco + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, capacidade_frasco + 1):
            ingrediente = ingredientes[i - 1]

            if ingrediente.tamanho <= j:
                dp[i][j] = max(ingrediente.tamanho + dp[i - 1][j - ingrediente.tamanho], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    frasco = Frasco(capacidade_frasco)

    i = n
    j = capacidade_frasco

    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            ingrediente = ingredientes[i - 1]
            frasco.adicionar_ingrediente(ingrediente)
            j -= ingrediente.tamanho
        i -= 1

    return frasco


# Criação dos ingredientes específicos de The Witcher
ingredientes = [
    Ingrediente("Erva Vermelha", 3, ["Vitalidade +10"]),
    Ingrediente("Cogumelo Bruxa", 2, ["Resistência a Veneno"]),
    Ingrediente("Esporos Fúngicos", 4, ["Invisibilidade temporária"]),
    Ingrediente("Sangue de Ghoul", 7, ["Regeneração de Vida"]),
    Ingrediente("Cauda de Grifo", 5, ["Força +5"]),
    Ingrediente("Olho de Basilisco", 6, ["Visão Noturna"]),
    Ingrediente("Escama de Dragão", 9, ["Resistência a Fogo"]),
    Ingrediente("Pétala de Sereia", 1, ["Respiração Subaquática"]),
    Ingrediente("Gema de Troll", 10, ["Regeneração Acelerada"]),
    Ingrediente("Garra de Quimera", 12, ["Velocidade +10"]),
]

# Solicita ao jogador o número de frascos disponíveis
numero_frascos = int(input("Digite o número de frascos disponíveis: "))

# Solicita ao jogador a capacidade de cada frasco
capacidades = []
for i in range(numero_frascos):
    capacidade_frasco = int(input(f"Digite a capacidade do frasco {i+1} em unidades: "))
    capacidades.append(capacidade_frasco)

# Empacotamento dos ingredientes nos frascos
frascos = []
for capacidade_frasco in capacidades:
    frasco = empacotar_ingredientes(ingredientes, capacidade_frasco)
    frascos.append(frasco)

# Mostrar os ingredientes em cada frasco
for i, frasco in enumerate(frascos):
    print(f"Frasco {i + 1}:")
    frasco.mostrar_ingredientes()
    print()
