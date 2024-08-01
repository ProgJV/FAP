print("-------------------------------------")
print("        CALCULADORA COMPLETA         ")
print("-------------------------------------")

numero1= float(input('Digite o primeiro numero: '))
numero2= float(input('Digite o segundo numero: '))

print('MENU DE OPERAÇOES:')
print('1- Adição')
print('2- Subtração')
print('3- Multiplicação')
print('4- Divisão')

def multiplicao(a, b):
    resultado = a * b
    return resultado

def divisao(a, b):
    resultado = a / b
    return resultado

def somar (a,b):
    resultado = a + b
    return resultado 

def Subtração (a,b):
    resultado = a - b
    return resultado 

def par_impar(a):
    conta = a % 2

    if conta == 0:
        conta1 = ('par')
    else:
        conta1 = ('impar')
    return conta1

def positivo_negativo(a):
    if a >= 0:
        result = ('positivo')
    else:
        result = ('negativo')
    return result
     
def inteiro_decimal(a):
    numero = float(a)

    if(numero == round(numero)):
        result = ('inteiro')
    else:
        result = ('decimal')
    return result

opcao= int(input('Qual a opção desejada: '))

if opcao == 1:
    resuldado= somar(numero1, numero2)
elif opcao == 2: 
    resuldado= Subtração(numero1, numero2)
elif opcao == 3: 
    resuldado= multiplicao(numero1, numero2)
elif opcao == 4: 
    resuldado= divisao(numero1, numero2)
else:
    print('Opção invalida')

def formatar_num(a):
    
    if a.is_integer():
        return f"{int(a)}"
    else:
        return f"{a}"

result_par_impar = par_impar(resuldado)
result_positivo_negativo = positivo_negativo(resuldado)
result_inteiro_decimal = inteiro_decimal(resuldado)
result_formatar_num = formatar_num(resuldado)

print (f'O resultado é {result_formatar_num}, ele é {result_par_impar}, {result_positivo_negativo} e {result_inteiro_decimal}')