print('PROBLEMA DE MATEMATICA')

numero_int = int (input('DIGITE UM NUMERO MENOR QUE 1000: '))

centenas = int(numero_int / 100)

resto_dez= numero_int % 100
dezena= int(resto_dez / 10) 

unidade = int(resto_dez % 10) 

if centenas > 0:
    print(f"Centenas: {centenas}, dezenas: {dezena} e unidades: {unidade}")
elif dezena > 0:
    print(f"Dezenas: {dezena} e unidades: {unidade}")
elif unidade > 0:
    print(f"Unidades: {unidade}")
else:
    print("Numero invalido")