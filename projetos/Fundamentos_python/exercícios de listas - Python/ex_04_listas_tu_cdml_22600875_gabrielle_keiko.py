# -*- coding: utf-8 -*-
"""
Construa um programa que preencha uma lista de 100 elementos inteiros, colocando
"1" na posição (= índice da lista) correspondente a um número par e "0" na posição (=
índice da lista) correspondente a um número ímpar.
"""

lista = []

for i in range(100):
    if i % 2 == 0:
        lista.append(1)
    else:
        lista.append(0)

print(lista)