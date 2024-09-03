import json

def analisar_faturamento(dados_faturamento):
    faturamentos = [item['valor'] for item in dados_faturamento if item['valor'] > 0]
    
    if not faturamentos:
        return None, None, 0

    menor_faturamento = min(faturamentos)
    maior_faturamento = max(faturamentos)
    media_mensal = sum(faturamentos) / len(faturamentos)
    dias_acima_media = sum(faturamento > media_mensal for faturamento in faturamentos)
    
    return menor_faturamento, maior_faturamento, dias_acima_media

def main():
    # Carregar os dados de faturamento do arquivo JSON
    with open('faturamento.json', 'r') as file:
        dados = json.load(file)
    
    faturamentos = dados['faturamentos']
    
    menor_faturamento, maior_faturamento, dias_acima_media = analisar_faturamento(faturamentos)

    if menor_faturamento is not None:
        print(f"Menor valor de faturamento: R${menor_faturamento:.2f}")
        print(f"Maior valor de faturamento: R${maior_faturamento:.2f}")
        print(f"Número de dias com faturamento acima da média mensal: {dias_acima_media}")
    else:
        print("Nenhum dado de faturamento válido fornecido.")

if __name__ == "__main__":
    main()

