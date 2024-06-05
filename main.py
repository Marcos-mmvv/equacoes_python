# Calcular equações de 1º e 2º grau

import os
# Para usar a função match.sqrt(valor)
import math 

def exibir_menu():
    print(f'{'-'*30} SELECIONE A OPÇÃO DESEJADA{'-'*30}\n')
    print('1 - Equação de 1º grau.')
    print('2 - Equação de 2º grau.')
    print('3 - Sair do programa.\n')

def calcular_equacao1(ax, b, c):
    calc = (float(b) - float(c)) / float(ax)
    return calc

def calcular_equacao2(ax2, bx, c):
    
    delta = (float(bx) * float(bx)) - 4*float(ax2) * float(c)
    return delta

while True:
    exibir_menu()

    opcao = int(input('Informe a opção desejada: '))

    os.system('cls')

    match opcao:
        case 1:
            print('Equação de 1º Grau: \n')

            ax = input('Digite o valor de A: ')
            b = input('Digite o valor de B: ')
            c = input('Digite o valor de C: ')

            print(f'O valor de X é: {calcular_equacao1(ax, b, c)}')
            continue
                    
        case 2:
            print('Equação de 2º Grau: \n')

            ax2 = input("Digite o valor de A: ")
            bx = input("Digite o valor de B: ")
            c = input("Digite o valor de C: ")

            print(f'O valor de X é: {calcular_equacao2(ax2, bx, c)}')

        case 3:
            break
        case _:
            print('Opção inválida.')
            continue

