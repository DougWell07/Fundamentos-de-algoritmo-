L=[]
i=0
for i in range(10):
    x= int(input("Digite um número:"))
    L.append(x)
print(f"Numeros: {L}")

maior = 0
for x in L:
    if x > maior:
        maior = x

print (f"Maior numero: {maior}")

indice = L.index(maior)
print(indice)


