def main():
    
    try:
        print('sistema de calculo de IMC')

        altura= float (input('Digite sua altura (m): '))
        peso= float(input('Digite seu peso (kg): '))

        imc= peso / (altura**2)

        print('IMC: ', imc)

        if imc <= 18.5:
            print('Seu peso esta abaixo da media')
        elif imc > 18.5 and imc < 25:
            print('seu peso esta normal')
        elif imc > 25 and imc < 29.9:
            print('Você esta com sobrepeso')
        elif imc > 30 and imc < 34.9:
            print('Você esta obesidade grau 1')
        elif imc > 35 and imc < 39.9:
            print('Você esta obesidade grau 2')
        elif imc > 40:
            print('Você esta obesidade grau 3')

    except ValueError:
        print("O valor digitado não é um número")
    except Exception as e: 
        print(f'Erro inesperado. Erro: {e}') 
main()
