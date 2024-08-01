

def fibonacci(n):
    numero = fibonacci(n - 1)
    resultado = numero[-1] + numero[-2]
    numero.append(resultado)
    return numero

def main():
    continuar = True
    while continuar:
        try:
            print('BEM VINDO AO IDENTIFICADOR FIBONACCI')
            print(37*('-'))

            numero = int(input('Digite o numero que você deseja consultar: '))

            if numero < 0:
                print('Não há negativos na sequencia de fibonacci.')
            else:    
                sequencia = fibonacci(50)

                if numero in list(sequencia):
                    print(f'O número {numero} faz parte de fibonacci')
                else:
                    print(f'O numero {numero} não faz parte de fibonacci')
            
            valor = input('digite 0 para sair: ')
            if valor == '0':
                continuar = False

        except ValueError:
            print("O valor digitado não é um numero")
        except Exception as e: 
            print(f'Erro inesperado. Erro: {e}')
    
main()
