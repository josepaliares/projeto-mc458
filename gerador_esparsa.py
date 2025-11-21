from random import Random
Random = Random()

# Gera as matrizes recebendo parametros direto, facilita os testes
def gerar_matriz(expoente, esparsidade_idx):
    # Opções de esparsidade para matrices pequenas
    if expoente < 4:
        opcoes = [0.01, 0.05, 0.1, 0.2]
    # Opções de esparsidade para matrizes maiores
    else:
        opcoes = [10**(-(expoente+2)), 10**(-(expoente+1)), 10**(-expoente)]
    # A matriz vai ter lado de tamanho 10**expoente
    n = 10**expoente
    # Total de elementos
    total = n*n
    # Total de elementos não nulos
    k = int(total * opcoes[esparsidade_idx])
    # Inicia dicionário de elementos não nulos
    data = {}
    # Enquanto o tamanho do dicionário for menor que a quantia de elementos não nulos
    while len(data) < k:
        # Pega um i aleatório dentro das dimensões da matriz
        i = Random.randint(0, n-1)
        # Pega um j aleatório dentro das dimensões da matriz
        j = Random.randint(0, n-1)
        # Pega um valor inteiro aleatório entre 1 e 100
        val = Random.randint(1, 100)
        # Se ainda não existir valor em (i,j)
        if (i,j) not in data:
            # Adiciona o valor
            data[(i,j)] = val
    # Retorna o dicionário de elementos não nulos
    return data