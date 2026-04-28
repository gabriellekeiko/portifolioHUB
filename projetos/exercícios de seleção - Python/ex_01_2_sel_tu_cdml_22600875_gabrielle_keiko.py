# -*- coding: utf-8 -*-
"""
Faça um programa que leia o ano de nascimento de uma pessoa e calcule sua idade.
Após isso verifique se ela já tem idade para votar (16 anos ou mais). 
"""

ano_atual = 2026
ano_nascimento = int(input("Digite o ano de nascimento: "))
idade = ano_atual - ano_nascimento
print("Ano de nascimento:", ano_nascimento)
print("Idade:", idade, "anos")
if idade >= 16:
    print("A idade é", idade, "anos e já pode votar.")
else:
    print("A idade é", idade, "anos e não pode votar.")