# -*- coding: utf-8 -*-
"""
Analise o resultado de uma transação comercial. Verifique a situação final do
comerciante trabalhando com os valores lidos, ou seja, o preço de compra e o preço de
venda
"""

preco_compra = float(input("Digite o preço de compra: ").replace(",","."))
preco_venda = float(input("Digite o preço de venda: ").replace(",","."))
print("Preço de Compra: R$", preco_compra)
print("Preço de Venda: R$", preco_venda)

if preco_venda > preco_compra:
    print("Resultado: Teve lucro.")

elif preco_venda < preco_compra:
    print("Resultado: Teve prejuízo.")

else:
    print("Resultado: Os valores são iguais.")
