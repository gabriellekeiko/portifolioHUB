# -*- coding: utf-8 -*-
"""
 Faça um programa que leia dois valores quaisquer e mostre o maior deles ou mostre a
mensagem “Os valores são iguais.”
"""

n1 = float(input("Digite o primeiro valor: ").replace(",","."))
n2 = float(input("Digite o segundo valor: ").replace(",","."))

if n1 > n2:
    print("O maior valor é", n1)
    print("Ordem decrescente:", n1, "e", n2)

elif n2 > n1:
    print("O maior valor é", n2)
    print("Ordem decrescente:", n2, "e", n1)

else:
    print("Os valores são iguais.")
    print("Valor digitado:", n1)
