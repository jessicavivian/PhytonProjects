#!/usr/bin/env python3
#Calculator


operation = int(input("Selecione o número da opção desejada: \n\n 1 - Soma \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n\n Digite sua opção (1/2/3/4):"))


if operation == 1:
    value1 = int(input("\nDigite o primeiro número:"))
    value2 = int(input("Digite o segundo número:"))
    soma = value1 + value2
    print("\n %i + %i = %i" %(value1, value2, soma))

elif operation == 2:
    value1 = int(input("\nDigite o primeiro número:"))
    value2 = int(input("Digite o segundo número:"))
    subt = value1 - value2
    print("\n %i - %i = %i" %(value1, value2, subt))


elif operation == 3:
    value1 = int(input("\nDigite o primeiro número:"))
    value2 = int(input("Digite o segundo número:"))
    mult = value1 * value2
    print("\n %i * %i = %i" %(value1, value2, mult))


elif operation == 4:
    value1 = int(input("\nDigite o primeiro número:"))
    value2 = int(input("Digite o segundo número:"))
    div = value1 / value2
    print("\n %i / %i = %i" %(value1, value2, div))


else:
    print("\n Opção digitada inválida")

