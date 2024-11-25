import os
from app.models.endereco import Endereco

class Funcionario(Endereco):
    def __init__(self, nome: str, telefone: str, email: str, salario: float, endereco: Endereco) -> None:
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.salario = salario
        self.endereco = endereco

    def __str__(self) -> str:
        return(

            f"\nFuncionário: \nNome: {self.nome}, \nTelefone: {self.telefone}"
            f" \nEmail: {self.email} \nSalário: {self.salario} \nEndereco: {self.Endereco}"
        ) 