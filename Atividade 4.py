salario = float(input("Digite o seu salário:"))
print(salario)
if salario > 1250.00:
    salario_sup = salario * 1.10
    print("O seu novo salário é de:", salario_sup)
if salario < 1250.00:
    salario_inf = salario * 1.15
    print("O seu novo salário é de:", salario_inf)