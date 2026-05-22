# -*- coding: utf-8 -*-
"""
Faça um programa que receba a temperatura média de cada mês do ano e armazeneas em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as
temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por
extenso: 1 – Janeiro, 2 – Fevereiro, ...).
"""

temperaturas = []
meses = [
    "Janeiro", "Fevereiro", "Março", "Abril",
    "Maio", "Junho", "Julho", "Agosto",
    "Setembro", "Outubro", "Novembro", "Dezembro"
]

soma = 0

for i in range(12):
    temperatura = float(input(f"Digite a temperatura média de {meses[i]}: "))
    temperaturas.append(temperatura)
    soma = soma + temperatura

media_anual = soma / 12

print(f"\nMédia anual das temperaturas: {media_anual:.2f}")
print("\nTemperaturas acima da média anual:")

for i in range(12):
    if temperaturas[i] > media_anual:
        print(f"{i + 1} - {meses[i]}: {temperaturas[i]} graus")