# -*- coding: utf-8 -*-
"""
Construa um programa que calcule a média aritmética de uma classe com dez alunos,
onde cada aluno teve uma avaliação. Gere um relatório, tela de saída, com o número e
a nota dos alunos, a média da turma e mostre também a quantidade de notas acima
da média da turma.
"""

notas = []
soma = 0

for i in range(10):
    nota = float(input(f"Digite a nota do aluno {i + 1}: ").replace(",","."))
    notas.append(nota)
    soma = soma + nota

media = soma / 10

acima_media = 0

for i in range(10):
    if notas[i] > media:
        acima_media = acima_media + 1

print("\nRELATÓRIO DA TURMA")

for i in range(10):
    print(f"Aluno {i + 1} - Nota: {notas[i]}")

print(f"\nMédia da turma: {media:.2f}")
print(f"\nQuantidade de notas acima da média: {acima_media}")