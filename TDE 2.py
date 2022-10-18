# Exercicio 1

# a. Armazene os seguintes valores ao vetor: 1, 0, 5, -2, -5, 7
# vetor = [1, 0, 5, -2, -5, 7]
# b. Armazene em uma variável a soma dos valores nas posições 0, 1 e 5. Imprima na tela a soma.
# n1 = vetor[0] + vetor[1] + vetor[5]
# print(n1)
# c. Modifique o valor da posição 4 para 100.
# vetor[4] = 100
# print(vetor[4])
# d. Imprima na tela cada valor do vetor, um em cada linha.
# print('=' * 30)
# for i in range(0, 6):
#    print(vetor[i])

# Exercicio 2

import random

# vetor = [0] * 50
# soma = maior = 0
# menor = 1
# for i in range(0, 50):
#    a = random.randint(0, 20)
#    vetor[i] += a
#    soma += vetor[i]
#    if vetor[i] > maior:
#        maior = vetor[i]
#    if vetor[i] == 0:
#        menor = vetor[i]
#    else:
#        if vetor[i] < menor:
#            menor = vetor[i]
# print(vetor)
# print(f"A soma do vetor é {soma}.")
# print(f"Números de vezes que o 9 apareceu foi {vetor.count(9)}.")
# print(f"O maior valor é {maior} e o menor é {menor}")

# Exercicio 3

# vetor = []
# maior = cont = soma1 = soma2 = total = 0
# while True:
#    n = int(input("Digite: "))
#    if n < 0:
#        break
#    vetor.append(n)
#    if vetor[cont] > 5:
#        maior += 1
#    if vetor[cont] % 2 == 0:
#        soma1 += vetor[cont]
#    else:
#        soma2 += vetor[cont]
#    total = len(vetor)
#    cont += 1
# print(vetor)
# print(f"Números maiores que 5 no vetor são {maior}.")
# print(f"Quantidade de números pares {soma1} e ímpares {soma2}.")
# print(f"Quantidades de valores dentro do vetor são {total}.")

# Exercicio 4

# vetor = []
# for i in range(0, 6):
#    vetor.append(int(input("Digite: ")))
# vetor.reverse()
# print(vetor)

# Exercicio 5


# Exercicio 6


# Exercicio 7

#vetor = []
#for i in range(0, 15):
#    vetor.append(int(input("Digite: ")))
#print(vetor)
#for p, j in enumerate(vetor):
#    if j == 0:
#        vetor.remove(0)
#print(vetor)

# Exercicio 8

#vetor1 = []
#vetor2 = []
#vetor3 = []
#par = 0
#impar = 1
#for i in range(0, 10):
#    vetor1.append(int(input("Digite para o vetor1: ")))
#    vetor2.append(int(input("Digite para o vetor2: ")))
#for j in range(0, 10):
#    vetor3.insert(par, vetor1[j])
#    vetor3.insert(impar, vetor2[j])
#    par += 2
#    impar += 2
#print(vetor1)
#print(vetor2)
#print(vetor3)

