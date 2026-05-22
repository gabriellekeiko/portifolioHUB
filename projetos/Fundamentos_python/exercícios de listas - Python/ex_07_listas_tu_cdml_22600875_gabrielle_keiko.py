# -*- coding: utf-8 -*-
"""
Elabore um programa que, dadas duas listas de inteiros de 20 posições, efetue as
respectivas operações indicadas por uma outra lista de 20 posições de caracteres
também fornecido pelo usuário, contendo as quatro operações aritméticas em
qualquer combinação, armazenando os resultados numa quarta lista
"""

lista1 = []
lista2 = []
operacoes = []
resultados = []

print("Digite os 20 valores da primeira lista:")
for i in range(20):
    valor = int(input(f"Digite o {i + 1}º valor da lista 1: "))
    lista1.append(valor)

print("\nDigite os 20 valores da segunda lista:")
for i in range(20):
    valor = int(input(f"Digite o {i + 1}º valor da lista 2: "))
    lista2.append(valor)

print("\nDigite as 20 operações (+, -, * ou /):")
for i in range(20):
    op = input(f"Digite a operação da posição {i + 1}: ")
    operacoes.append(op)

for i in range(20):
    if operacoes[i] == "+":
        resultado = lista1[i] + lista2[i]
    elif operacoes[i] == "-":
        resultado = lista1[i] - lista2[i]
    elif operacoes[i] == "*":
        resultado = lista1[i] * lista2[i]
    elif operacoes[i] == "/":
        resultado = lista1[i] / lista2[i]
    else:
        resultado = "Operação inválida"

    resultados.append(resultado)

print("\nResultados:")

for i in range(20):
    print(lista1[i], operacoes[i], lista2[i], "=", resultados[i])