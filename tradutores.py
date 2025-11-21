# Inicia a estrutura1 com o dicionário data
def estrutura1(data):
    from estrutura1_dict import matriz_esparsa_dict
    
    return matriz_esparsa_dict(data) # O(1)

# Traduz o dicionário data para uma matriz_esparsa_AVL
def estrutura2(data):
    from estrutura2_avl import matriz_esparsa_AVL
    
    # Cria matriz AVL inicialmente vazia
    A = matriz_esparsa_AVL()    # O(1)
    
    # Para cada par (i,j) com valor não nulo
    for (i, j), valor in data.items():   # O(k)
        # Insere/atualiza na estrutura 2
        A.inserir_atualizar(i, j, valor)  # O(log k)
    
    # Retorna a matriz AVL
    return A

# Traduz o dicionário data para uma matriz_tradicional de tamanho n × n
def tradicional(data, n):
    from matriz_tradicional import matriz_tradicional

    # Cria uma matriz tradicional n × n preenchida com zeros
    A = matriz_tradicional(n, n)   # O(n²) para alocação

    # Para cada par (i,j) com valor não nulo em data
    for (i, j), valor in data.items():   # O(k)
        # Insere o valor correspondente na posição (i,j)
        A.inserir_atualizar(i, j, valor)  # O(1)

    # Retorna a matriz tradicional preenchida
    return A