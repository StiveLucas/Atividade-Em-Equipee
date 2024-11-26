import os
from app.models.abstract.funcionario import Funcionario
from app.models.endereco import Endereco
os.system("clear")

class Engenheiro(Funcionario):
    def __init__(self, crea: str, nome: str, telefone: str, email: str, salario: float, endereco: Endereco) -> None:
       super().__init__(nome, telefone, email, salario, endereco)

       self.crea = crea


    def __str__(self) -> str:
      return(

        f"\nNome: {self.nome}"
      )