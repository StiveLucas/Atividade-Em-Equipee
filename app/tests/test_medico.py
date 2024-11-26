#Não esqueça de instalar o pytest  (pip install pytest)
import pytest
from app.models.medico import Medico
from app.models.endereco import Endereco
from unittest.mock import Mock

def test_medico_crm_vazio():

    endereco = Endereco("3", "3", "3", "3", "3")
    with pytest.raises(ValueError, match="O CRM não pode estar vazio"):
        Medico("", "3", "3", "3", 3, endereco)

def test_medico_nome_vazio():

    endereco = Endereco("3", "3", "3", "3", "3")
    with pytest.raises(ValueError, match="O Nome não pode estar vazio"):
        Medico("3", "", "3", "3", 3, endereco)

def test_medico_telefone_vazio():

    endereco = Endereco("3", "3", "3", "3", "3")
    with pytest.raises(ValueError, match="O Telefone não pode estar vazio"):
        Medico("3", "3", "", "3", 3, endereco)

def test_medico_email_vazio():

    endereco = Endereco("3", "3", "3", "3", "3")
    with pytest.raises(ValueError, match="O E-mail não pode estar vazio"):
        Medico("3", "3", "3", "", 3, endereco)

def test_medico_salario_vazio():

    endereco = Endereco("3", "3", "3", "3", "3")
    with pytest.raises(ValueError, match="O Salário não pode estar vazio"):
        Medico("3", "3", "3", "3", None, endereco)
