import os

class Endereco():
    def __init__(self, logradouro: str, numero: str, complemento: str, cep: str, cidade: str) -> None:

        if not logradouro:
            raise ValueError("O Logradouro não pode estar vazio")
        
        if not numero:
            raise ValueError("O Número não pode estar vazio")
        
        if not complemento:
            raise ValueError("O Complemento não pode estar vazio")
        
        if not cep:
            raise ValueError("O CEP não pode estar vazio")
        
        if not cidade:
            raise ValueError("A Cidade não pode estar vazio")

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