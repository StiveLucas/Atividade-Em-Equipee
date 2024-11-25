import os
os.system("clear")

class Engenheiro():
    def __init__(self, crea: str) -> None:
        self.crea = crea

    def __str__(self) -> str:
      return(f"\nCrea: {self.crea}") 