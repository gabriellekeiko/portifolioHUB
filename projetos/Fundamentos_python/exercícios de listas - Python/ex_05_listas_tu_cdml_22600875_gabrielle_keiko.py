# -*- coding: utf-8 -*-
"""
Dados duas listas, “a” com dez elementos e “b“com vinte elementos, escreva um
programa que faça a união dessas duas listas armazenando todos os elementos
numa terceira lista. Leia os dados das listas “a“e “b“ e no final mostre a listas com a
união.
"""

a = []
b = []
c = []

print("Digite os 10 elementos da lista A:")
for i in range(10):
    valor = int(input(f"Digite o {i + 1}º valor da lista A: "))
    a.append(valor)

print("\nDigite os 20 elementos da lista B:")
for i in range(20):
    valor = int(input(f"Digite o {i + 1}º valor da lista B: "))
    b.append(valor)

for i in range(10):
    c.append(a[i])

for i in range(20):
    c.append(b[i])

print("\nLista A:")
print(a)

print("Lista B:")
print(b)

print("União das listas A e B:")
print(c)