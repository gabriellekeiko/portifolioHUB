# -*- coding: utf-8 -*-
"""
Faça um programa que imprime todos os números entre 30 e 5 (nesta ordem)
divisíveis por 3, e no final imprime sua soma.
"""

soma = 0  # Variável acumuladora para armazenar a soma total

for num in range(30, 4, -1):
    if num % 3 == 0:
        print(num)     
        soma += num    

print("Soma total:", soma)