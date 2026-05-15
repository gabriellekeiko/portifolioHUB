# -*- coding: utf-8 -*-
"""
Sabendo que a fórmula de conversão de graus Fahrenheit para Celsius é:
C = ( 5 / 9 ) * ( f – 32 ), escreva um programa que converta de Fahrenheit para
Celsius exiba na tela as temperaturas compreendidas em um intervalo a ser
fornecido pelo usuário. O usuário deverá fornecer o valor inicial e o valor final. O
fluxograma então exibirá as temperaturas compreendidas no intervalo, devendo
exibir as duas unidades de conversão.
"""

f_inicial = int(input("Digite o valor inicial em Fahrenheit: "))
f_final = int(input("Digite o valor final em Fahrenheit: "))
print("CONVERSÃO FAHRENHEIT-CELSIUS")
print("FAHRENHEIT|CELSIUS")
f = f_inicial

while f <= f_final:
    c = (5 / 9) * (f - 32)
    print(f, "°F| %.2f" %c, "°C")
    f = f + 1
