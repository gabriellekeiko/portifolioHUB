# -*- coding: utf-8 -*-
"""
Construa um programa que imprime a soma de todos os valores positivos
digitados pelo usuário até que ele digite um número negativo.
"""

soma = 0
print("Digite valores positivos para somar (digite um negativo para parar):")

while True:
    valor = float(input("Digite um valor: ").replace(",","."))
    if valor < 0:
        break
    soma = soma + valor
print("A soma total dos valores positivos é:", soma)