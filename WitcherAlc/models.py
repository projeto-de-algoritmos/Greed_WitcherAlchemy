class Ingrediente:
    def __init__(self, nome, tamanho, propriedades):
        self.nome = nome
        self.tamanho = float(tamanho)
        self.propriedades = propriedades
        self.usado = False

    def usar(self):
        if not self.usado:
            self.usado = True
        else:
            print(f"O ingrediente {self.nome} já foi usado e não pode ser adicionado a mais de um frasco.")


class Frasco:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.espaco_livre = capacidade
        self.ingredientes = []

    def adicionar_ingrediente(self, ingrediente):
        if ingrediente.usado:
            print(f"O ingrediente {ingrediente.nome} já foi usado e não pode ser adicionado ao frasco.")
        elif ingrediente.tamanho <= self.espaco_livre:
            self.ingredientes.append(ingrediente)
            self.espaco_livre -= ingrediente.tamanho
            ingrediente.usar()
        #else:
            #print(f"O frasco não tem espaço suficiente para adicionar o ingrediente {ingrediente.nome}.")

    def mostrar_ingredientes(self):
        print(f"Ingredientes no frasco (capacidade: {self.capacidade} - espaço livre: {self.espaco_livre}):")
        if len(self.ingredientes) > 0:
            for ingrediente in self.ingredientes:
                print(ingrediente.nome)
        else:
            print("Nenhum ingrediente no frasco.")
        print()

