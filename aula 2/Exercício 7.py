distancia=float(input("Qual a distância percorrida:"))
if distancia <= 200:
    valor = distancia * 0.5
    print("O valor a ser pago da viagem é de: %.2f" %valor)
if distancia > 200:
    valor = distancia * 0.45
    print("O valor a ser pago é de: %.2f" %valor)