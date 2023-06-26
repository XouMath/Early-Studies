
#inicio 
n1 = float(input("Digite a 1ª Nota: "))
n2 = float(input("Digite a 2ª Nota: "))
n3 = float(input("Digite a 3ª Nota: "))
n4 = float(input("Digite a 4ª Nota: "))

smtotal = (n1 + n2 + n3 + n4)/4

if smtotal >= 5:
    print(f'Aluno Aprovado com média {smtotal:.2f}')
else:
    print(f'Aluno Reprovado com média {smtotal:.2f}')
#concluido! 
