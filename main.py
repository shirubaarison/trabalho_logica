import numpy as np
from codigo import Instancia
from concurrent.futures import ProcessPoolExecutor, as_completed

VALORES_N = [50, 100, 150, 200]
N_INSTANCIAS = 30
LIM = 10.1
K = 3

def processar(a, n, k, N_INSTANCIAS):
    m = int(a * n)
    v = [] # [True, False, True, ...]

    # Gerar instâncias e cláusulas e resolvê-las
    for _ in range(N_INSTANCIAS):
        instancia = Instancia()
        instancia.gerar_clausulas(n, m, k)
        v.append(instancia.resolva_clausulas())

    # Calcular a porcentagem de probabilidade
    prob = round((sum(v) / len(v)) * 100)
    return a, n, prob

# Tentativa de processar concorrentemente com processos
def main():
  resultados = {}
  with ProcessPoolExecutor(max_workers=8) as executor:
      futures = []
      for a in np.arange(0.1, LIM, 0.1):
          for n in VALORES_N:
              futures.append(executor.submit(processar, a, n, K, N_INSTANCIAS))

      for future in as_completed(futures):
          a, n, prob = future.result()
          if a not in resultados:
              resultados[a] = {}
          resultados[a][n] = prob
          print(f'{K}-SAT a = {a:.1f}, n = {n}: {prob}%')


if __name__ == "__main__":
    main()
