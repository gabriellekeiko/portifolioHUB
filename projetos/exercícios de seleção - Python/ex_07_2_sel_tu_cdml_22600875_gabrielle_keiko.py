# -*- coding: utf-8 -*-
"""
 Desenvolva um programa que calcule a média aritmética de um aluno que realizou duas
avaliações. Além do valor da média, inclua na tela de saída uma das mensagens: “Aluno
aprovado.” ou “Aluno reprovado.”. Considere que o aluno será aprovado com a média
maior ou igual a cinco.
"""

nota1 = float(input("Digite a nota 1: ").replace(",","."))
peso1 = float(input("Digite o peso da nota 1: ").replace(",","."))
nota2 = float(input("Digite a nota 2: ").replace(",","."))
peso2 = float(input("Digite o peso da nota 2: ").replace(",","."))
media = (nota1 * peso1 + nota2 * peso2) / (peso1 + peso2)

if media >= 5.0:
    print("Média do aluno:", round(media, 2), " Aluno aprovado.")
else:
    print("Média do aluno:", round(media, 2), " Aluno reprovado.")
