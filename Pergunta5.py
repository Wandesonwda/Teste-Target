def inverter_string(s):
    """
    Função para inverter os caracteres de uma string.
    """
    string_invertida = ''
    for caractere in s:
        string_invertida = caractere + string_invertida
    return string_invertida

def main():
    # Exemplo com string definida no código
    string = "Exemplo de string"
    
    # Ou, se preferir, você pode descomentar a linha abaixo para permitir entrada do usuário
    # string = input("Digite uma string para inverter: ")
    
    string_invertida = inverter_string(string)
    
    print("String original:", string)
    print("String invertida:", string_invertida)

if __name__ == "__main__":
    main()
