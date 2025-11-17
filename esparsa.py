# Implementação da estrutura 1
# Represetnta a matriz esparsa como um dicionário que com chave (i,j) e valor o elemento na posição (i,j)
# Armazena apenas elementos não nulos da matriz

# **Todas as complexidades escritas aqui são a complexidade esperada**

# Classe geral que define a estrutura 1
class matriz_esparsa:
    # Inicia a matriz_esparsa com um dicionário de elementos não nulos em data
    def __init__(self, data):
        # Atribui o dicionário de elementos não nulos para o data da matriz_esparsa
        self.data = data # O(1)

    # Retorna o elemento no índice (i,j) da matriz self, caso não encontrar, retorna 0
    def acessar(self, i, j):
        return self.data.get((i,j), 0) # O(1)
    
    # Insere (ou atualiza se ja existir) um elemento na posição (i,j) da matriz self
    # se o valor for 0, remove(se ja existir) a chave do dicionário
    def inserir_atualizar(self, i, j, valor):
        if valor == 0: # O(1)
            if (i,j) in self.data: # O(1)
                del self.data[i,j] # O(1)
        self.data[i,j] = valor # O(1)
    
    # Transpõe a matriz self
    def transpor(self):
        return transposta(self) # O(1)

# Classe que representa a matriz transpostas
class transposta:
    def __init__(self, original):
        self.original = original

    def acessar(self, i, j):
        return self.original.acessar(j,i)
    
def soma(A, B):
    C = {} # O(1)

    for chave, valor in A.data.items(): #O(kA)
        C[chave] = valor #O(1)

    for chave, valor in B.data.items(): #O(kB)
        if chave in C: # O(1)
            C[chave] += valor #O(1)
            if C[chave] == 0: #O(1)
                del C[chave] #O(1)
        else:
            C[chave] = valor #O(1) 

    return matriz_esparsa(C) #O(1)

#O(kA + kB)

def mult_escalar(A, x):
    C = {}

    for chave, valor in A.data.items():
        C[chave] = valor * x

    return matriz_esparsa(C)

def mult(A, B):
    C = {}
    B_temp = {}

    for chave, valor in B.data.items():
        if not chave[0] in B_temp:
            B_temp[chave[0]] = []

        B_temp[chave[0]].append((chave[1], valor))
    
    for chave, valor in A.data.items():
        if chave[1] in B_temp:
            for j in B_temp[chave[1]]:
                C[chave[0], j[0]] = C.get((chave[0], j[0]), 0) + valor * j[1]
    
    return matriz_esparsa(C)