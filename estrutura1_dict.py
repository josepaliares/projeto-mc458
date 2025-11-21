# Implementação da estrutura 1
# Representa a matriz esparsa como um dicionário que com chave (i,j) e valor o elemento na posição (i,j)
# Armazena apenas elementos não nulos da matriz

# **Todas as complexidades escritas aqui são a complexidade esperada**

# Classe geral que define a estrutura 1
class matriz_esparsa_dict:
    # Inicia a matriz_esparsa com um dicionário de elementos não nulos em data
    def __init__(self, data):
        # Atribui o dicionário de elementos não nulos para o data da matriz_esparsa
        self.data = data # O(1)

    # Retorna o elemento no índice (i,j) da matriz self, caso não encontrar, retorna 0
    def acessar(self, i, j):
        return self.data.get((i,j), 0) # O(1)
        # Complexidade total: O(1)
    
    # Insere (ou atualiza se ja existir) um elemento na posição (i,j) da matriz self
    # se o valor for 0, remove(se ja existir) a chave do dicionário
    def inserir_atualizar(self, i, j, valor):
        if valor == 0: # O(1)
            if (i,j) in self.data: # O(1)
                del self.data[i,j] # O(1)
        self.data[i,j] = valor # O(1)
        # Complexidade total: O(1)
    
    # Transpõe a matriz self
    def transpor(self):
        return transposta(self) # O(1)
        # Complexidade total: O(1)
    
    # Multiplica a matriz self pelo escalar x
    def mult_escalar(self, x):
        # Se o escalar for 0, todos os elementos
        # do resultado serão 0, então não precisariamos
        # armazenar nada
        if x == 0:
            return None
        # Inicia um dicionário vazio
        C = {} # O(1)
        # Para cada par (chave, valor) em self
        for chave, valor in self.data.items(): # O(k)
            # C[chave] vai ser self[chave] multiplicado pelo escalar
            C[chave] = valor * x # O(1)
        # Retorna a matriz esparsa com o dicionário C
        return matriz_esparsa_dict(C) # O(1)
        # Complexidade total: O(k)
        
    # Como armazena apenas os elementos não nulos,
    # a complexidade do uso de memória é O(k)

# Classe que representa a matriz transpostas
class transposta:
    # Função de inicialização da tranposta
    # original se refere a matriz antes de transpor
    def __init__(self, original):
        self.original = original #O(1)

    # Reutiliza o acesso da matriz original, apenas trocando os índices
    def acessar(self, i, j):
        return self.original.acessar(j,i) # O(1)
    # Mantém o acesso em O(1)

# Soma as matrizes A e B
def soma(A, B):
    # Inicia um dicionário C, que será o resultado
    C = {} # O(1)
    # Copia todos os elementos de A para C
    for chave, valor in A.data.items(): #O(kA)
        C[chave] = valor #O(1)
    # Para cada par (chave, valor) em B
    for chave, valor in B.data.items(): #O(kB)
        # Se a chave já existir em C
        if chave in C: # O(1)
            # Adiciona em C[chave] o valor armazenado em B[chave]
            C[chave] += valor #O(1)
            # Se C[chave] + B[chave] for 0, não precisamos mais armazenar esse valor
            if C[chave] == 0: #O(1)
                # Removemos C[chave] do dicionário
                del C[chave] #O(1)
        # Se a chave não existir em C
        else:
            # Atribui o valor de B[chave] em C[chave]
            C[chave] = valor #O(1) 
    # Retorna a a matriz_esparsa com o dicionário C
    return matriz_esparsa_dict(C) #O(1)
    # Complexidade total: O(kA + kB)

# Multiplica as matrizes A e B
def mult(A, B):
    # Inicia um dicionário vazio C, que será o resultado
    C = {} # O(1)
    # Inicia um dicionário vazio B_temp, que vai ajudar a
    # fazer as multiplicações
    B_temp = {} # O(1)

    # Para cada par (chave, valor) em B
    for chave, valor in B.data.items(): # O(kB)
        # Se a chave ainda não existir em B_temp
        if not chave[0] in B_temp: # O(1)
            # Iniciamos B_temp na posição chave[0] 
            # como uma lista vazia
            # (como chave armazena (i,j), chave[0] é i)
            B_temp[chave[0]] = [] # O(1)
        # Adicionamos em B_temp[chave[0]], um par (chave[1], valor)
        # como chave armazena (i,j), chave[1] é j
        B_temp[chave[0]].append((chave[1], valor)) # O(1)
        # Dessa forma, B_temp vai ter uma chave i para cada linha que tem elementos
        # não nulos, e em cada chave i, terá uma lista de pares (j, valor) representando
        # a coluna, e o valor armazenado dos elementos

    # Para cada par (chave, valor) em A
    for chave, valor in A.data.items(): # O(kA)
        # Se o j de A[chave], for uma chave de B_temp
        # Ou seja, se para a coluna do elemento em A, 
        # exisitir uma linha não nula em B
        if chave[1] in B_temp: # O(1)
            # Para cada elemento dessa linha não nula em B
            for j_valor in B_temp[chave[1]]: # O(dB)
                # Somamos em C[chave[0], j_valor[0]] o valor atual
                # + o valor armazenado em A[chave] * o valor armazenado
                # em B_temp[chave[1]]
                C[chave[0], j_valor[0]] = C.get(chave[0], j_valor[0]) + valor * j_valor[1] # O(1)
    # Retorna a a matriz_esparsa com o dicionário C
    return matriz_esparsa_dict(C) # O(1)
    # Complexidade total: O(kA * dB)