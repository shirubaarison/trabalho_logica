import numpy as np
import matplotlib.pyplot as plt
import json
import Instancia
import utils_grafico as gra
from concurrent.futures import ProcessPoolExecutor, as_completed

def processar(a, n, k, qtd_instancias):
  m = int(a * n)
  # Vetor para calcular as probabilidades das instâncias
  v = [] # [True, False, True, ...]

  # Gerar instâncias e cláusulas e resolvê-las
  for _ in range(qtd_instancias):
      instancia = Instancia()
      instancia.gerar_clausulas(n, m, k)
      v.append(instancia.resolva_clausulas())

  # Calcular a porcentagem de probabilidade
  prob = round((sum(v) / len(v)) * 100)
  tempo = instancia.get_time()
  return a, n, prob, tempo


def executar(k: int, qtd_instancias, a_lim, valores_n):
  resultados = {} # dicionário com a cara {a: {prob: prob, tempo: tempo}]}
  
  # Usando processamento paralelo (máximo de 16 processos)
  with ProcessPoolExecutor(max_workers=16) as executor:
    futures = []
    for a in np.arange(0.1, a_lim, 0.1): # Tive que usar numpy para ir incrementando de 0.1
      a = round(a, 1) # Deixar a com uma casa decimal para q no json fique certinho
      for n in valores_n:
        futures.append(executor.submit(processar, a, n, k, qtd_instancias))

    for future in as_completed(futures):
        a, n, prob, tempo = future.result()
        if a not in resultados:
            resultados[a] = {}
        resultados[a][n] = {'prob': prob, 'tempo': tempo}
        print(f'{k}-SAT a = {a:.1f}, n = {n}: {prob}%')

  return resultados


def salvar_resultado(resultado, k: int):
  caminho = f'data/{k}_sat_result.json'

  with open(caminho, 'w') as file:
     json.dump(resultado, file)
  print(f"Resultados salvos em: {caminho}")


def ler_resultados(k: int):
  caminho = f'data/{k}_sat_result.json'
  with open(caminho, 'r') as file:
    resultado = json.load(file)

    resultado = {float(a): {int(n): v for n, v in subdict.items()} for a, subdict in resultado.items()}
  
  return resultado

def main():
  # Tamanhos de n
  n_instancias_3 = [50, 100, 150, 200]
  n_instancias_5 = [20, 30, 40, 50]

  # Alphas
  a_3 = 10
  a_5 = 30

  # qtd_instancias = 30
  # # Executar dois processos um para 3-SAT e outro para 5-SAT ao mesmo tempo
  # with ProcessPoolExecutor(max_workers=2) as executor:
  #   futures = []
  #   futures.append(executor.submit(executar, 3, qtd_instancias, a_3, n_instancias_3))
  #   futures.append(executor.submit(executar, 5, qtd_instancias, a_5, n_instancias_5))

  #   for future in as_completed(futures):
  #     resultados = future.result()
  #     if future == futures[0]:        # 0 é os 3-SAT
  #       salvar_resultado(resultados, 3)
  #       gra.construir_grafico_prob(3, resultados, n_instancias_3)
  #       gra.construir_grafico_tempo(3, resultados, n_instancias_3)
  #     else:
  #       salvar_resultado(resultados, 5)
  #       gra.construir_grafico_prob(5, resultados, n_instancias_5)
  #       gra.construir_grafico_tempo(5, resultados, n_instancias_5)
  resultados = ler_resultados(3)
  
  gra.construir_grafico_prob(3, resultados, n_instancias_3)
  gra.construir_grafico_tempo(3, resultados, n_instancias_3)


if __name__ == "__main__":
  main()
