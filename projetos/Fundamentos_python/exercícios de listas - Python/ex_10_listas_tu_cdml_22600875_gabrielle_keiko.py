# -*- coding: utf-8 -*-
"""
Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine
quantos alunos com mais de 13 anos possuem altura inferior à média de altura
desses alunos.
"""

idades = []
alturas = []
soma_alturas = 0

for i in range(30):
    idade = int(input(f"Digite a idade do aluno {i + 1}: "))
    altura = float(input(f"Digite a altura do aluno {i + 1}: ").replace(",","."))

    idades.append(idade)
    alturas.append(altura)

    soma_alturas = soma_alturas + altura

media_altura = soma_alturas / 30

quantidade = 0

for i in range(30):
    if idades[i] > 13 and alturas[i] < media_altura:
        quantidade = quantidade + 1
        
print(f"\nMédia de altura da turma: {media_altura:.2f}")
print(f"Quantidade de alunos com mais de 13 anos e altura abaixo da média: {quantidade}")