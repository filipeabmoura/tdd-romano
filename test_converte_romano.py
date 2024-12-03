import pytest
from converte_romano import converter_para_romano

def test_conversao_valores_basicos():
    """Testa a conversão de valores básicos."""
    assert converter_para_romano(1) == "I"
    assert converter_para_romano(4) == "IV"
    assert converter_para_romano(9) == "IX"
    assert converter_para_romano(40) == "XL"
    assert converter_para_romano(90) == "XC"
    assert converter_para_romano(400) == "CD"
    assert converter_para_romano(900) == "CM"
    assert converter_para_romano(1000) == "M"

def test_conversao_valores_combinados():
    """Testa a conversão de valores mais complexos."""
    assert converter_para_romano(58) == "LVIII"  # 50 + 5 + 3
    assert converter_para_romano(1994) == "MCMXCIV"  # 1000 + 900 + 90 + 4
    assert converter_para_romano(3999) == "MMMCMXCIX"

def test_valores_fora_do_intervalo():
    """Testa se a função lida corretamente com valores inválidos."""
    with pytest.raises(ValueError, match="O número deve estar entre 1 e 3999."):
        converter_para_romano(0)
    with pytest.raises(ValueError, match="O número deve estar entre 1 e 3999."):
        converter_para_romano(-5)
    with pytest.raises(ValueError, match="O número deve estar entre 1 e 3999."):
        converter_para_romano(4000)
