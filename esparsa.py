class matriz_esparsa:
    def __init__(self, data):
        self.data = data

    def acessar(self, i, j):
        return self.data.get((i,j), 0)
    
    def inserir_atualizar(self, i, j, valor):
        self.data[i,j] = valor
    
    def transpor(self):
        return transposta(self)

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
        if chave in C: #O(1)
            C[chave] += valor #O(1)
            if C[chave] == 0: #O(1)
                del C[chave] #O(1)
        else:
            C[chave] = valor #O(1)

    return matriz_esparsa(C) #O(kA + kB)

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

matriz1 = [[0,0,0,0,1],
     [0,2,0,0,3],
     [0,7,0,0,0],
     [1,0,0,0.3,0],
     [0,0,6,0,0]]

matriz2 = [[0,7,0,0,0],
     [0,1,0,0,0],
     [0,0,0,2,0],
     [-1,0,0,0,0],
     [0,0,9.2,0,0]]

dic1 = {}
dic2 = {}
A = matriz_esparsa(dic1)
B = matriz_esparsa(dic2)

for i in range(5):
    for j in range(5):
        if matriz1[i][j] != 0:
            A.inserir_atualizar(i,j,matriz1[i][j])
        if matriz2[i][j] != 0:
            B.inserir_atualizar(i,j,matriz2[i][j])

AmaisB = soma(A,B)
Ax3 = mult_escalar(A,3)
At = A.transpor()
AxB = mult(A, B)
