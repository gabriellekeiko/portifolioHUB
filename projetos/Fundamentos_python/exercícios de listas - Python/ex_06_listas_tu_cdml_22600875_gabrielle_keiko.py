# -*- coding: utf-8 -*-
"""
Faça um programa que receba uma frase, e diga quantas consoantes foram lidas.
Imprima as consoantes
"""

frase = input("Digite uma frase (sem acentos e símbolos): ")

consoantes = []

for letra in frase:
    if letra != "a" and letra != "e" and letra != "i" and letra != "o" and letra != "u" and letra != " ":
        consoantes.append(letra)

print("Quantidade de consoantes:", len(consoantes))

print("Consoantes lidas:")
for i in range(len(consoantes)):
    print(consoantes[i], end=" ")