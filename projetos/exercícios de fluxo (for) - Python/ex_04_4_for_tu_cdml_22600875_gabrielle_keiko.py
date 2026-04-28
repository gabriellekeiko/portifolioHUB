# -*- coding: utf-8 -*-
"""
A partir do exercício 3 faça um programa que deverá exibir os resultados da
conversão, parando a cada 25 valores exibidos e solicitar ao usuário que digite a
tecla “ENTER” para continuar, após o usuário digitar “ENTER” a tela deverá ser limpa
e a exibição continuar. A cada tela exibida o programa deverá exibir o seguinte
cabeçalho.
CONVERSAO FAHREINHEIT – CELSIUS
CELSIUS FAHREINHEIT
"""

import os  

valores_fahrenheit = list(range(-50, 0)) + list(range(1, 51))
contador = 0
print("CONVERSAO FAHREINHEIT – CELSIUS")
print("CELSIUS | FAHREINHEIT")

for f in valores_fahrenheit:
    if contador > 0 and contador % 25 == 0:
        input("Pressione ENTER para continuar...")
        os.system('cls')  
        
        print("CONVERSAO FAHREINHEIT – CELSIUS")
        print("CELSIUS | FAHREINHEIT")

    celsius = (5 / 9) * (f - 32)
    print("%.2f |" %celsius, "%.2f" %f)
    contador += 1