import numpy as np
from codigo import Instancia

VALORES_N = [50, 100, 150, 200]
N_INSTANCIAS = 30
LIM = 10.1

k = 3    # k-Cláusulas
instancia = Instancia()
for a in np.arange(0.1, LIM, 0.1):
  for n in VALORES_N:
    m = int(a * n)

    v = []

    for i in range(N_INSTANCIAS):
      instancia.resetar()
      instancia.gerar_clausulas(n, m, k)
      v.append(instancia.resolva_clausulas())

    percent = round((sum(v) / len(v)) * 100)
    print(f'{k}-SAT a = {a:.1f}, n = {n}: {percent}%')