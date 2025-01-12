import json

with open("dados.json", "r") as arquivo:
    dados = json.load(arquivo)

faturamento_valido = [dia["valor"] for dia in dados if dia["valor"] > 0]
menor_valor = min(faturamento_valido)
maior_valor = max(faturamento_valido)
media_mensal = sum(faturamento_valido) / len(faturamento_valido)
dias_acima_da_media = sum(1 for valor in faturamento_valido if valor > media_mensal)

print(f"Menor valor de faturamento: {menor_valor:.2f}")
print(f"Maior valor de faturamento: {maior_valor:.2f}")
print(f"Dias com faturamento acima da média mensal: {dias_acima_da_media}")
