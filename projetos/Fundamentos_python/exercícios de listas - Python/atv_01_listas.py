# -*- coding: utf-8 -*-
"""
1. Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:

Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem;
"""

notas = []

while True:
    valor = float(input("Digite uma nota (ou -1 para encerrar): ").replace(",","."))
    if valor == -1:
        break

    notas.append(valor)

quantidade = len(notas)
print("\nQuantidade de valores lidos:", quantidade)

if quantidade > 0:
    print("Valores informados:", end=" ")
    for n in notas:
        print(n, end=" ")

    print("Valores na ordem inversa:")
    for i in range(quantidade - 1, -1, -1):
        print(notas[i])

    soma = 0
    for n in notas:
        soma += n
    print("Soma dos valores: %.2f" % soma)
    media = soma / quantidade
    print("Média dos valores: %.2f" % media)
    acima_da_media = 0
    for n in notas:
        if n > media:
            acima_da_media += 1
    print("Quantidade de valores acima da média:", acima_da_media)
    abaixo_de_sete = 0
    for n in notas:
        if n < 7:
            abaixo_de_sete += 1
    print("Quantidade de valores abaixo de sete:", abaixo_de_sete)

print("\nProcessamento concluído. O programa foi encerrado com sucesso!")