# -*- coding: utf-8 -*-
"""
Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma.
O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. 
Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). 
Os valores referentes a cada uma das opções devem ser armazenados num vetor. 
Após os dados terem sido completamente informados, o programa deverá calcular o percentual de cada um dos concorrentes e informar o vencedor da enquete.
"""

sistemas = ["Windows Server", "Unix", "Linux", "Netware", "Mac OS", "Outro"]
votos = [0] * len(sistemas)  # Inicializa o vetor com zeros
total_votos = 0

while True:
    voto = int(input("Informe o valor (1-6, ou 0 para sair): "))
    
    if voto == 0:
        break
    
    elif 1 <= voto <= len(sistemas):
        votos[voto - 1] += 1
        total_votos += 1
    else:
        print("Valor inválido!")

print("\nSistema Operacional     Votos   %")
print("-------------------     -----   ---")

maior_votos = -1
vencedores = []

for i in range(len(sistemas)):
    percentual = 0
    if total_votos > 0:
        percentual = (votos[i] / total_votos) * 100
    
    print("%-19s     %-5d   %.0f%%" % (sistemas[i], votos[i], percentual))
    
    if votos[i] > maior_votos:
        maior_votos = votos[i]
        vencedores = [sistemas[i]]
    elif votos[i] == maior_votos and maior_votos > 0:
        vencedores.append(sistemas[i])

print("-------------------     -----   ---")
print("Total                   %d" % total_votos)
if total_votos > 0:
   
    if len(vencedores) == 1:
        print("\nO Sistema Operacional vencedor foi o %s, com %d votos." % (vencedores, maior_votos))
    else:
        nomes_vencedores = ""
        for v in vencedores:
            nomes_vencedores += v + " "
        print("\nHouve um EMPATE entre os sistemas: %s (com %d votos cada)." % (nomes_vencedores, maior_votos))