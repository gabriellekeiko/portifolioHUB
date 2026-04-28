# -*- coding: utf-8 -*-
"""
Prepare um programa para gerar o número H, ou seja, calcular o valor de H.
Sendo H = 1/2 + 1/3 + 1/4 + 1/5 + . . . + 1/n. O número “n” será fornecido pelo usuário.
"""

n = int(input("Digite o valor de n: "))
h = 0

for i in range(2, n + 1):
 
    h += 1 / i

print("O valor de H é: %.2f" % h)