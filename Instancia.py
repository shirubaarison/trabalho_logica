import random
from pysat.solvers import Glucose42

class Instancia:
  def __init__(self):
    self.solver = Glucose42(use_timer=True)
    self.time = 0.0
    self.clausulas = []


  def gerar_clausulas(self, n: int, m: int, k: int) -> None:
    if k > n:
        raise ValueError("k maior que n")

    clausulas = set()
    for _ in range(m):  
        literais = random.sample(range(1, n + 1), k)
        clausula = tuple(v * random.choice((-1, 1)) for v in literais)
        clausulas.add(clausula)

    self.clausulas = list(clausulas) 

    for clausula in self.clausulas:
        self.solver.add_clause(list(clausula))

  def get_clausulas(self) -> list[tuple[int]]:
    return self.clausulas
  

  def resolva_clausulas(self) -> bool:
    resultado = self.solver.solve()
    self.time += self.solver.time()
    return resultado


  def get_time(self) -> float:
    return round(self.time, 2)