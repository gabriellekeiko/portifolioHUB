# -*- coding: utf-8 -*-
"""
Desenvolva um programa que leia vários números digitados pelo usuário e use o
valor -1 como condição (flag) de saída da estrutura de repetição. Na tela de saída,
mostre os números um ao lado do outro, separados por vírgula e ao término do
fluxograma a quantidade de números digitados.
"""

quantidade = 0
lista_numeros = "" 
num = 0
soma = 1

print("Digite os números desejados.")
print("(Para encerrar e ver o resultado, digite -1)")

while num != -1:
    num = int(input("Digite um número: "))
    if num != -1:
        if quantidade == 0:
            lista_numeros = str(num)
        else:
            lista_numeros = lista_numeros + ", " + str(num)
        quantidade = quantidade + 1
    soma += num
print("Números digitados:", lista_numeros)
print("Quantidade de números digitados:", quantidade)
print("A soma dos números digitados:", soma)
