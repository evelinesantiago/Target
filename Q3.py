import json
from statistics import mean

def faturamento(dados):
    with open(dados, 'r') as file:
        data = json.load(file)
    
    faturamento_diario = [day['valor'] for day in data if day['valor'] > 0]
    
    menor_valor = min(faturamento_diario)
    maior_valor = max(faturamento_diario)
    media_mensal = mean(faturamento_diario)
    dias_acima_media = sum(1 for valor in faturamento_diario if valor > media_mensal)
    
    return {
        'menor_valor': menor_valor,
        'maior_valor': maior_valor,
        'dias_acima_media': dias_acima_media
    }

resultado = faturamento('dados.json')
print(f"Menor valor de faturamento: R$ {resultado['menor_valor']:.2f}")
print(f"Maior valor de faturamento: R$ {resultado['maior_valor']:.2f}")
print(f"Número de dias acima da média mensal: {resultado['dias_acima_media']}")