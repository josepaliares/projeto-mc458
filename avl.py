# Classe que representa um nó da AVL
class Nodo_AVL:
    # Inicializa um nodo com índice i, coluna j e valor
    def __init__(self, i, j, valor):
        self.i = i                       # O(1)
        self.j = j                       # O(1)
        self.valor = valor               # O(1)
        self.esq = None                  # O(1)
        self.dir = None                  # O(1)
        self.altura = 1                  # O(1)

    # Retorna a altura de um nó, caso ele exista
    def get_altura(self, node):
        if node is None:
            return 0
        return node.altura               # O(1)

    # Atualiza a altura do nó atual
    def atualizar_altura(self):
        self.altura = 1 + max(self.get_altura(self.esq), self.get_altura(self.dir))  # O(1)

    # Retorna o fator de balanceamento do nó atual
    def fator_balanceamento(self):
        return self.get_altura(self.esq) - self.get_altura(self.dir)                 # O(1)

    # Rotação simples à direita
    def rotacao_dir(self):
        nova_raiz = self.esq             # O(1)
        temp = nova_raiz.dir             # O(1)
        nova_raiz.dir = self             # O(1)
        self.esq = temp                  # O(1)

        self.atualizar_altura()          # O(1)
        nova_raiz.atualizar_altura()     # O(1)

        return nova_raiz                 # O(1)

    # Rotação simples à esquerda
    def rotacao_esq(self):
        nova_raiz = self.dir             # O(1)
        temp = nova_raiz.esq             # O(1)
        nova_raiz.esq = self             # O(1)
        self.dir = temp                  # O(1)

        self.atualizar_altura()          # O(1)
        nova_raiz.atualizar_altura()     # O(1)

        return nova_raiz                 # O(1)

    # Rotação dupla esquerda-direita
    def rotacao_dir_dupla(self):
        self.esq = self.esq.rotacao_esq()  # O(1)
        return self.rotacao_dir()          # O(1)

    # Rotação dupla direita-esquerda
    def rotacao_esq_dupla(self):
        self.dir = self.dir.rotacao_dir()  # O(1)
        return self.rotacao_esq()          # O(1)

    # Verifica e aplica rotações necessárias
    def balancear(self):
        fb = self.fator_balanceamento()    # O(1)

        # Caso esquerda-esquerda
        if fb > 1 and self.esq.fator_balanceamento() >= 0:
            return self.rotacao_dir()      # O(1)

        # Caso esquerda-direita
        if fb > 1 and self.esq.fator_balanceamento() < 0:
            return self.rotacao_dir_dupla()  # O(1)

        # Caso direita-direita
        if fb < -1 and self.dir.fator_balanceamento() <= 0:
            return self.rotacao_esq()        # O(1)

        # Caso direita-esquerda
        if fb < -1 and self.dir.fator_balanceamento() > 0:
            return self.rotacao_esq_dupla()  # O(1)

        return self                         # O(1)

    # Insere (ou atualiza) um elemento na posição (i,j)
    def inserir(self, i, j, valor):
        # Inserção normal em ABB por ordem lexicográfica
        if i < self.i or (i == self.i and j < self.j):
            if self.esq is None:
                self.esq = Nodo_AVL(i, j, valor)   # O(1)
            else:
                self.esq = self.esq.inserir(i, j, valor)  # O(log k)
        elif i > self.i or (i == self.i and j > self.j):
            if self.dir is None:
                self.dir = Nodo_AVL(i, j, valor)   # O(1)
            else:
                self.dir = self.dir.inserir(i, j, valor)  # O(log k)
        else:
            # Caso (i,j) já exista, atualiza o valor
            self.valor = valor                      # O(1)
            return self                              # O(1)

        # Atualiza altura e balanceia
        self.atualizar_altura()                      # O(1)
        return self.balancear()                      # O(1)

    # Busca o nodo de índice (i,j)
    def buscar(self, i, j):
        if i == self.i and j == self.j:
            return self                               # O(1)

        if i < self.i or (i == self.i and j < self.j):
            if self.esq is None:
                return None
            return self.esq.buscar(i, j)              # O(log k)

        if self.dir is None:
            return None
        return self.dir.buscar(i, j)                  # O(log k)

    # Percorre a árvore inteira (in-order), usado em soma e multiplicação
    def inordem(self, lista):
        if self.esq:
            self.esq.inordem(lista)       # O(k)
        lista.append((self.i, self.j, self.valor))  # O(1)
        if self.dir:
            self.dir.inordem(lista)       # O(k)

