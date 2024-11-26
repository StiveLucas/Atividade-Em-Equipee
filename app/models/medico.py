import os
from app.models.abstract.funcionario import Funcionario
from app.models.endereco import Endereco
os.system("clear")

class Médico(Funcionario):
    def __init__(self, crm: str, nome: str, telefone: str, email: str, salario: float, endereco: Endereco) -> None:
      super().__init__(nome, telefone, email, salario, endereco) 

      self.crm = crm

    def __str__(self) -> str:
       return(

        f"\nCrm: {self.crm} \nNome: {self.nome} \nTelefone: {self.telefone} \nE-mail: {self.email}"
        f"\nSalário: {self.salario} \nEndereço: {self.endereco}"
      )