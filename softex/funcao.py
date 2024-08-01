def somar (a,b):
    resultado = a + b
    return resultado 



def bem_vindo():
    print("-------------------------------------")
    print("           FAMILY PETSHOP            ")
    print("-------------------------------------")
    print("--- Aqui seu animal é bem cuidado ---")
    print()
    print("--------------------------------------")
    print("Seja muito bem vindo")
    print("--------------------------------------")

def menu():
    print("Menu:")
    print("1-Valor a pagar")
    print("2-cadastrar")
    opcao = int(input("digite a opcao escolhida: "))
    return opcao

def calcular_servico(quant_horas, quant_servicos):
    pagar = quant_horas*quant_servicos*10
    return pagar


def main():
    bem_vindo()
    opcao = menu()

    if opcao == 1:
        quant_servico = int(input("quantos servicos foram realizados: "))
        quant_horas = float(input("quantas horas meu funcionario trabalhou: "))
        quant_horas = round(quant_horas,2)
        cobrar = calcular_servico(quant_horas, quant_servico)
        #print("O usuario precisará pagar o valor de ", cobrar)
        print(f"O usuario solicitou {quant_servico} serviços e meu funcionario precisou trabalhar {quant_horas} horas, logo o usuario precisará pagar o valor de {cobrar}")

    else:
        print("Escolheu a opcao 2")

main()