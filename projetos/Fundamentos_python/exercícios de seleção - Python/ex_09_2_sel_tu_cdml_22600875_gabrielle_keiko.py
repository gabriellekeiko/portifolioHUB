# -*- coding: utf-8 -*-
"""
Faça um programa que calcule as raízes de uma equação do 2° grau, levando em
consideração a análise da existência de raízes reais. Se o valor de delta for menor que
zero, não existem raízes nos reais; se delta for igual a zero, existem duas raízes iguais; se
delta for maior que zero, existem duas raízes diferentes.
"""

import math

a = float(input("Digite o valor de a: ").replace(",","."))
b = float(input("Digite o valor de b: ").replace(",","."))
c = float(input("Digite o valor de c: ").replace(",","."))

if a == 0:
    print("Não posso dividir por zero.")
else:
    delta = (b ** 2) - (4 * a * c)
    
    if delta < 0:
        print("Não existem raízes nos reais.")
        
    elif delta == 0:
        x = (-b) / (2 * a)
        print("Duas raízes iguais: x =", x)
        
    else:
        raiz_delta = math.sqrt(delta)
        x1 = (-b + raiz_delta) / (2 * a)
        x2 = (-b - raiz_delta) / (2 * a)
        print("Diferentes: x1 =", x1, "e x2 =", x2)
