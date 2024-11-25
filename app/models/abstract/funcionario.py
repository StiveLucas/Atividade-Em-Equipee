import os

class Funcionario():
    def __init__(self, nome: str, telefone: str, email: str, Endereco: Endereco) -> None:
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.Endereco = Endereco



    def calcular_bonus(self) -> float:
        pass

    def __str__(self) -> str:
        return f"Funcionário(Nome: {self.nome}, Telefone: {self.telefone}, Email: {self.email}, Endereco: {self.Endereco})"