# Implementação da matriz tradicional, para futuras comparações
class matriz_tradicional:
    # Inicializa a matriz tradicional
    def __init__(self, linhas, colunas):
        self.linhas = linhas
        self.colunas = colunas
        self.data = [[0 for _ in range(colunas)] for _ in range(linhas)]

    # Acessa o valor na posiçao (i, j)
    def acessar(self, i, j):
        return self.data[i][j]
    
    # Insere ou atualiza o valor na posiçao (i, j)
    def inserir_atualizar(self, i, j, valor):
        self.data[i][j] = valor

    # Retorna a transposta da matriz
    def transpor(self):
        return transposta(self, self.linhas, self.colunas)
    
    # Realiza a multiplicação de uma matriz tradicional A por um escalar x
    def mult_escalar(self, x):
        # Inicia a matriz C que será o resultado
        C = matriz_tradicional(self.linhas, self.colunas)
        # Se o escalar for 0, todos os elementos serão 0
        if x == 0:
            # Retorna a matriz C vazia
            return C
        # Para cada linha de self
        for i in range(self.linhas):
            # Para cada coluna de self
            for j in range(self.colunas):
                # C[i][j] = self[i][j] * x
                valor_mult = self.acessar(i, j) * x
                C.inserir_atualizar(i, j, valor_mult)
        # Retorna a matriz resultante C
        return C

# Representação da transposta
class transposta:
    def __init__(self, original, linhas, colunas):
        self.linhas = colunas
        self.colunas = linhas
        self.original = original
    def acessar(self, i, j):
        return self.original.acessar(self.colunas, self.linhas)
    

# Realiza a soma de duas matrizes tradicionais A e B
def soma(A, B):
    # Inicia a matriz C que será o resultado
    C = matriz_tradicional(A.linhas, A.colunas)
    # Para cada linha de A
    for i in range(A.linhas):
        # Para cada linha de B
        for j in range(A.colunas):
            # C[i][j] = A[i][j] + B[i][j]
            valor_soma = A.acessar(i, j) + B.acessar(i, j)
            C.inserir_atualizar(i, j, valor_soma)
    # Retorna a matriz resultante C
    return C

# Realiza a multiplicação de duas matrizes tradicionais A e B
def mult(A, B):
    # Inicia a matriz C, que será o resultado
    C = matriz_tradicional(A.linhas, B.colunas)
    # Para cada linha i de A
    for i in range(A.linhas):
        # Para cada coluna j de B
        for j in range(B.colunas):
            soma = 0
            # Para cada coluna k de A
            for k in range(A.colunas):
                # Adiciona na soma, a multiplicação A[i][k] + B[k][j]
                soma += A.acessar(i, k) * B.acessar(k, j)
            # Depois de todas as somas, adiciona o valor em C[i][j]
            C.inserir_atualizar(i, j, soma)
    # Retorna a matriz resultante C
    return C

