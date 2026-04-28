# -*- coding: utf-8 -*-
"""
Construa o programa que calcule o peso ideal de uma pessoa.
"""

altura = float(input("Digite a sua altura: ").replace(",","."))
genero = input("Digite o gênero (M para masculino ou F para feminino): ").upper()


if genero == "M":
    peso_ideal = (72.7 * altura) - 58
    print("Peso ideal: %.2f" %peso_ideal, "Kg")

elif genero == "F":
    peso_ideal = (62.1 * altura) - 44.7
    print("Peso ideal: %.2f" %peso_ideal, "Kg")

else:
    print("Erro: Gênero inválido! Por favor, digite 'M' ou 'F'.")
