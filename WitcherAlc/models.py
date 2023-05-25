class Ingrediente:
    """
    Classe que identifica ingrediente (tamanho e valor)
    """
    def __init__(self, nome, tamanho, valor, propriedades):
        self.nome = nome
        self.tamanho = float(tamanho)
        self.propriedades = propriedades
        self.valor = valor
        self.usado = False

    def usar(self):
        """
        Se todo o ingrediente já for usado
        """
        if not self.usado:
            self.usado = True
        else:
            print(f"O ingrediente {self.nome} já foi usado e não pode ser adicionado a mais de um frasco.")

class Frasco:
    """
    Classe que identifica frasco (capacidade)
    """
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.espaco_livre = capacidade
        self.ingredientes = []

    def adicionar_ingrediente(self, ingrediente):
        """
        Aplicação do Knapsack (verifica se tem que fracionar ou não)
        """
        if ingrediente.tamanho <= self.espaco_livre:
            self.ingredientes.append(ingrediente)
            self.espaco_livre -= ingrediente.tamanho
            ingrediente.usar()
        else:
            fracao = self.espaco_livre / ingrediente.tamanho
            
            ingrediente_fracionado = Ingrediente(ingrediente.nome, ingrediente.tamanho * fracao, ingrediente.valor * fracao, ingrediente.propriedades)
            self.ingredientes.append(ingrediente_fracionado)
            self.espaco_livre = 0
            
            ingrediente.tamanho = ingrediente.tamanho - ingrediente.tamanho * fracao


    def mostrar_ingredientes(self):
        """
        Mostra os ingredientes alocados ao frasco
        """
        print(f"Ingredientes no frasco (capacidade: {self.capacidade} - espaço livre: {self.espaco_livre}):")
        if len(self.ingredientes) > 0:
            for ingrediente in self.ingredientes:
                print(ingrediente.nome)
        else:
            print("Nenhum ingrediente no frasco.")
        print()

class Contrato:
    """
    Classe que identifica um contrato
    """
    def __init__(self, nome, descricao, inicio, termino):
        self.nome = nome
        self.descricao = descricao
        self.inicio = inicio
        self.termino = termino