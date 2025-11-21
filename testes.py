import time
import csv

import matriz_tradicional as trad
import estrutura1_dict as e1
import estrutura2_avl as e2
import gerador_esparsa as ge
import tradutores as t

from random import Random
Random = Random()

def medir_tempo(func, *args, **kwargs):
    inicio = time.perf_counter_ns()
    func(*args, **kwargs)
    fim = time.perf_counter_ns()
    return fim - inicio   # tempo em nanossegundos

def gerar_csv(resultados, nome_arquivo):

    with open(nome_arquivo, "w", newline="") as arq:
        writer = csv.writer(arq)

        writer.writerow(["estrutura", "operacao", "min_ns", "max_ns", "media_ns"])

        for estrutura, ops in resultados.items():
            for op, tempos in ops.items():

                if len(tempos) == 0:
                    writer.writerow([estrutura, op, "-", "-", "-"])
                    continue

                mn = min(tempos)
                mx = max(tempos)
                media = sum(tempos) / len(tempos)

                writer.writerow([estrutura, op, mn, mx, media])

def inicializar_resultados():
    estruturas = ["E1", "E2", "TRAD"]
    operacoes = ["acesso", "inserir", "transpor", "mult_escalar", "soma", "mult"]
    return {e: {op: [] for op in operacoes} for e in estruturas}

def testes(expoente, esparsidade_idx, num_testes, saida_csv):

    resultados = inicializar_resultados()

    n = 10**expoente

    for _ in range(num_testes):
        # Gera duas matrizes esparsas aleatórias
        matriz1 = ge.gerar_matriz(expoente, esparsidade_idx)
        matriz2 = ge.gerar_matriz(expoente, esparsidade_idx)

        # Traduz as matrizes para cada estrutura
        A_e1 = t.estrutura1(matriz1)
        A_e2 = t.estrutura2(matriz1)
        A_trad = t.tradicional(matriz1, n)
        B_e1 = t.estrutura1(matriz2)
        B_e2 = t.estrutura2(matriz2)
        B_trad = t.tradicional(matriz2, n)
        
        # Índices aleatórios para os testes
        i = Random.randint(0, n-1)
        j = Random.randint(0, n-1)

        # Acesso
        resultados["E1"]["acesso"].append(
            medir_tempo(A_e1.acessar, i, j)
        )
        resultados["E2"]["acesso"].append(
            medir_tempo(A_e2.acessar, i, j)
        )
        resultados["TRAD"]["acesso"].append(
            medir_tempo(A_trad.acessar, i, j)
        )

        # Valor aleatório para inserir/atualizar
        val = Random.randint(1, 100)
        # Inserir/atualizar
        resultados["E1"]["inserir"].append(
            medir_tempo(A_e1.inserir_atualizar, i, j, val)
        )
        resultados["E2"]["inserir"].append(
            medir_tempo(A_e2.inserir_atualizar, i, j, val)
        )
        resultados["TRAD"]["inserir"].append(
            medir_tempo(A_trad.inserir_atualizar, i, j, val)
        )

        # Transpor
        resultados["E1"]["transpor"].append(
            medir_tempo(A_e1.transpor)
        )
        resultados["E2"]["transpor"].append(
            medir_tempo(A_e2.transpor)
        )
        resultados["TRAD"]["transpor"].append(
            medir_tempo(A_trad.transpor)
        )

        # Escalar aleatório para mult_escalar
        esc = Random.randint(1, 100)
        # Multiplicação por escalar
        resultados["E1"]["mult_escalar"].append(
            medir_tempo(A_e1.mult_escalar, esc)
        )
        resultados["E2"]["mult_escalar"].append(
            medir_tempo(A_e2.mult_escalar, esc)
        )
        resultados["TRAD"]["mult_escalar"].append(
            medir_tempo(A_trad.mult_escalar, esc)
        )

        # Soma de matrizes
        resultados["E1"]["soma"].append(
            medir_tempo(e1.soma, A_e1, B_e1)
        )
        resultados["E2"]["soma"].append(
            medir_tempo(e2.soma, A_e2, B_e2)
        )
        resultados["TRAD"]["soma"].append(
            medir_tempo(trad.soma, A_trad, B_trad)
        )

        # Multiplicação de matrizes
        resultados["E1"]["mult"].append(
            medir_tempo(e1.mult, A_e1, B_e1)
        )
        resultados["E2"]["mult"].append(
            medir_tempo(e2.mult, A_e2, B_e2)
        )
        resultados["TRAD"]["mult"].append(
            medir_tempo(trad.mult, A_trad, B_trad)
        )

        gerar_csv(resultados, saida_csv)

# Tamanho da matriz = 10^expoente x 10^expoente
expoente = 3 # No mínimo 2 e no máximo 6

# Para expoente < 4 : 0 = 0.01 , 1 = 0.05 , 2 = 0.1 , 3 = 0.2
# Para expoente >= 4 : 0 = 10^-(n+2) , 1 = 10^-(n+1) , 2 = 10^-(n)
esparsidade_idx = 1

num_testes = 10 # Número de vezes que cada função vai ser executada para cada estrutura

saida_csv = "resultados.csv" # Nome do arquivo para o qual vão os dados obtidos

testes(expoente, esparsidade_idx, num_testes, saida_csv)