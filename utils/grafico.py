import matplotlib.pyplot as plt
import datetime

from utils.constants import *

def construir_grafico_prob(k: int, resultados: dict[float, dict[int, dict[str, float]]], valores_n: list[int]):
  plt.figure(figsize=(12, 8))
  maior_tempo = 0
  
  for n in valores_n:
    alphas = []  # alpha
    probs = []  # prob de satisfazibilidade
    for a in sorted(resultados.keys()):
        alphas.append(a)
        probs.append(resultados[a][n]['prob'])
        if float(resultados[a][n]['tempo']) > maior_tempo:
          maior_tempo = float(resultados[a][n]['tempo'])
          ponto_critico = a
          critical_prob = resultados[a][n]['prob']

    plt.plot(alphas, probs, label=f'n = {n} (Instâncias = {QTD_INSTANCIAS})')

  # Destacar o alpha crítico
  plt.scatter([ponto_critico], [critical_prob], color='black', zorder=5, label="Ponto Crítico")
  plt.annotate(f'Ponto Crítico (α={ponto_critico})',
    xy=(ponto_critico, critical_prob),
    xytext=(ponto_critico, critical_prob),
    fontsize=10)
  
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


def construir_grafico_tempo(k: int, resultados: dict[float, dict[int, dict[str, float]]], valores_n: list[int]):
  plt.figure(figsize=(12, 8))
  
  maior_tempo = 0
  for n in valores_n:
    alphas = []  # a
    tempos = []  # tempo
    for a in sorted(resultados.keys()):
      if n in resultados[a]:
        alphas.append(a)
        tempos.append(resultados[a][n]['tempo'])
        if resultados[a][n]['tempo'] > maior_tempo:
          maior_tempo = resultados[a][n]['tempo']
          alpha_maior_tempo = a

    plt.plot(alphas, tempos, label=f'n = {n} (Instâncias = {QTD_INSTANCIAS})')

  # Destacar ponto de maior tempo
  plt.scatter(alpha_maior_tempo, maior_tempo, color='red', zorder=3, label="Maior Tempo")
  plt.annotate(f'({alpha_maior_tempo:.2f}, {maior_tempo:.2f}s)', 
                (alpha_maior_tempo, maior_tempo), 
                textcoords="offset points", 
                xytext=(10, -10), 
                ha='center', fontsize=10, color='black')
  
  titulo = f'{k}-SAT Tempo Médio de Resolução vs α'
  plt.title(titulo)
  plt.xlabel('Alpha (α)')
  plt.ylabel('Tempo médio (s)')
  plt.legend()
  plt.grid(True)

  # Gerar timestamp e caminho
  timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
  caminho = f'graficos/{k}sat_tempo_{timestamp}.png'
  
  plt.savefig(caminho)
  print(f'Gráfico de tempo gerado em: {caminho}')


def construir_graficos(k: int, resultados: dict[float, dict[int, dict[str, float]]], valores_n: list[int]):
  construir_grafico_prob(k, resultados, valores_n)
  construir_grafico_tempo(k, resultados, valores_n)