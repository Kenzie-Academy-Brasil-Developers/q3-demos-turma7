from app.main import soma, sub, mult, divisao, converter
import random
import pytest


@pytest.mark.funcaox
def test_funcao_soma_se_os_valores_quando_somados_estao_corretos():
    """ ESSE TESTE VERIFICA SE A FUÇÃO SOMA ESTÁ SOMANDO """
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    
    resultado = soma(num1, num2)
    esperado = num1 + num2
    assert resultado == esperado


@pytest.mark.funcaox
def test_funcao_sub_se_os_valores_quando_subtraidos_estao_corretos():
    resultado = sub(7, 8)
    esperado = 7 - 8
    assert resultado == esperado


@pytest.mark.funcaog
def test_funcao_div_se_os_valores_quando_divididos_estao_corretos():
    resultado = sub(7, 8)
    esperado = 7 - 8
    assert resultado == esperado


def test_soma_valores_aproximados():
    resultado = soma(0.1, 0.2)
    esperado = 0.3
    assert resultado == pytest.approx(esperado)


def test_verifique_se_string_esta_capitalizada():
    # TODO: Quero que esse teste verifique se a string está capitalizada
    # FIXME: Temos um pequeno problema e precisamos resolver o quanto antes, urgência
    # XXX: Deu ruim, bora consertar senão ferrou, emergência

    # Given, UM VALOR INICIAL
    # When, FUNÇÃO IMPLEMENTADA converver()
    # Then, O QUE EU ESPERO QUE SEJA RETORNADO

    palindromo = "socorram-me subi no onibus em marrocos"
    result = converter(palindromo)
    esperado = palindromo.capitalize()
    assert len(result) == len(palindromo)
