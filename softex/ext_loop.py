
def main():

    quantidade = 5
    maior = 0
    numeros = []
    for i in range(quantidade):
        numero = float(input(f"Digite o {i+1}º numero: "))
        numeros.append(numero)
        
        if numero > maior:
            maior = numero

    soma = sum(numeros)
    media = soma / len(numeros)
    print(f"A soma dos numeros é: {soma}")
    print(f"A média dos numeros é: {media}")
    print(f"A média dos numeros é: {media}")


main()

