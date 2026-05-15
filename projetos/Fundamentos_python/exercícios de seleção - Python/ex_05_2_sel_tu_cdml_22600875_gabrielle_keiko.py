# -*- coding: utf-8 -*-
"""
Elabore o programa que verifica se o valor inteiro fornecido pelo usuário é par ou ímpar.
Analise o problema e verifique quais são os dados que o usuário precisa fornecer.
"""

numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print("O número", numero, "é PAR.")
else:
    print("O número", numero, "é ÍMPAR.")