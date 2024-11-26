import os
from app.models.abstract.funcionario import Funcionario
from app.models.endereco import Endereco
os.system("clear")

class Medico(Funcionario):
    def __init__(self, crm: str, nome: str, telefone: str, email: str, salario: float, endereco: Endereco) -> None:
      super().__init__(nome, telefone, email, salario, endereco) 

      if not crm:
            raise ValueError("O CRM não pode estar vazio")
      
      if not nome:
          raise ValueError("O Nome não pode estar vazio")
      
      if not telefone:
          raise ValueError("O Telefone não pode estar vazio")
      
      if not email:
          raise ValueError("O E-mail não pode estar vazio")
      
      if not salario:
          raise ValueError("O Salário não pode estar vazio")

      self.crm = crm
 
    def __str__(self) -> str:
       return(

        f"\nMédico: \nCrm: {self.crm} \nNome: {self.nome} \nTelefone: {self.telefone} \nE-mail: {self.email}"
        f"\nSalário: R${self.salario} \nEndereço: {self.endereco}"
      )