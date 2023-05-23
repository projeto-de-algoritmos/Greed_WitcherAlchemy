class Ingrediente:
    """
    Classe que representa ingredientes, que possuem uma propriedade interessante para os personagens.
    Eles também possuem sua quantidade disponível, um tamanho e um valor de importância para aplicação do Knapsack.
    """
    def __init__(self, nome, tamanho, propriedades):
        self.nome = nome
        self.tamanho = tamanho
        self.propriedades = propriedades
        self.usado = False

    def usar(self):
        """
        Função que retorna se o ingrediente foi usado ou não (se não, é usado).
        """
        if not self.usado:
            self.usado = True
        else:
            print(f"O ingrediente {self.nome} já foi usado e não pode ser adicionado a mais de um frasco.")


class Frasco:
    """
    Classe que representa um frasco que guarda os ingredientes.
    Possui uma capacidade e guarda o espaço livre e os ingredientes que estão no frasco.
    """
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.espaco_livre = capacidade
        self.ingredientes = []

    def adicionar_ingrediente(self, ingrediente):
        """
        Adiciona um ingrediente ao fraso (verifica tamanho e se já foi usado).
        """
        if ingrediente.usado:
            print(f"O ingrediente {ingrediente.nome} já foi usado e não pode ser adicionado ao frasco.")
        elif ingrediente.tamanho <= self.espaco_livre:
            self.ingredientes.append(ingrediente)
            self.espaco_livre -= ingrediente.tamanho
            ingrediente.usar()
        else:
            print(f"O frasco não tem espaço suficiente para adicionar o ingrediente {ingrediente.nome}.")

    def mostrar_ingredientes(self):
        """
        Mostra os ingredientes que estão em um frasco.
        """
        print(f"Ingredientes no frasco (capacidade: {self.capacidade} - espaço livre: {self.espaco_livre}):")
        if len(self.ingredientes) > 0:
            for ingrediente in self.ingredientes:
                print(ingrediente.nome)
        else:
            print("Nenhum ingrediente possível no frasco.")
        print()

