# -*- coding: utf-8 -*-
"""
Sabendo que a 01 pé equivale a 0.3048m, faça um programa que mostre na tela a
conversão de metros para pés, de 0 a 100metros. Seu programa deverá exibir o
cabeçalho abaixo e a cada 20 valores exibidos na tela, seu programa deverá solicitar
ao usuário que digite a tecla ENTER pra continuar, após isso deverá ser limpa a tela ,
exibido o cabeçalho e continuar o processamento até o final do programa.
Conversão metros – pés
Metros pés
"""

import os

contador = 0

for m in range(101):
    if contador % 20 == 0:
        if contador > 0:
            input("Pressione ENTER para continuar...") 
            os.system('cls')
        
        print("Conversão metros – pés")
        print("Metros | pés")

    pes = m / 0.3048
    print(m, "| %.2f" % pes)
    contador += 1