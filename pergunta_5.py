string = input("Informe uma string para inverter: ")

string_invertida = ""
indice = len(string) - 1

while indice >= 0:
    string_invertida += string[indice]
    indice -= 1

print(f"String invertida: {string_invertida}")
