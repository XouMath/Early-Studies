#exercicio inicio
n1 = int(input("Digite o 1º Número:"))
n2 = int(input("Digite o 2º Número:"))
dif = n1 - n2
if n1 > n2:
    maior = n1
    menor = n2
elif n1 < n2:
    maior = n2
    menor = n1
else:
    maior = n1
    menor = n2
print(f'A diferença entre {maior} e {menor} é de {dif}')
if n1 == n2:
    n1 = n2
print(f'os números {n1} e {n2} são Iguais')