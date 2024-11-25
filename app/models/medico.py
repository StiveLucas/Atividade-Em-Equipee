import os
os.system("clear")

class Médico():
    def __init__(self, crm: str) -> None:
        self.crm = crm

    def __str__(self) -> str:
      return(f"\nCrm: {self.crm}") 