# -*- coding: utf-8 -*-
"""
Faça um programa que calcula a média aritmética de uma turma com cinquenta
alunos, sabendo que cada aluno realizou uma avaliação. 
"""

soma_notas = 0
contador = 1

while contador <= 50:
    print("Nota do aluno", contador)
    nota = float(input("Digite a nota do aluno:").replace(",","."))
    soma_notas = soma_notas + nota
    contador = contador + 1
media = soma_notas / 50
print("Média aritmética da turma: %.2f" %media)
