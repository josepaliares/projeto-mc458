import matriz_tradicional as mt
import estrutura1_dict as e1
import estrutura2_avl as e2
import gerador_esparsa as ge
import tradutores as t

from random import Random
Random = Random()

# Expoente do tamanho da matriz (10^n x 10^n)
# No mínimo 2 e no máximo 6
n = 3

# Para n < 4 :  0 = 0.01 , 1 = 0.05 , 2 = 0.1 , 3 = 0.2
# Para n >= 4 : 0 = 10^-(n+2) , 1 = 10^-(n+1) , 2 = 10^-(n)
esparsidade_idx = 1

# Número de vezes que cada função será testada para cada estrutura
num_testes = 100

#acesso, inserir/atualizar, transpor, mult_escalar, soma, mult
def testes(n, esparsidade_idx, num_testes):
    for i in range(num_testes):
        matriz1 = ge.gerar_matriz(n, esparsidade_idx)
        matriz2 = ge.gerar_matriz(n, esparsidade_idx)

        A_e1 = t.estrutura1(matriz1)
        A_e2 = t.estrutura2(matriz1)
        A_trad = t.tradicional(matriz1)

        B_e1 = t.estrutura1(matriz2)
        B_e2 = t.estrutura2(matriz2)
        B_trad = t.tradicional(matriz2)







