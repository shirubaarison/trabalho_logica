import matplotlib.pyplot as plt
import datetime
  
def construir_grafico_prob(self, k: int, resultados, valores_n):
  plt.figure(figsize=(12, 8))
  for n in valores_n:
    alphas = []  # alpha
    probs = []  # prob de satisfazibilidade
    for a in sorted(resultados.keys()):
        alphas.append(a)
        probs.append(resultados[a][n]['prob'])
    plt.plot(alphas, probs, label=f'n = {n}')

  titulo = f'{k}-SAT Satisfazibilidade vs Alpha'
  plt.title(titulo)
  plt.xlabel('Alpha (α)')
  plt.ylabel('Probabilidade (%)')
  plt.legend()
  plt.grid(True)

  # Gerar timestamp e caminho
  timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
  caminho = f'graficos/{k}sat_{timestamp}.png'
  
  plt.savefig(caminho)
  print(f'Gráfico de probabilidade gerado em: {caminho}')


def construir_grafico_tempo(self, k: int, resultados, valores_n):
  plt.figure(figsize=(12, 8))
  for n in valores_n:
    alphas = []  # a
    tempos = []  # tempo
    for a in sorted(resultados.keys()):
      if n in resultados[a]:
        alphas.append(a)
        tempos.append(resultados[a][n]['tempo'])

    plt.plot(alphas, tempos, label=f'n = {n}')
  
  titulo = f'{k}-SAT Tempo de Resolução vs α'
  plt.title(titulo)
  plt.xlabel('Alpha (α)')
  plt.ylabel('Tempo de Resolução (s)')
  plt.legend()
  plt.grid(True)

  # Gerar timestamp e caminho
  timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
  caminho = f'graficos/{k}sat_tempo_{timestamp}.png'
  
  plt.savefig(caminho)
  print(f'Gráfico de tempo gerado em: {caminho}')