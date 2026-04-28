# -*- coding: utf-8 -*-
"""
Crie um programa que imprima na tela os números 1 até o 10, usando o laço while, em
seguida faça o mesmo, porém contando de 10 até 1.
"""

print("Contagem Progressiva (1 até 10):")
contador_up = 1

while contador_up <= 10:
    print(contador_up)
    contador_up += 1

print("Contagem Regressiva (10 até 1):")
contador_down = 10

while contador_down >= 1:
    print(contador_down)
    contador_down -= 1

print("Fim do programa!")