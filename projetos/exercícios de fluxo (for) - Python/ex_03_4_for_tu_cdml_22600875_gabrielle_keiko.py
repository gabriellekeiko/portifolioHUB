# -*- coding: utf-8 -*-
"""
Sabendo que a fórmula de conversão de graus Fahreinheit para Celsius é C = ( 5 / 9 ) *
( f – 32 ), escreva um programa que converta de Fahreinheit para Celsius. O programa
deverá imprimir na tela os 50 (cinquenta) primeiros valores positivos e negativos
devendo exibir as duas unidades de conversão
"""

print("Valores Negativos (Fahrenheit para Celsius):")
for f in range(-50, 0, 1):
    celsius = (5 / 9) * (f - 32)
    print("Fahrenheit: %d | Celsius: %.2f" % (f, celsius))

print("Valores Positivos (Fahrenheit para Celsius):")
for f in range(1, 51, 1):
    celsius = (5 / 9) * (f - 32)
    print("Fahrenheit: %d | Celsius: %.2f" %(f, celsius))