
# -*- coding: utf-8 -*-
"""
Faça um programa que peça um número inteiro maior que 1 ao usuário. Em seguida,
imprima todos os números, de 1 até o número que o usuário informou.
"""

n = int(input("Digite um número inteiro maior que 1: "))
contador = 1
print("Contagem de 1 até", n, ":")
while contador <= n:
    print(contador)
    contador+=1
print("Fim da contagem!")