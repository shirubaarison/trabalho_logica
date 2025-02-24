import datetime
import json

def salvar_resultado(k: int, resultado: dict[float, dict[int, dict[str, float]]]):
  """ Salva resultados em um JSON em /data """
  timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
  caminho = f'data/{k}_sat_result_{timestamp}.json'

  with open(caminho, 'w') as file:
    json.dump(resultado, file)
  print(f"Resultados salvos em: {caminho}")


def ler_resultados(k: int) -> dict[float, dict[int, dict[str, float]]]:
  """ Ler resultados já salvos como JSON """
  caminho = f'data/{k}_sat_result.json'
  with open(caminho, 'r') as file:
    resultado = json.load(file)

    resultado = {float(a): {int(n): v for n, v in subdict.items()} for a, subdict in resultado.items()}
  
  return resultado