import numpy as np
import utils.grafico as gra
import utils.io as io

from Instancia import Instancia
from concurrent.futures import ProcessPoolExecutor, as_completed
from utils.constants import *

def processar(a: float, n: int, k: int, qtd_instancias: int) -> tuple[float, int, float, float]:
  """Gera instâncias e resolve, retornando:
    - alpha
    - número de variáveis
    - probabilidade de ser satisfazível
    - tempo médio de resolução
  """
  m = int(a * n)
  v = []  # Lista de resultados (True/False)

  # Gerar instâncias com cláusulas e resolvê-las
  instancia = Instancia()
  for _ in range(qtd_instancias):
      instancia.gerar_clausulas(n, m, k)
      v.append(instancia.resolva_clausulas())
      instancia.resetar()

  # Calcular a porcentagem de probabilidade e tempo
  prob = round((sum(v) / len(v)) * 100)
  tempo_medio = round(instancia.get_time() / qtd_instancias, 2)
  
  return a, n, prob, tempo_medio


def executar(k: int, qtd_instancias: int, a_lim: float, valores_n: list[int]) -> None:
  """ Executa processos para resolução das instâncias. Salva em JSON e constroi os gráficos """
  
  resultados: dict[float, dict[int, dict[str, float]]] = {}
  #{
  #    a: {
  #     "prob": float
  #     "tempo": float
  #   }
  # }
  
  # 8 processos ao mesmo tempo
  with ProcessPoolExecutor(max_workers=8) as executor:
    futures = []
    # Tive que usar numpy para ir incrementando de 0.1
    for a in np.arange(0.1, a_lim + 0.1, 0.1):  
      # Deixar a com uma casa decimal para que no JSON fique certinho
      a = round(a, 1)
      for n in valores_n:
        futures.append(executor.submit(processar, a, n, k, qtd_instancias))

    for future in as_completed(futures):
      a, n, prob, tempo = future.result()
      
      if a not in resultados:
          resultados[a] = {}
      resultados[a][n] = {'prob': prob, 'tempo': tempo}
      
      print(f'{k}-SAT a = {a:.1f}, n = {n}: {prob}%')

  io.salvar_resultado(k, resultados)
  gra.construir_graficos(k, resultados, valores_n)


def main():
  # Executar 3-SAT primeiro e depois 5-SAT
  executar(3, QTD_INSTANCIAS, A_3, N_INSTANCIAS_3)
  executar(5, QTD_INSTANCIAS, A_5, N_INSTANCIAS_5)


if __name__ == "__main__":
  main()
