def calcular_percentuais(faturamentos):
    """
    Função para calcular o percentual de representação de cada estado.
    """
    total_faturamento = sum(faturamentos.values())
    percentuais = {estado: (valor / total_faturamento) * 100 for estado, valor in faturamentos.items()}
    return percentuais

def main():
    # Faturamento mensal detalhado por estado
    faturamentos = {
        'SP': 67836.43,
        'RJ': 36678.66,
        'MG': 29229.88,
        'ES': 27165.48,
        'Outros': 19849.53
    }

    percentuais = calcular_percentuais(faturamentos)

    print("Percentual de representação de cada estado:")
    for estado, percentual in percentuais.items():
        print(f"{estado}: {percentual:.2f}%")

if __name__ == "__main__":
    main()
