# -*- coding: utf-8 -*-
"""
Elaborar um programa para computar a média de N números reais.
"""

n = int(input("Quantos números você deseja digitar? "))
soma = 0
contador = 0

while contador < n:
    valor = float(input("Digite um número real: ").replace(",","."))
    soma = soma + valor
    contador = contador + 1

if n > 0:
    media = soma / n
    print("A soma dos números é:", soma)
    print("A média de", n, "números é: %.2f" %media)
else:
    print("Quantidade inválida para média.")