def inverter_string(texto):
    invertida = ""
    for i in range(len(texto) - 1, -1, -1):
        invertida += texto[i]
    return invertida

texto_original = input("Digite uma string para inverter: ")

texto_invertido = inverter_string(texto_original)

print("String original:", texto_original)
print("String invertida:", texto_invertido)
