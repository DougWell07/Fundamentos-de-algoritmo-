dias=float(input("Digite a quantidade de dias que você ficou com o carro:"))
km= float(input("Digite a quantidade de quilometros que você rodou:"))
total_pagar= (0.15*km) + 60*dias
print("O valor a pagar é de: %.2f" %total_pagar)