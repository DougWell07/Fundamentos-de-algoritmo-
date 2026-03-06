
print("Sexo:")
print("1-Masculino")
print("2-Feminino")
sexo=float(input("Digite qual é o seu sexo:"))
altura=float(input("Insira a sua altura:"))
if sexo == 1:
   peso_ideal= (72.7*altura)-58
   print("O seu peso ideal é de: %.2f" %peso_ideal)
if sexo == 2:
   peso_ideal= (62.1*altura)-44.7
   print("O seu peso ideal é de: %.2f" %peso_ideal)