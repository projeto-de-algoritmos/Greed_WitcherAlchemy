from pocoes import *


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
frascos = empacotar_ingredientes(ingredientes, capacidades)

# Mostrar os ingredientes em cada frasco
for i, frasco in enumerate(frascos):
    print(f"Frasco {i + 1}:")
    frasco.mostrar_ingredientes()

