# -*- coding: utf-8 -*-
"""
Leia quatro valores digitados pelo usuário, armazene-os em uma lista, e no final
mostre os valores que estão armazenados na lista
"""

valores = []

for i in range(4):
    valor = int(input(f"Digite o {i + 1}º valor: "))
    valores.append(valor)

print("Valores armazenados na lista:", valores)

print("Valores na ordem inversa:")

for i in range(3, -1, -1):
    print(valores[i], end=" ")