def Binario(binario):
    if len(binario) == 0:
        return 0
    
    ultimo_digito = int(binario[-1])
    resto = binario[:-1]
    valor_decimal = ultimo_digito + 2 * Binario(resto)
    return valor_decimal

binario = "10101"
valor_decimal = Binario(binario)

print("Valor decimal:", valor_decimal)