from random import Random
Random = Random()

def receber_esparcidade(opcoes_esparcidade):
    """Recebe do usuário o grau de esparcidade desejado para a matriz."""

    print("Grau de esparcidade:")
    for i, opcao in enumerate(opcoes_esparcidade):
        print(f"{i}: {opcao}")
    
    escolha = int(input("Escolha o grau de esparcidade da matriz: "))
    
    while escolha < 0 or escolha >= len(opcoes_esparcidade):
        print("Opção inválida. Tente novamente.")
        escolha = int(input("Escolha o grau de esparcidade da matriz: "))
    
    return opcoes_esparcidade[escolha]


def receber_tamanho_matriz():
    """Recebe do usuário o tamanho desejado para a matriz quadrada."""

    tamanho = int(input("Digite o tamanho da matriz quadrada (10^n x 10^n): "))
    
    while tamanho < 2 or tamanho > 6:
        print("Tamanho inválido. Deve ser um número entre 2 e 6.")
        tamanho = int(input("Digite o tamanho da matriz quadrada (10^n x 10^n): "))
    
    return tamanho

def gerador_matriz():
    """Gera uma matriz esparsa e a salva em um arquivo de texto."""

    tamanho_matriz = receber_tamanho_matriz()

    opcao_esparcidade = [0.01, 0.05, 0.1, 0.2]

    if tamanho_matriz >=4:
        opcao_esparcidade = [10**(-tamanho_matriz-4), 10**(-tamanho_matriz-3), 10**(-tamanho_matriz-2)]

    nmr_linhas = 10**tamanho_matriz

    esparcidade = receber_esparcidade(opcao_esparcidade)

    nmr_total_elementos = nmr_linhas * nmr_linhas

    nmr_valores_nao_nulos = int(esparcidade * nmr_total_elementos)


    lista_pontos_nao_nulos = dict()
    while len(lista_pontos_nao_nulos) < nmr_valores_nao_nulos:
        i = Random.randint(0, nmr_linhas - 1)
        j = Random.randint(0, nmr_linhas - 1)
        
        val = Random.randint(1, 100)
        
        if (i, j) not in lista_pontos_nao_nulos:
            lista_pontos_nao_nulos[(i, j)] = val
    
    return tamanho_matriz, lista_pontos_nao_nulos, nmr_valores_nao_nulos


A = gerador_matriz()
for chave, valor in A[1].items():
    print(chave,valor)
print(A[2])