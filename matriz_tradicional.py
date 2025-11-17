class matriz_tradicional:

    # inicializa a matriz tradicional
    def __init__(self, linhas, colunas):
        self.linhas = linhas
        self.colunas = colunas
        self.data = [[0 for _ in range(colunas)] for _ in range(linhas)]

    # acessa o valor na posiçao (i, j)
    def acessar(self, i, j):
        return self.data[i][j]
    
    # insere ou atualiza o valor na posiçao (i, j)
    def inserir_atualizar(self, i, j, valor):
        self.data[i][j] = valor
    
    # retorna a transposta da matriz
    def transpor(self):
        matriz_transposta = matriz_tradicional(self.colunas, self.linhas)
        for i in range(self.linhas):
            for j in range(self.colunas):
                matriz_transposta.inserir_atualizar(j, i, self.acessar(i, j))
        return matriz_transposta
    

# realiza a soma de duas matrizes tradicionais A e B
def soma(A, B):
    # checa se as dimensões das matrizes são compatíveis para a soma
    if A.linhas != B.linhas or A.colunas != B.colunas:
        raise ValueError("As matrizes devem ter as mesmas dimensões para serem somadas.")

    matriz_soma = matriz_tradicional(A.linhas, A.colunas)

    for i in range(A.linhas):
        for j in range(A.colunas):
            valor_soma = A.acessar(i, j) + B.acessar(i, j)
            matriz_soma.inserir_atualizar(i, j, valor_soma)

    return matriz_soma

# realiza a multiplicação de uma matriz tradicional A por um escalar x
def mult_escalar(A, x):
    matriz_resultado = matriz_tradicional(A.linhas, A.colunas)
    if x == 0:
        return matriz_resultado
        
    for i in range(A.linhas):
        for j in range(A.colunas):
            valor_mult = A.acessar(i, j) * x
            matriz_resultado.inserir_atualizar(i, j, valor_mult)

    return matriz_resultado

# realiza a multiplicação de duas matrizes tradicionais A e B
def mult(A, B):
    # checa se as dimensões das matrizes são compatíveis para a multiplicação
    if A.linhas != B.colunas:
        raise ValueError("A matriz A deve ter numero de linhas igual ao numero de colunas da matriz B.")
    
    matriz_resultado = matriz_tradicional(A.linhas, B.colunas)

    for i in range(A.linhas):
        for j in range(B.colunas):
            soma = 0
            for k in range(A.colunas):
                soma += A.acessar(i, k) * B.acessar(k, j)
            matriz_resultado.inserir_atualizar(i, j, soma)

    return matriz_resultado

