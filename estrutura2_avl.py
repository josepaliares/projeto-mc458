
from avl import *

# Classe geral da estrutura 2
class matriz_esparsa_AVL:
    # Inicializa a matriz com raiz None (árvore vazia)
    def __init__(self, raiz=None):
        self.raiz = raiz   # O(1)

    # Acessa elemento na posição (i,j)
    def acessar(self, i, j):
        if self.raiz is None:
            return 0
        nodo = self.raiz.buscar(i, j)   # O(log k)
        if nodo is None:
            return 0
        return nodo.valor               # O(1)
        # Complexidade total: O(log k)

    # Insere ou atualiza elemento
    def inserir_atualizar(self, i, j, valor):
        if valor == 0:
            # Remoção não é necessária no projeto
            # Mantemos como não fazer nada
            return                       # O(1)

        if self.raiz is None:
            self.raiz = Nodo_AVL(i, j, valor)   # O(1)
        else:
            self.raiz = self.raiz.inserir(i, j, valor)  # O(log k)
        # Complexidade total: O(log k)

    # Transposição O(1) como view
    def transpor(self):
        return transposta(self)   # O(1)
        # Complexidade total: O(1)

    # Multiplicação por escalar
    def mult_escalar(self, x):
        if x == 0:
            return matriz_esparsa_AVL()       # O(1)

        elementos = []
        if self.raiz:
            self.raiz.inordem(elementos)      # O(k)

        nova = matriz_esparsa_AVL()
        for (i, j, v) in elementos:           # O(k)
            nova.inserir_atualizar(i, j, v * x)  # O(log k)

        return nova
        # Complexidade total: O(k log k)

# Classe da transposta como view
class transposta:
    def __init__(self, original):
        self.original = original    # O(1)

    def acessar(self, i, j):
        return self.original.acessar(j, i)   # O(log k)
        # Complexidade total: O(log k)


# Soma de matrizes AVL
def soma(A, B):
    # Constrói árvore resultado como cópia de B
    elementos_B = []
    if B.raiz:
        B.raiz.inordem(elementos_B)         # O(kB)

    res = matriz_esparsa_AVL()
    for (i, j, v) in elementos_B:           # O(kB)
        res.inserir_atualizar(i, j, v)      # O(log kB)

    # Soma os elementos de A
    elementos_A = []
    if A.raiz:
        A.raiz.inordem(elementos_A)         # O(kA)

    for (i, j, v) in elementos_A:           # O(kA)
        atual = res.acessar(i, j)           # O(log k)
        novo = atual + v                    # O(1)
        if novo != 0:
            res.inserir_atualizar(i, j, novo)  # O(log k)
    # Complexidade total: O((kA + kB) log k)

    return res


# Multiplicação A × B
def mult(A, B):
    if A.raiz is None or B.raiz is None:
        return matriz_esparsa_AVL()          # O(1)

    # Transpõe B uma vez
    BT = B.transpor()                        # O(1)

    elementos_A = []
    A.raiz.inordem(elementos_A)              # O(kA)

    C = matriz_esparsa_AVL()

    # Para cada (i,k) em A
    for (i, k, aval) in elementos_A:         # O(kA)
        # Buscar elementos da linha k em BT (equivalente a coluna k de B)
        elementos_linha = []
        if B.raiz:
            buscar_linha_BT(B.raiz, k, elementos_linha)  # O(dB)

        # Para cada (k,j)
        for (_, j, bval) in elementos_linha:             # O(dB)
            prod = aval * bval                           # O(1)
            atual = C.acessar(i, j)                      # O(log k)
            C.inserir_atualizar(i, j, atual + prod)      # O(log k)

    # Complexidade total: O(kA * dB * log k)
    return C


# Busca apenas os elementos de linha k na árvore
def buscar_linha_BT(node, k, lista):
    if node is None:
        return

    if k < node.i:
        buscar_linha_BT(node.esq, k, lista)
    elif k > node.i:
        buscar_linha_BT(node.dir, k, lista)
    else:
        # Encontrou a linha k, agora pega todos da linha
        coletar_mesma_linha(node, k, lista)


def coletar_mesma_linha(node, k, lista):
    if node is None:
        return
    if node.i == k:
        lista.append((node.i, node.j, node.valor))      # O(1)
        coletar_mesma_linha(node.esq, k, lista)          # O(dB)
        coletar_mesma_linha(node.dir, k, lista)          # O(dB)
