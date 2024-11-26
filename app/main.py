from app.models.engenheiro import Engenheiro
from app.models.endereco import Endereco
from app.models.medico import Medico
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'app')))

#Ola prof, use esse comando aqui em baixo para da Run no código. Garanto que vai funcionar
#python -m app.main

#Eu não conseguir configurar para  rodar no botão de executar, espero q aceite.

try:

    #Instanciando classes.
    endereco = Endereco("Perto do rio", "333", "Nenhum", "404579-98", "Salvador")
    engenheiro = Engenheiro("12456", "Lucas", "71-8768-97", "@gmail.com", 4500, endereco)
    medico = Medico("2442", "Davi", "72-76646-788", "@hotmail.com", 3400, endereco)

    print(medico, engenheiro)

except ValueError as e:
    print(e)

#Alunos que fizeram
#Lucas Santos Pêpe Pinheiro
#Thiago Gabriel Torres
#Davi Alexandro Freitas Leal