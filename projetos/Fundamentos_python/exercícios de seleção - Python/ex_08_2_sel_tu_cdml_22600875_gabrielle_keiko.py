# -*- coding: utf-8 -*-
"""
Faça um programa que leia um valor numérico e verifique se ele é maior ou igual a cem.
Mostre uma das mensagens: “Valor maior ou igual a cem.” Ou “Valor menor que cem.”
"""

valor = float(input("Digite um valor numérico: "))
print("Valor digitado:", valor)

if valor >= 100:
    print("Valor maior ou igual a cem.")
else:
    print("Valor menor que cem.")
