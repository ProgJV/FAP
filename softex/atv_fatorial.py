
def fatorial(n):
    resultado=1

    if n > 0:
        for n in range(1, n+1):
         resultado *= n
    else:
        print('Não é possivel calcular fatorial de 0')
    return resultado

def main():
    try:
        numero=int(input('Digite um numero para calcular fatorial: '))
        calculo = fatorial(numero)
        print (f'O fatorial de {numero} é {calculo}')
    except ValueError:
        print("O valor digitado não é um numero")

main()
