# -*- coding: utf-8 -*-
"""
Elaborar um programa C para computar a média de N números reais. Você receberá
um número real e irá realizar a soma dele com todos os seus antecessores até chegar
a zero
"""

n = int(input("Digite um número real: "))

soma = 0
contador = 0
numero_original = n

for n in range(numero_original,0,-1):
    soma += n          
    contador += 1    
    media = soma / contador

print("Soma total:",soma) 
print("A média da soma de",numero_original, "e seus antecessores é:",media)