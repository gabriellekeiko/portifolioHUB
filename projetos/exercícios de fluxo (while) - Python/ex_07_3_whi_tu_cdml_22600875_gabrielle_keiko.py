# -*- coding: utf-8 -*-
"""
Faça um programa que implemente a tabuada de um número inteiro a ser
solicitado ao usuário. Apresente da seguinte forma:

"""

n = int(input("Digite um número inteiro para ver a tabuada: "))
i = 0
print("Tabuada do", n)

while i <= 10:
    resultado = n * i
    print(n, "x", i, "=", resultado)
    i = i + 1