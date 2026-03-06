numero= int(input("Digite um numero:"))
i=0

while True:
    if numero >= 0 and numero <= 10:
        print("numero aceito")
        numero += 1
        break
    else:
        print("Digite outro número")
        