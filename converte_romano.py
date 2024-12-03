def converter_para_romano(numero):
    """
    Converte um número inteiro em algarismos romanos.
    Apenas números no intervalo de 1 a 3999 são aceitos.
    """
    if numero <= 0 or numero > 3999:
        raise ValueError("O número deve estar entre 1 e 3999.")
    
    valores = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]
    resultado = ""
    for valor, simbolo in valores:
        while numero >= valor:
            resultado += simbolo
            numero -= valor
    return resultado


print(converter_para_romano(1000))