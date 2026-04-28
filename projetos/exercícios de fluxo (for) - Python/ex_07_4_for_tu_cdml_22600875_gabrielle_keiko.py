# -*- coding: utf-8 -*-
"""
Elabore um programa que gere a sequência dos números inteiros, onde o usuário
deverá fornecer o valor inicial e o valor final dessa sequência.
"""

valor_inicial = int(input("Digite o valor inicial: "))
valor_final = int(input("Digite o valor final: "))

print("Sequência gerada:")

for i in range(valor_inicial, valor_final + 1):
    print(i)