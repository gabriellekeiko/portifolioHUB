# -*- coding: utf-8 -*-
"""
Elabore um programa que leia, some e imprima o resultado da soma posicional, entre
duas listas de inteiros de 10 posições. Use uma terceira lista para armazenar o
resultado. Ao final mostre os valores das 3 listas da seguinte forma:
A soma de (valor da lista 1) + (valor da lista 2) = (valor da lista 3)
"""

lista1 = []
lista2 = []
lista3 = []

print("Digite os valores da primeira lista:")
for i in range(10):
    valor = int(input(f"Digite o {i + 1}º valor: "))
    lista1.append(valor)

print("\nDigite os valores da segunda lista:")
for i in range(10):
    valor = int(input(f"Digite o {i + 1}º valor: "))
    lista2.append(valor)

for i in range(10):
    soma = lista1[i] + lista2[i]
    lista3.append(soma)

print("\nResultado da soma posicional:")
for i in range(10):
    print(f"A soma de {lista1[i]} + {lista2[i]} = {lista3[i]}")