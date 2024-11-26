import pytest
from app.models.engenheiro import Engenheiro
from app.models.endereco import Endereco
from unittest.mock import Mock

def test_engenheiro_crea_vazio():

    endereco = Endereco("3", "3", "3", "3", "3")
    with pytest.raises(ValueError, match="A CREA não pode estar vazio"):
        Engenheiro("", "3", "3", "3", 3, endereco)

def test_engenheiro_nome_vazio():

    endereco = Endereco("3", "3", "3", "3", "3")
    with pytest.raises(ValueError, match="O Nome não pode estar vazio"):
        Engenheiro("3", "", "3", "3", 3, endereco)

def test_engenheiro_telefone_vazio():

    endereco = Endereco("3", "3", "3", "3", "3")
    with pytest.raises(ValueError, match="O Telefone não pode estar vazio"):
        Engenheiro("3", "3", "", "3", 3, endereco)

def test_engenheiro_email_vazio():

    endereco = Endereco("3", "3", "3", "3", "3")
    with pytest.raises(ValueError, match="O E-mail não pode estar vazio"):
        Engenheiro("3", "3", "3", "", 3, endereco)

def test_engenheiro_salario_vazio():

    endereco = Endereco("3", "3", "3", "3", "3")
    with pytest.raises(ValueError, match="O Salário não pode estar vazio"):
        Engenheiro("3", "3", "3", "3", None, endereco)