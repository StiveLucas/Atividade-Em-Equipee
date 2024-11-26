#Não esqueça de instalar o pytest  (pip install pytest)
import pytest
import os
from app.models.endereco import Endereco

def test_endereco_logradouro_vazio():
    with pytest.raises(ValueError, match= "O Logradouro não pode estar vazio"):
        Endereco("","3", "3", "3", "3")

def test_endereco_numero_vazio():
    with pytest.raises(ValueError, match= "O Número não pode estar vazio"):
        Endereco("3","", "3", "3", "3")

def test_endereco_complemento_vazio():
    with pytest.raises(ValueError, match= "O Complemento não pode estar vazio"):
        Endereco("3", "3", "", "3", "3")

def test_endereco_cep_vazio():
    with pytest.raises(ValueError, match= "O CEP não pode estar vazio"):
        Endereco("3", "3", "3", "", "3")

def test_endereco_cidade_vazio():
    with pytest.raises(ValueError, match= "A Cidade não pode estar vazio"):
        Endereco("3", "3", "3", "3", "")