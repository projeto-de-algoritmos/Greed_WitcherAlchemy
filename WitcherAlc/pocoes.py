class Ingrediente:
    def __init__(self, nome, tamanho, propriedades):
        self.nome = nome
        self.tamanho = tamanho
        self.propriedades = propriedades


class Frasco:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ingredientes = []

    def adicionar_ingrediente(self, ingrediente):
        self.ingredientes.append(ingrediente)

    def mostrar_ingredientes(self):
        for ingrediente in self.ingredientes:
            print(ingrediente.nome)

