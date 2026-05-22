# -*- coding: utf-8 -*-
"""
Leia uma palavra e mostre-a na ordem inversa. Utilize a função comprimento da
string
"""

palavra = input("Digite uma palavra (sem acentos ou símbolos): ")

comprimento = len(palavra)

print("Palavra na ordem inversa: ", end="")

for i in range(comprimento - 1, -1, -1):
    print(palavra[i], end="")
