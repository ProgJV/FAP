import random

def menu():
    print('Menu de dificuldades:')
    print('1- Fácil')
    print('2- Médio')
    print('3- Difícil')
    print('4- Sair')
    opcao = input('Escolha a opção:')
    return opcao

def main():
    try:

        print('Bem vindo(a) ao jogo da forca!!')
        print('-' * 31)
        
        while True:
            letras_user = []
            opcao = menu()
        
            ### abrindo o arquivo e selecionando uma palavra aleatoria 
            if opcao == '1':
                with open("palavra_f.txt", "r", encoding='utf-8') as palavra_f:
                    palavras = palavra_f.readlines()
                    palavra = random.choice(palavras).strip()
                chance = 7

            elif opcao == '2': 
                with open("palavra_m.txt", "r", encoding='utf-8') as palavra_m:
                    palavras = palavra_m.readlines()
                    palavra = random.choice(palavras).strip()
                chance = 6

            elif opcao == '3': 
                with open("palavra_d.txt", "r", encoding='utf-8') as palavra_d:
                    palavras = palavra_d.readlines()
                    palavra = random.choice(palavras).strip()
                chance = 5

            elif opcao == '4':
                print('Saindo do jogo...')
                break
                
            else:
                print('Opção inválida, tente novamente')
                continue  

            while True:
                ### mostrar letras que o usuario digitou 
                print('A palavra é: ')
                for letra in palavra:
                    if letra.lower() in letras_user:
                        print(letra, end=' ')
                    else:
                        print('_', end=' ')
                print()
                print(f'Você tem {chance} chances')
                
                ### pedir letra
                print()
                letra_u = input('Digite uma letra: ').lower()
                print()

                if letra_u not in letras_user:
                    letras_user.append(letra_u)

                    if letra_u not in palavra.lower():
                        chance -= 1
                        print(f'Letra incorreta. Você tem {chance} chances restantes.')

                        if chance == 0:
                            print(f'Você perdeu! A palavra era {palavra}')
                            break
                
                ### verificar letras 
                todas_letras_adivinhadas = True
                for letra in palavra:
                    if letra.lower() not in letras_user:
                        todas_letras_adivinhadas = False
                        break

                if todas_letras_adivinhadas:
                    print('Você adivinhou a palavra:', palavra)
                    break
    
    except ValueError:
        print("O valor digitado não é um número")
    except Exception as e: 
        print(f'Erro inesperado. Erro: {e}') 

main()
