from random import Random
Random = Random()

# Função auxiliar para receber a opção de esparcidade escolhida
def receber_esparcidade(opcoes_esparcidade):
    print("Grau de esparcidade:")
    for i, opcao in enumerate(opcoes_esparcidade):
        print(f"{i}: {opcao}")
    
    escolha = int(input("Escolha o grau de esparcidade da matriz: "))
    
    while escolha < 0 or escolha >= len(opcoes_esparcidade):
        print("Opção inválida. Tente novamente.")
        escolha = int(input("Escolha o grau de esparcidade da matriz: "))
    
    return opcoes_esparcidade[escolha]

# Função auxiliar para receber o tamanho da matriz
def receber_tamanho_matriz():

    tamanho = int(input("Digite o tamanho da matriz quadrada (10^n x 10^n): "))
    
    while tamanho < 2 or tamanho > 6:
        print("Tamanho inválido. Deve ser um número entre 2 e 6.")
        tamanho = int(input("Digite o tamanho da matriz quadrada (10^n x 10^n): "))
    
    return tamanho

# Função principal que gera a matriz esparsa
def gerador_matriz():
    # Recebe o tamanho informado
    tamanho_matriz = receber_tamanho_matriz()
    # Opções de esparcidade para matrizes com tamanho >= 2 e < 4
    opcao_esparcidade = [0.01, 0.05, 0.1, 0.2]
    # Opções de esparcidade para matrizes com tamanho >= 4 e < 7
    if tamanho_matriz >=4:
        opcao_esparcidade = [10**(-tamanho_matriz-4), 10**(-tamanho_matriz-3), 10**(-tamanho_matriz-2)]
    # O número de linhas vai ser 10^tamanho_matriz
    nmr_linhas = 10**tamanho_matriz
    # Recebe a opção de esparcidade escolhida
    esparcidade = receber_esparcidade(opcao_esparcidade)
    # Como a matriz é quadrada, o total vai ser nmr_linhas^2
    nmr_total_elementos = nmr_linhas * nmr_linhas
    # O número de valores não nulos será o grau de esparcidade * o total de elementos
    nmr_valores_nao_nulos = int(esparcidade * nmr_total_elementos)
    # Inicia o dicionário da estrutura 1
    lista_pontos_nao_nulos = {}
    # Enquanto ainda faltarem elemento não nulos para atingir o valor necessário
    while len(lista_pontos_nao_nulos) < nmr_valores_nao_nulos:
        # Pega um i aleatório dentro das dimensões da matriz
        i = Random.randint(0, nmr_linhas - 1)
        # Pega um j aleatório dentro das dimensões da matriz
        j = Random.randint(0, nmr_linhas - 1)
        # Pega um valor inteiro aleatório entre 1 e 100
        val = Random.randint(1, 100)
        # Se não existir elemento não nulo em (i,j)
        if (i, j) not in lista_pontos_nao_nulos:
            # Adiciona o valor gerado
            lista_pontos_nao_nulos[(i, j)] = val
    # Retorna o dicionário da estrutura 1 de pontos não nulos 
    return lista_pontos_nao_nulos

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