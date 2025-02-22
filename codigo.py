import random
from pysat.solvers import Glucose4

class Instancia:
  def __init__(self):
    self.solver = Glucose4(use_timer=True)
    self.time_to_solve = 0
    self.clausulas = []


  def gerar_clausulas(self, n: int, m: int, k: int):
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

  def get_clausulas(self):
    return self.clausulas
  

  def resolva_clausulas(self):
    resultado = self.solver.solve()
    self.time_to_solve += self.solver.time()
    return resultado


  def resetar(self):
    self.solver.delete()
    self.clausulas = []
    self.solver = Glucose4(use_timer=True)


  def get_time(self):
    return round(self.time_to_solve, 2)