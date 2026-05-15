# -*- coding: utf-8 -*-
"""
Elabore um programa que leia um número qualquer e verifique se ele é positivo, nulo ou
negativo.
"""

num = float(input("Digite um número: ").replace(",","."))
print("Número digitado:", num)

if num > 0:
    dobro = num * 2
    print("Número Positivo")
    print("O dobro de seu valor é:", dobro)

elif num < 0:
    triplo = num * 3
    print("Número Negativo")
    print("O triplo de seu valor é:", triplo)

else:
    print("Número Nulo")
