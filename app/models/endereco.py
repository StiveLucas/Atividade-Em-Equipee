import os

class Endereco():
    def __init__(self, logradouro: str, numero: str, complemento: str, cep: str, cidade: str, ufnome: str, ufsigla: str) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade
        

    def __str__(self) -> str:
      return(
         
         f"\nLogradouro: {self.logradouro} \nNúmero: {self.numero}"
         f" \nComplemento: {self.complemento} \nCEP: {self.cep} \nCidade: {self.cidade}"
      ) 