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
    C = {}

    for chave, valor in A.data.items():
        C[chave] = valor

    for chave, valor in B.data.items():
        if chave in C:
            C[chave] += valor
            if C[chave] == 0:
                del C[chave]
        else:
            C[chave] = valor

    return C

def mult_escalar(A, x):
    C = {}

    for chave, valor in A.data.items():
        C[chave] = valor * x

    return C

def mult(A, B):
    return

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

print('Valores não nulos de A:')
print(((chave, valor) for chave, valor in A.data.items()))
print('Valores não nulos de B:')
print(((chave, valor) for chave, valor in B.data.items()))
print('Valores não nulos de A+B:')
print(((chave, valor) for chave, valor in AmaisB.data.items()))
print('Valores não nulos de A * 3:')
print(((chave, valor) for chave, valor in Ax3.data.items()))
print('Valores não nulos de At:')
print(((chave, valor) for chave, valor in At.data.items()))

