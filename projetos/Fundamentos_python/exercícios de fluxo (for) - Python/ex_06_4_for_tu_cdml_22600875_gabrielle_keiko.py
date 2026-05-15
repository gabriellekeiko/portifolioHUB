# -*- coding: utf-8 -*-
"""
Faça um programa que some os algarismos de um número inteiro e ao final da
execução exiba o número digitado e o somatório de seus algarismos.
"""

numero_digitado = input("Digite um número inteiro: ")
soma_algarismos = 0

for algarismo in numero_digitado:
    soma_algarismos += int(algarismo) 

print("Número digitado:", numero_digitado)
print("Somatório de seus algarismos:", soma_algarismos)