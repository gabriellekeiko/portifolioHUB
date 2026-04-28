# -*- coding: utf-8 -*-
"""
Sabendo que a fórmula de conversão de graus Fahrenheit para Celsius é:
C = ( 5 / 9 ) * ( f – 32 ), escreva um programa que converta de Fahrenheit para
Celsius e exiba na tela os 20 (vinte) primeiros valores a partir da temperatura de 32°
F , devendo exibir as duas unidades de conversão. 
"""

f = 32
contador = 1
print("CONVERSÃO FAHRENHEIT-CELSIUS")
print("FAHRENHEIT|CELSIUS")

while contador <= 20:
    c = (5 / 9) * (f - 32)
    print(f, "°F| %.2f" %c, "°C")
    f = f + 1
    contador = contador + 1
